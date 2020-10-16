# Expenso
Expenso is an expense-management software basically for Organisations. It will track your expenses, and give it a tabular as well as a graphical view so that you need to know where to tighten up.

 

It contains two web-apps:

-   Register
   
-   Input Expense
   
-   ViewExpenses
   

 
 

**Register** fulfills the following functionalities:

-   Let the user login(Authenticate) with their given Id and Password.
   
-   After Authenticating, it allows you to Register the details of your new Employee
   

 

**InputExpense** fulfills the following functionalities:

-   It allows you to add other expenses on various sections like Insurance, Allowance, many more that you did on a particular employee on daily basis.
   

 

**ViewExpenses** fulfills the following functionalities:

-   It allows you to track down the expenses: daily, weekly, and monthly.
   
-   It allows you to track down the expenses of the company in various sectors like allowances, insurance, and many more.
   
-   It allows you to track down the expenses made on particular departments like Technical, Finance, and many more.
   
-   It also shows the expenditure on each employee for the entire month.
   



# Extra Features

-   Beautiful Pie Chart for better visualization.
   
-   Complete tabular data of the entire month on the employee, each sector and each department.
   
-   Clean and Clutter-free UI.
   

 
 

# Deployment

-   This web apps are deployed on
   

 
 
 
 
 
 
 
 

# Table Of Contents

1.  Pre-Requisites
   
2.  Setup and Installation.
   
3.  Starting the Project.
   
4.  Tech Stack Used
   
5.  Features and Implementation.
   
6.  Software Designs and Dataflow.
   
7.  Working with the app
   
8.  Working Demo.
   
9.  Contact Us.
   

 

# Pre-Requisites

-   Django Framework Should be Installed on your system.
   
-   Python v3.8(or above) should be installed on your system.
   
-   PIP Packages should be installed on your system.
   

 

# Installation

-   Clone the repository.
   

  **TODO: Add deployment link**

 

-   Run the following command -
   

  **TODO: Requirements.txt**

![](https://lh3.googleusercontent.com/3iMyf-b6GbiAAbPB3pqauIxNUpPHFYn1c_UpZ-0AhewDG8GUeJW6FXxxGItVKFBjupB5NOfu7i7YsJuiMjsyX3zCDdlwvPa6m4JfELuQTAUel6NpCDnJ1Bpk0F4Hk6piSFicGADp)

 

-   Make migrations to the database.
   

 

![](https://lh4.googleusercontent.com/Vh1H03_TiqqYdClU6Ko6ZOI86aoroc_JYVjPenACvtgXX0rkQj1B0qBD6D2tm1gObOr8GV2FDS6chH5bH-Mf_GYRcrrU8_z88qJbeGy0Y4ihiNzdvSGsNPM7t6GVPSQfFxGCRmaV)

 

# Starting the Project

 

-   Start the project using -
   

 

![](https://lh5.googleusercontent.com/EEI9alJXFjtgkPYlQ8aM2rUWe9fwPdT0TbUe9eELgtJMfztC3ymtwNadHJw13boygwJ4-Qg3HHngw30-TYMyMGIHImGwNC6ah6MLVDbRY_JHGeyR5p89cQ5tSXWu_BPW9n2Fd0np)

 

-   Browse to ____________________ to see you web app.
   

 
 

# Tech Stack Used

 

**Frontend**

-   HTML
   
-   CSS
   
-   Javascript
   
-   Bootstrap
   

 

**Backend**

-   Django
   
-   Python 3.8
   

**Database**

-   Sqlite3
   

 
 

# Fetaures and Implemention

 

-   After starting the server, the landing page will ask you to Login Through Given Id and Password.
   
-   You won’t be able to access anything before Login in the Login Page
   
-   After clicking on Login In button, you will be redirected to the login page to authenticate your ID and Password.
   
-   On the Home Page, You will see three options Register, InputExpenses, and View Expenses.
   
-   If the employee you want to look for is new first get him registered in the Register.
   
-   The employee details are then stored in the Employee database implemented using sqlite3.
   
-   Also, all the URLs are stored in the urls database.
   
-   If the employee is registered but you want to add the expense you did on that particular employee you can go to InputExpense and add it there
   
-   Employee expenditure in the various tags(Allowance, Insurance, etc) is stored in other database Expense.
   
-   If you wanna track down the expense Click on ViewExpense:
   

-   Click on the Track By Time if you want to track the total expense daily, weekly, or monthly.
   
-   Click on the Track By Tag if you want to track the total expense for various other expenses(Allowance, Insurance, etc) monthly.
   
-   Click on the Track By Department if you want to track the total expense of various departments monthly.
   
-   Click on the Track Per Employee if you want to track the total expense on a particular employee monthly.
   

 

-   After storing the user’s database we extract those data when we use our ViewExpense.
   
-   Here we extract data like the EmpId, tags, department, etc to meet the demands of the various ViewExpanses functions.
   
-   After logging out, the user will be redirected to the login page.
   
-   Data Structures used- List for storing various expenses details of the employee also for various tags and departments so that they can be searched accordingly.
   



# Working with the App

 

**Login Page**

-   Clicking on the Login with the login button will take you to the Login page.
   

 

**Home Page**

-   The home page containing three navbars - Registration, InputExpense, ViewExpense.
   

 

-   The Registration has a small detail form for the new Employee.
   
-   The Input Expense has a small detail form about the tag in which the expense for the particular employee is made.
   
-   The View Expense has further four dropdown cards, Track by time, Track by tag, Track by department, Track per Employee.