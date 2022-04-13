#Headings for sidebar
Headings=['DESCRIPTION','AND1','AND2','AND3','RANGEOFVALUES1','RANGEOFVALUES2','RANGEOFVALUES3','RANGEOFVALUES4','RANGEOFVALUES5'
,'INDEXORDER','GROUPBY1','GROUPBY2','GROUPBY3','ORDERBY1','ORDERBY2','ORDERBY3','ORDERBY4','ORDERBY5',
'FLAGS AND LOW CARDINALITY1','FLAGS AND LOW CARDINALITY2','FLAGS AND LOW CARDINALITY3','OR1','OR2','COVERINGINDEX','TEXT/BLOB',
'DATE','JOIN1','JOIN2','IN SELECT1','IN SELECT2','FULLTEXT'
]
#List of Questions
Question_Queries=[
    'Display the personal information of all the patients whose age is 45.',
    'Display the details of patients whose age is 38 and gender is male?',
    "Display the details of patients whose last name is 'Taylor'. (Note: Case insensitive)",
    'Display the count of patients whose age is greater than 40?',
    'Display the count of patients whose age is between 40 and 50?',
    'Display all the first names of patients whose last name starts with letter T?',
    "Display all the first names of patients whose last name ends with letter 'r' ",
    "Display the count of patients whose first name starts with letter 'A' and gender is Male?",
    "Display the firstname and lastname of patients whose first name starts with 'A' and last name is 'Taylor'?",
    "Display the first name and last name of patients whose firstname is Marion and lastname is Marshall and grouped by firstname and lastname",
    "Display all the different age values in personal_info table and also the count of number of people in that age sorted by age in ascending order",
    "Display the first name and length of the last name of patients, with first name as 'Marion' and grouped by first name and the length of last name",
    "Display the age of patients in descending order whose first name is Marion and last name is Marshall",
    "Display the first name, last name and maximum age of patients whose first name is Alex grouped by the first and last names and ordered by last name",
    "Display the first name, last name and maximum age of patients whose first name is Alex, last name starts with D,  grouped by the first and last names and ordered by the maximum ages",
    "Display all the personal information of patients whose first name is Marion ordered by last name in ascending and age in descending order.",
    "Display all the personal information of the first 20 patients whose first name is Marion ordered by age in descending order",
    "Display the first name of patients who are married.",
    "Display the last name of patients who are not married and have their first name as 'Alex'.",
    "Display all the personal information of first 5000 patients who are not married and have ctime higher than 2020/01/01 and first name is 'Alex'.",
    "Display the firstname and lastname of patients whose age is either 38 or 40?",
    "Display the first name of patients(without repetition) whose age is 38 or last name is Taylor.",
    "Display all the contact details of patients whose serial number is 9999975, phone number is (726) 238-9825 and email id is pij@darefhaf.lb",
    "Display all the personal information of patients with first name starting with Al and last name as Taylor",
    "Display a street whose ctime is after 2020-01-01 and belongs to state 'MO'",
    "Display the fname and city of patients whose fname ='Alice'?",
    "Display the fname and city and email of patients whose lname='Taylor'?",
    "Display the first name of patients whose first name starts with 'T' and street name starts with 'A'?",
    "Display the first name that starts with 'A' and street name starts with 'V', ordered by state?",
    "Display the details of patients whose first name or last name is either Alice or Parker"
      ]
#List of Hints
Hints=[
'Given a WHERE with a bunch of expressions connected by AND: Include the columns (if any), in any order, that are compared to a constant and not hidden in a function.'
,'Given a WHERE with a bunch of expressions connected by AND: Include the columns (if any), in any order, that are compared to a constant and not hidden in a function.'
,'Given a WHERE with a bunch of expressions connected by AND: Include the columns (if any), in any order, that are compared to a constant and not hidden in a function.'
, 'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Include one column to index used in range operator like BETWEEN,>,LIKE'
,'Index order matters a lot'
,'Indexing columns in GROUP BY and ORDER BY  in the same order helps optimise queries.'
,"Indexing columns in GROUP BY and ORDER BY  in the same order helps optimise queries. But don't index columns which are embedded inside functions"
,'ORDER BY indexes are added at the end of the other indexes that are being built.'
,'Indexing on columns are embedded in functions are not helpful'
,'Indexing on columns are embedded in functions are not helpful'
,"Answer varies depending on MySQL version.If the mysql version is below 8.0 then If there are multiple columns in the ORDER BY, and there is a mixture of ASC and DESC, do not add the ORDER BY columns to index, they won't help.If the mysql version is above 8.0 then If there are multiple columns in the ORDER BY, and there is a mixture of ASC and DESC,  add the ORDER BY columns to index, they will help."
,"Check if the limit value gets all the way through the order by"
,"Indexing a column where the value occurs more than 20% time is not of any use."
,"Compound indexing helps in this case."
,"Compound indexing helps in this case."
,"USE IN instead of OR and then add index."
,"Combine the conditions using two separate queries with UNION rather than using OR"
,"We can add up to 5 columns in an index."
,"Texts cannot be directly indexed."
,"Don't use the like operator while searching for dates. Use '>' operator in this case."
,"Join the tables and then retrieve values."
,"Add indexes to relevant columns of all tables"
,"Use JOIN to combine the tables"
,"Use JOIN to combine the tables and combined indexes."
,"Use fulltext to search fname and lname columns together."
]

