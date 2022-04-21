# MYSQL-Performance-Training-Suite
MYSQL training performance suite is an interactive game created using MySQL and Streamlit. 
This game helps the player understand the rules and guidelines to be followed while adding indexes to a large database.

# Steps to run the app:-

  1) Install MySQL into your system. (https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

  2) Install streamlit into your system. ( Enter command "pip install streamlit" in your terminal).
  
  2) Clone this repository into your local system.
  
  3) Open the cloned repository in an editor of your choice.
  
  3) In the repository, create a folder named “.streamlit”.
  
  4) Within the folder, create a file named “secrets.toml”.
  
  5) Open this file and copy the following contents into it.
  
                    [mysql]
                    host = "localhost"
                    port = 3306
                    database = "xxx"
                    user = "root"
                    password = "yyy"

	Note: 
      
      Replace database value (xxx) with your database name.
      Replace password value (yyy) with your MySQL password. 

  6) Open terminal and move to the repository folder. 
     
     Enter → pip install mysql-connector-python
     
  7) Finally, to run the app, 
  
     Enter → streamlit run main.py
     
     The app will open up in your browser. 


# This repository contains 6 files:

data.py → contains all the data that is used across various pages of the app. 

db.py → connects the app to MySQL using mysql.connector

desc.py → code for the description page.

main.py → main page that links the various pages of the app. 

pages.py → code for the question pages.  

requirements.txt → text file containing the mysql connector version.

