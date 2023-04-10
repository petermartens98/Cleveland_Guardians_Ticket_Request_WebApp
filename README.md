# Guardians_Ticket_Request_WebApp
Cleveland Guardians coding assessment web UI for fictional employee ticket requests.

Using the JSON provided:
-	Employees
-	Ticket Requests

1. Create a web page that will show an employee their own ticket request. Employees should be able to see if their request was approved, the number of tickets, the date of the game requested, the time they entered the ballpark, if they were at the game

2. Bonus points: Add a way to show requests from others in the same department. If the employee is an admin, they should be able to see requests from all departments. 
Feel free to use any technology you feel comfortable with to complete the task. Be as creative as you wish, we are looking for web page design with good form as well as function. Let us know the libraries you are using as well as any design frameworks that might be involved so that we can install your dependencies.

Project Description:
This is a Flask application that allows users to view ticket requests made by employees. The application uses Python to load data from JSON files and convert them to pandas data frames. The application has three main routes - employee request page, department request page, and all requests page.
The employee request page allows users to view all the ticket requests made by a specific employee, which are displayed based on their email and employee ID. The department request page displays all the requests made by employees in the same department as the given employee.
The all requests page is accessible only to an admin user and displays all the requests made by all employees. This page provides a comprehensive overview of all the ticket requests made in the organization. 

Below is more detailed descriptions on the individual project files:

## Project Heirarchy File Descriptions:
 
### requirements.txt : Contains Project Dependencies

### application.py Description:
This is a Flask application that uses Python to load data from JSON files, convert them to pandas data frames, and display the data on different web pages. The application has three main routes - employee request page, department request page, and all requests page.

###Templates:
### Index.html Output and Description:

![image](https://user-images.githubusercontent.com/87671757/231012194-275ba330-3574-4d47-b37d-36d3dcc0b0a5.png)

This is an HTML page that serves as a form for submitting ticket requests for Guardians event. The page features a centered header with the title "Guardians Ticket Requests" and a form that requires users to input their email and employee ID. Upon submitting the form, users can select one of three buttons that indicate whether the request is being made by an employee, a department, or an admin for all requests. The page also includes a script that checks whether the employee ID input is an integer and displays an error message if it is not. Finally, the page displays any flashed messages using Jinja2 templating. The styling for the page is defined in the main.css file, which is linked in the head of the HTML document.

### employee_request.html Output and Description:

![image](https://user-images.githubusercontent.com/87671757/231012217-b95f999a-99e7-4804-9626-215e7a51a1ab.png)
 
This is an HTML template for the employee request page of a Flask application that retrieves and displays ticket request information for a specific employee. The template uses Python and pandas to load data from JSON files and display it in a table format on a web page. The page displays information about the selected employee, such as their name, email, department, and whether they are an admin user. It also lists all the ticket requests made by the employee, including the request ID, number of tickets requested, date requested, whether the request has been approved, game date, and entry time into the ballpark. The template includes a home button that redirects the user to the home page of the application.

### department_request.html Output and Description: 

![image](https://user-images.githubusercontent.com/87671757/231012245-b249814a-c2ea-4c40-935d-66a6ce20a103.png)
 
This is an HTML page template that displays a table of ticket requests made by employees in a department. The page uses requests_table.CSS to style the table and includes external links to CSS and JavaScript files. The table is populated using a for loop that iterates over a data frame containing the ticket requests. The table includes columns for request ID, employee name, email, date requested, number of tickets, approval status, game date, and entry time. The template also includes a home button that redirects the user to the home page of the application
The page also includes JavaScript code that initializes the DataTables library to provide search and ordering functionality to the table. The language settings for the DataTables library are customized to display "Search Requests:" in the search box and a message indicating the range of records currently displayed.

### all_requests.html Output and Description:

![image](https://user-images.githubusercontent.com/87671757/231012264-bf43bc3e-28f9-4651-a776-baa8885fe226.png)
 
This code is an HTML page template that displays a table of all ticket requests for all employees. The table is generated dynamically using a Flask template engine to iterate over a pandas DataFrame object, which contains the ticket request data. The table is styled with requests_table.CSS and also uses an external CSS file and the DataTables plugin from jQuery. 

The table has ten columns, which display the following data for each ticket request: request ID, employee ID, name, email, department, date requested, number of tickets, approval status, game date, and entry time.
The DataTables plugin adds several features to the table, including pagination, the ability to search and sort the data, and responsive design that adjusts the table layout based on screen size. The plugin also provides translations for the table's user interface elements, such as a search box and pagination buttons. 

### Static:
### main.css Description:
This code is a set of CSS styles used for index.html and employee_requests.html. It includes styles for the body, headings, form, buttons, and tables.
The body style sets the font family, background color, and removes any default margins and padding.
There are three heading styles: h1, h3, and h4, which have different font sizes, colors, and margins.
The employee form style sets the width, margin, padding, background color, and border radius of a form. It also styles the label and input fields for email and text types.
The button styles include a submit button and a home button, which have different background colors, padding, margins, and border radii. The submit button has a hover effect that changes the background color.
The table style sets the border-collapse to collapse, the width to 80%, and a maximum width of 800px, with margins set to auto. It also sets styles for the table headers and data cells, including text alignment, padding, and background colors for alternating rows.
### request_table.css Description:
This code is a set of CSS styles used for department_request.html and all_requests.html. It includes global styles that apply to all elements, such as setting margin and padding to 0, and box-sizing to border-box.
It also includes specific styles for the body, headings, form elements (labels, selects, and options), buttons, and tables.
The body has a background color of #00385D and font-family of Arial, Helvetica, sans-serif.
Headings have a font size of 2em and are centered.
Form labels, selects, and options have a text color of white.
The home_button class is defined with specific styles for display, padding, margin, text alignment, font size, border, border-radius, color, and background color.
Table styles include setting the width to 50%, collapsing borders, adding padding, and setting alternating row background colors. Table header cells have a background color of #3d85c6 and a text color of white, while table data cells have black text.

Additional styles are defined for hover and active states of elements, as well as specific styles for the DataTables plugin for jQuery, such as setting colors for search input and pagination links.