#List of Optimised Output Queries
Output_queries=[
  'select * from personal_info where age=45;',
  "select * from personal_info where age=38 and gender='M'",
  "select * from personal_info where LOWER(lname)='taylor'",
  "select count(*) from personal_info where age>40;",
  "select count(*) from personal_info where age between 40 and 50;",
  "select fname from personal_info where lname like 'T%';",
  "select fname from personal_info where lname like '%r';",
  "select count(*) from personal_info where fname like 'A%' and gender='M';",
  "Select fname,lname from personal_info where fname like 'A%' and lname='Taylor';",
  "Select fname,lname from personal_info where fname='Marion' and lname='Marshall' group by fname,lname;",
  "select age,count(*) from personal_info group by age order by age;",
  "Select fname,length(lname) as length_lname from personal_info where fname='Marion' group by fname,length_lname;",
  "Select age from personal_info where fname='Marion' and lname='Marshall' order by age desc;",
  "Select fname,lname,max(age) from personal_info where fname='alex' group by fname,lname order by lname;",
  "Select fname,lname,max(age) as max_age from personal_info where fname='Alex' and lname like 'D%'  group by fname,lname order by max_age;",
  "Select * from personal_info where fname='Marion' order by lname asc,age desc;",
  "Select * from personal_info where fname='Marion' order by age desc limit 20;",
  "Select fname from personal_info where marital_status='true';",
  "Select lname from personal_info where marital_status='false' and fname='Alex';",
  "Select * from personal_info where marital_status='false' and ctime>'2020-01-01' and fname='Alex' limit 5000;",
  "select fname,lname from personal_info where age IN (38,40);",
  "Select fname from personal_info where age=38 Union distinct Select fname from personal_info where lname='Taylor';",
  "select * from contact_details where sno=9999975  and  phone_number='(726) 238-9825' and email='pij@darefhaf.lb';",
  "Select * from personal_info where fname like 'Al%' and lname='Taylor'",
  "select street from address where ctime>'2020-01-01' and state='MO';",
  "Select fname,city from personal_info join address on personal_info.sno=address.sno where fname='Alice';",
  "Select fname,city,email from personal_info join address on personal_info.sno=address.sno join contact_details on address.sno=contact_details.sno where lname='Taylor';",
  "Select fname from personal_info join address using(sno) where fname like 'T%' and street like 'A%';",
  "Select fname from personal_info join (select * from address where street like 'V%' order by state)b using (sno) where fname like 'A%';",
  "Select * from personal_info where MATCH(fname,lname) AGAINST('alice parker');"


]

