# Import required libraries
import json
import pandas as pd
from flask import Flask, render_template, flash, redirect, url_for
from werkzeug import Response


# Function to load data from JSON file and convert it into pandas dataframe
def load_data(filename: str) -> pd.DataFrame:
    with open(filename) as f:
        data = json.load(f)
    return pd.DataFrame(data)


# Load employee and request data into pandas dataframes
employee_df = load_data('Employees.json')
request_df = load_data('Requests.json')

# Add columns to request_df for employee name, email, and department using employee_df
request_df['name'] = request_df['employee_id'].map(employee_df.set_index('employee_id')['name'])
request_df['email'] = request_df['employee_id'].map(employee_df.set_index('employee_id')['email'])
request_df['department'] = request_df['employee_id'].map(employee_df.set_index('employee_id')['department'])

# Format date columns in request_df
date_cols = ['date_requested', 'game_date', 'entry_time']
for col in date_cols:
    try:
        request_df[col] = request_df[col].str.replace('.0', '', regex=False)
        request_df[col] = pd.to_datetime(request_df[col])
        request_df[col] = request_df[col].dt.strftime('%Y-%m-%d %I:%M %p')
    except:
        pass

# Create flask application instance
application = Flask(__name__)

# Set a secret key for the application
application.secret_key = 'abcdef12345!@#$%'


# Define a route for the home page
@application.route('/', methods=['GET', 'POST'])
def index() -> str:
    return render_template('index.html')


# Define a route for the employee request page
@application.route('/employee_request/<string:employee_email>/<int:emp_id>', methods=['GET'])
def employee_requests(employee_email: str, emp_id: int) -> Response | str:
    # Validate input parameters
    if not isinstance(employee_email, str) or not isinstance(emp_id, int):
        flash("Invalid input parameters")
        return redirect(url_for('index'))
    # Check if the employee with the given email and id exists in employee_df
    try:
        employee = employee_df.loc[(employee_df['employee_id'] == emp_id) & (employee_df['email'] == employee_email)].iloc[0]
    except IndexError:
        flash("Invalid Credentials")
        return redirect(url_for('index'))
    # Retrieve all requests made by the employee
    requests = request_df.loc[request_df['employee_id'] == emp_id].to_dict('records')
    # Render the employee request page with the employee information and requests
    return render_template('employee_request.html', employee=employee, requests=requests)


# Define a route for the department request page
@application.route('/department_request/<string:employee_email>/<int:emp_id>', methods=['GET'])
def department_requests(employee_email: str, emp_id: int) -> Response | str:
    # Validate input parameters
    if not isinstance(employee_email, str) or not isinstance(emp_id, int):
        flash("Invalid input parameters")
        return redirect(url_for('index'))
    # Check if the employee with the given email and id exists in employee_df
    try:
        employee = employee_df.loc[(employee_df['employee_id'] == emp_id)
                                   & (employee_df['email'] == employee_email)].iloc[0]
    except IndexError:
        flash("Invalid Credentials")
        return redirect(url_for('index'))
    # Retrieve all requests made by employees in the same department as the employee
    dept_employee_ids = employee_df.loc[employee_df['department'] == employee['department'], 'employee_id']
    dept_requests = request_df.loc[request_df['employee_id'].isin(dept_employee_ids)]
    department = dept_requests.department.unique()[0]
    # Render the department request page with the employee information, requests, and department name
    return render_template('department_request.html', employee=employee, requests=dept_requests, department=department)


# define a route for the all requests page
@application.route('/all_requests/<string:employee_email>/<int:emp_id>', methods=['GET'])
def all_requests(employee_email: str, emp_id: int) -> Response | str:
    # Validate input parameters
    if not isinstance(employee_email, str) or not isinstance(emp_id, int):
        flash("Invalid input parameters")
        return redirect(url_for('index'))
    # Get the admin user by matching the employee ID, email and isAdmin status
    try:
        admin = employee_df.loc[(employee_df['employee_id'] == emp_id) & (employee_df['email'] == employee_email)
                                & (employee_df['isAdmin'] == 'yes')].iloc[0]
    except IndexError:
        # If no matching admin user is found, flash an error message and redirect to index page
        flash("Invalid Credentials")
        return redirect(url_for('index'))
    # Render the all_requests.html template with the admin user and all requests data
    return render_template('all_requests.html', employee=admin, requests=request_df)


if __name__ == "__main__":
    # Run the Flask app in debug mode
    application.run()
