This Django webapp uses a simple HTML form to capture and process input data as 4 fields:
    First Name, Surname, Date of Birth, and an .xlsx file containing their monthly income and expenditure. 
The information from the excel sheet is parsed using tablib, and then the data is added to the sqlite database as models.
The relevant data is then used to form a Pandas dataframe, which is used to draw a line and bar graph with Plotly.

*** NOTES ***

LIMITATION- Currently only accepting .xlsx sheets with 3 columns

BIG CHANGE:
No more tablib, convert xlsx straight to dataframe, use to plot graphs, turn df to json and store that in the user details model.

-I used a very straightforward Django setup as per the documentation/many tutorials available online.

-Swapped matplotlib for plotly, simpler integration of interactive charts

-Added responsiveness for mobile.


*** NEXT STEPS ***

-Add user login
-Add recapture