#List of Answers
Output_answers=[
"Query: select * from personal_info where age=45;We have to create an index on column age."
,"Query : select * from personal_info where age=38 and gender = 'M'; We have to create an index on columns age and gender."
,"Query: select * from personal_info where LOWER(lname)='taylor'; No Use of creating an index on lname because it is embedded in a function in where.."
,"Query: select count(*) from personal_info where age>40;Creating an index on column age would help in increasing query performance."
, "Query: select count(*) from personal_info where age BETWEEN 40 and 50; Creating an index on age will increase the query performance."
, "Query: select fname from personal_info where lname like 'T%';Creating an index on column lname will increase the query performance."
, "Query: select fname from personal_info where lname like '%r';No use of creating index on lname it would be useful if lname like 'r%' in where."
, "Query: select count(*) from personal_info where fname like 'A%' and gender='M';Creating a combined index on columns gender and fname (index order matters) will increase the query performance.Index(gender,fname) works but index(fname,gender) won't."
, "Query:Select fname,lname from personal_info where fname like 'A%' and lname='Taylor'; Unoptimised: Creating index with (fname,lname)Optimised: Creating index with (lname,fname) because we have full lastname and part of firstname.The format of the index would be 'lastnamefirstname' so it will use the full lastname to find out the rows to the given query."
, "Query: Select fname,lname from personal_info where fname='Marion' and lname='Marshall' group by fname,lname; Index on fname,lname can be created.If there is a GROUP BY, all the columns of the GROUP BY should now be added, in the specified order, to the INDEX you are building."
, "Query:  select age,count(*) from personal_info group by age order by age; Create an index on the age column so it will work more efficiently."
,"Query:Select fname,length(lname) as length_lname from personal_info where fname='Marion' group by fname,length_lname; Index on fname can be created. If you are grouping by an expression(including function calls),you cannot use that column in index so including lname column while creating index is useless here."
,"Query:Select age from personal_info where fname='Marion' and lname='Marshall' order by age desc; Index on fname,lname and age can be created.If there is an ORDER BY, all the columns of the ORDER BY should be added, in the specified order, at the end of the INDEX you are building."
,"Query:Select fname,lname,max(age) from personal_info where fname='alex' group by fname,lname order by lname; Index on fname and lname can be created."
,"Query:Select fname,lname,max(age) as max_age from personal_info where fname='Alex' and lname like 'D%'  group by fname,lname order by max_age; Index on (fname,lname)(Exact order) can be created.If there are both group by and order by on different columns , index on group by column in enough"
,"Query:Select * from personal_info where fname='Marion' order by lname asc,age desc; Index on fname can be created.(MySQL Version Below 8.0) Index on fname,lname,age can be created(MySQL Version After 8.0)"
,"Query:Select * from personal_info where fname='Marion' order by age desc limit 20; Index on fname,age can be created. Normally a LIMIT cannot be applied until after lots of rows are gathered and then sorted according to the ORDER BY. But, if the INDEX gets all the way through the ORDER BY, only (OFFSET + LIMIT) rows need to be gathered. So, in these cases, you win the lottery with your new index."
,"Query:Select fname from personal_info where marital_status='true'; No index should be created INDEX(flag) is almost never useful if flag has very few values. More specifically, when you say WHERE flag = 1 and '1' occurs more than 20 percentage of the time, such an index will be shunned. The Optimizer would prefer to scan the table instead of bouncing back and forth between the index and the data for more than 20 percentage of the rows."
,"Query:Select lname from personal_info where marital_status='false' and fname='Alex'; Index on flag,fname can be created. That would call for a composite (compound) index starting with a flag: INDEX(flag, fname). Such an index is likely to be very beneficial. And it is likely to be more beneficial than INDEX(fname). In this case, the flag is marital_status."
,"Query: Select * from personal_info where marital_status='false' and ctime>'2020-01-01' and fname='Alex' limit 5000; Index on marital_status,fname,ctime makes the query faster."
,"A) select fname,lname from personal_info where age IN (38,40); Still it takes much time to process if there is no  index on age column B) There is an index on age column then the above query performs more efficiently"
,"Unoptimised answer: select distinct(fname) from personal_info where age=38 or lname='Taylor'; Optimised answer: Select fname from personal_info where age=38 Union distinct Select fname from personal_info where lname='Taylor'; It is better to have indexes on age,lname columns separately for better performance"
,"Query:select * from contact_details where sno=9999975  and  phone_number='(726) 238-9825' and email='pij@darefhaf.lb'; Index on sno,phone_number and email must be created A covering index is an index that contains all the columns in the SELECT."
,"Query:Select * from personal_info where fname like 'Al%' and lname='Taylor'Index on (lname(6),fname(2)) can be created.You cannot directly index a TEXT or BLOB or large VARCHAR or large BINARY column.However,in this example fname column is small so (lname,fname) can also be used.Just used (lname(6),,fname(2)) to demonstrate this type."
,"Query: select street from address where ctime>'2020-01-01' and state='MO'; Create a compound index on state and ctime columns."
,"Unoptimised query: Select fname,city from personal_info,address where personal_info.sno=address.sno and fname='Alice'; Optimised: Create Index on fname in personal_info and index on Sno in address table Don't do comma join it was old syntax(It doesn't makes much difference) Query: Select fname,city from personal_info join address on personal_info.sno=address.sno where fname='Alice';"
,"Query: Select fname,city,email from personal_info join address on personal_info.sno=address.sno join contact_details on address.sno=contact_details.sno where lname='Taylor'; Creating index on lname, on sno of address table and on column sno of contact_details table will increase query performance."
,"Unoptimized solution: Select fname from personal_info where fname like 'T%' and sno in (select sno from address where street like 'A%'); Optimised solution: It can be transformed into a JOIN and Create index on sno in address table, which works much faster. One solution: Select fname from personal_info join address using(sno) where fname like 'T%' and street like 'A%'; Second solution: This solution will be useful only when there is an order by or group by in the inner subquery of unoptimized solution Select fname from personal_info join (select sno from address where street like 'A%') b using (sno) where fname like 'T%';"
,"Unoptimized solution: Select fname from personal_info where fname like 'A%' and sno in (select sno from address where street like 'V%' order by state);Optimised solution:Select fname from personal_info join (select * from address where street like 'V%' order by state)b using(sno) where fname like 'A%'; Combined Index on columns street,state will increase query performance"
,"Unoptimised solution: Select * from personal_info where fname='Alice' or lname='Parker'; Optimised solution: Create fulltext on fname and name so that it would be easy to search in both columns ALTER TABLE personal_info ADD FULLTEXT(fname,lname); Select * from personal_info where MATCH(fname,lname) AGAINST('alice parker'); In against you can add whatever name you want to search in both fname and lname separated by   space"
]

