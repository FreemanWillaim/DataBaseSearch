"""
!/usr/bin/env python3
"""





header1 = 'Title'  # A string variable to hold the title header.
header2 = 'Views'  # A string variable to hold the views header.
header3 = 'Author'  # A string variable to hold the author header.
header4 = 'Date'  # A string variable to hold the date header.

# A string variable to hold the precentage header.
header5 = 'Percentage of Errors'

# An sql query that selects title of each article in the database,
# and then counts the total number of of times this article is accesed
# in the log table. It# then joins the log table and extracts the path
# and compares this to the slug column in the articles tables.

sql1 = 'select a.title, count(*) as count from log join \
articles a on substring(path,10)=slug group by title \
order by count desc limit 3'

# An sql query the selects the name of the author from the log database.
# It then counts the total number of times an article written by each author
# is viewed.

sql2 = 'select au.name, count(*) from log join articles\
 a on substring(path,10)=slug join authors au on au.id \
 = a.author group by name order by count desc'

# Sql query's that selects the date from the log database. It then
# uses a case statement to count the numbeer of times a query recieved a 404
# error, and divides this by the total number of queries for each day.
# The query then multiplies the reult by 100 to show the percentage of errors
# for each day and rounds the reuslt to two decimal places.
 
 sql3 = 'select date(time) as date ,round(((SUM(CASE WHEN log.status=\
\'404 NOT FOUND\' THEN 1 ELSE 0 END))/((count(date(time)))::numeric)\
*100),2)as a from log group by date having round(((SUM(CASE WHEN \
log.status=\'404 NOT FOUND\' THEN 1 ELSE 0 END))/((count\
(date(time)))::numeric)*100),2) > 1;'

# Calls the fileOpen method to open the file NewsResults.txt for appending and
# creates an object.  Which is then stored in the variable file.

file = fileOpen()

# Calls the method connect to create a connection to the news database.
# Then this object is stored in the variable conn.

conn = connect()

# creates a cursor object to search the database.

curr = conn.cursor()

# Calls the searchData method and passes in a cursor, curr, an sql
# statement,  sql1, and two headers, header1 and header2. Then
# recieves the result of the query.

results = searchData(curr, sql1, header1, header2)

# Calls the method connect to create a connection to the news database.
# Then this object is stored in the variable conn.

file = fileOpen()

results = searchData(curr, sql2, header3, header2)