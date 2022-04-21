import desc
import streamlit as st

#Function to display the description page
def description():
    st.title('Description')
    st.subheader('Problem Statement')
    st.write('''Peter owns a clinic. In order to store the basic details of his patients, he uses 
    MySQL. Soon, the database grows in size and Peter realises that he needs a faster and cost effective way to retrieve his data. 
He comes across the concept of indexes and needs help applying it in his database. 
 ''')
    st.subheader('About Indexes')
    st.write('''Indexes are used to find rows with specific column values quickly. Without an index, MySQL must begin with the 
    first row and then read through the entire table to find the relevant rows. The larger the table, the more this costs. 
    If the table has an index for the columns in question, MySQL can quickly determine the position to seek to in the 
    middle of the data file without having to look at all the data. This is much faster than reading every row sequentially.''')
    st.write('''Check out official documentation [here](https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html
)''')
    st.subheader('''Steps to Load Peter's database into your local system''')
    st.write('''
    1. Installing Mysql server: Download it from this [link](https://dev.mysql.com/downloads/mysql/) and then Install mysql by opening the downloaded file 
    2. In your command line, create a database named “Patient_Details” and use it(Run below command in mysql to create database).
    ''')
    st.code('''
    create database Patient_Details;''')
    st.write('''
    3. To create tables run below commands in mysql:''')
    st.code('''create table personal_info(sno int,fname text,lname text,age int,gender char(2),marital_status text,ctime timestamp,mtime timestamp);''')
    st.code('''ALTER TABLE personal_info MODIFY ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.code('''ALTER TABLE personal_info MODIFY mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.code('''create table address(sno int,street text,city text,state text,zip text,ctime timestamp,mtime timestamp);''')
    st.code('''ALTER TABLE address MODIFY ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.code('''ALTER TABLE address MODIFY mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.code('''create table contact_details(sno int,email text,phone_number text,ctime timestamp,mtime timestamp);''')
    st.code('''ALTER TABLE contact_details MODIFY ctime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.code('''ALTER TABLE contact_details MODIFY mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
''')
    st.write('''Yay! All the tables have been successfully created!''')
    st.write('''4. Loading .csv files into database:-(Run below commands for loading in mysql)''')
    st.code('''SET GLOBAL local_infile=1;''')
    st.code('''quit;''')
    st.code('''/usr/local/mysql/bin/mysql --local-infile=1 -u root -p''')
    st.code('use Patient_Details;')
    st.write("Download the CSV files from this [link](https://drive.google.com/file/d/1NB2qdkHdPdaTAm2ONrElpEViEyqlAqA9/view?usp=sharing) and unzip it")
    st.code('''LOCAL INFILE 'locationofpersonal_info.csv' INTO TABLE personal_infoFIELDS TERMINATED BY ',';  ''')
    st.write('''In the command above replace 'locationofpersonal_info.csv' with actual location of personal_info.csv file in your computer.''')
    # st.write('''Download the 'address.csv' file from this [link]()''')
    st.code('''LOCAL INFILE 'locationofaddress.csv' INTO TABLE address FIELDS TERMINATED BY ',';''')
    st.write('''In the command above replace 'locationofaddress.csv' with actual location of address.csv file in your computer.''')
    # st.write("Download the 'contact_details.csv' file from this [link](https://drive.google.com/file/d/1JoeQWo-MM53xnZEhyf-nuqVtUMe7JnGu/view?usp=sharing)")
    st.code('''LOCAL INFILE 'locationofcontact_details.csv' INTO TABLE contact_details FIELDS TERMINATED BY ',';''')
    st.write('''In the command above replace 'locationofcontact_details.csv' with actual location contact_details.csv file in your computer.''')
    st.write('''Hooray! The tables values have been successfully loaded!
	We’re all set to begin! 
''')
    st.subheader('Rules to play the game')
    st.write(' ')
    st.write('1) Index names must always be in the format “i<column_name1><column_name2>.." ')
    st.write('      For example: ')
    st.write('      Index on column age → iage')
    st.write('      Index on columns fname and age → ifnameage')
    st.write(' ')
    st.write('2) Answering a question correctly without using any hint adds your score by 2.')
    st.write('If the hint is used for answering a question the score adds up by 1')
    st.write('      If output is shown, the score does not change.')
    


    