#Dictionary of indexes for each query
index_columns={
0:['iage'],
1:['iagegender'],
2:[],
3:['iage'],
4:['iage'],
5:['ilname'],
6:[],
7:['igenderfname'],
8:['ilnamefname'],
9:['ifnamelname'],
10:['iage'],
11:['ifname'],
12:['ifnamelnameage'],
13:['ifnamelname'],
14:['ifnamelname'],
15:['ifnamelnameage'],
16:['ifnameage'],
17:[],
18:['imarital_statusfname'],
19:['imarital_statusfnamectime'],
20:['iage'],
21:['iage','ilname'],
22:['isnophone_numberemail'],
23:['ilnamefname'],
24:['istatectime'],
25:['ifname','isno'],
26:['ilname','isno','isno'],
27:['isno'],
28:['istreetstate'],
29:['fnamelname']
}

#Dictionary of show index query for each query
index_queries={
  0:['show index from personal_info;'],
  1:['show index from personal_info;'],
  2:[],
  3:['show index from personal_info;'],
  4:['show index from personal_info;'],
  5:['show index from personal_info;'],
  6:[],
  7:['show index from personal_info;'],
  8:['show index from personal_info;'],
  9:['show index from personal_info;'],
  10:['show index from personal_info;'],
  11:['show index from personal_info;'],
  12:['show index from personal_info;'],
  13:['show index from personal_info;'],
  14:['show index from personal_info;'],
  15:['show index from personal_info;'],
  16:['show index from personal_info;'],
  17:[],
  18:['show index from personal_info;'],
  19:['show index from personal_info;'],
  20:['show index from personal_info;'],
  21:['show index from personal_info;','show index from personal_info;'],
  22:['show index from contact_details;'],
  23:['show index from personal_info;'],
  24:['show index from address;'],
  25:['show index from personal_info;','show index from address;'],
  26:['show index from personal_info;','show index from address;','show index from contact_details;'],
  27:['show index from personal_info;'],
  28:['show index from address;'],
  29:['show index from personal_info;']
}

#Dictionary of schemas for each query
schema={
  0:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  1:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  2:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  3:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  4:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  5:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  6:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  7:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  8:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  9:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  10:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  11:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  12:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  13:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  14:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  15:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  16:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  17:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  18:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  19:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  20:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  21:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  22:['contact_details(INT sno, TEXT email, TEXT phone_number, TIMESTAMP ctime, TIMESTAMP mtime)'],
  23:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  24:['address(INT sno, TEXT street, TEXT city, TEXT state, TEXT zip, TIMESTAMP ctime, TIMESTAMP mtime)'],
  25:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime) || ','address(INT sno, TEXT street, TEXT city, TEXT state, TEXT zip, TIMESTAMP ctime, TIMESTAMP mtime)'],
  26:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime) || ','address(INT sno, TEXT street, TEXT city, TEXT state, TEXT zip, TIMESTAMP ctime, TIMESTAMP mtime) || ','contact_details(INT sno, TEXT email, TEXT phone_number, TIMESTAMP ctime, TIMESTAMP mtime)'],
  27:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)'],
  28:['address(INT sno, TEXT street, TEXT city, TEXT state, TEXT zip, TIMESTAMP ctime, TIMESTAMP mtime)'],
  29:['personal_info(INT sno, TEXT fname, TEXT lname, INT age, CHAR(2) gender, TEXT marital_status,TIMESTAMP ctime, TIMESTAMP mtime)']
}

Already_solved=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #To keep track of solved questions

Opened_hints=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #To keep track of opened hints question and output answer question

Attempted=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #To keep track of completed questions

Final_score=0 #Variable which contains the score of the user

#Function to get the score
def getscore():
    return Final_score

#Function to update the score
def update_score(page_number):
    global Final_score
    if Opened_hints[page_number-1]==0:
        Final_score=Final_score+2
    elif Opened_hints[page_number-1]==1:
        Final_score=Final_score+1
    
