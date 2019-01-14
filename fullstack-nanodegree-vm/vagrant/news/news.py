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