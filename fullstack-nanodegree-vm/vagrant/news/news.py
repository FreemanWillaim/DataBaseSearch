"""
!/usr/bin/env python3
"""





header1 = 'Title'  # A string variable to hold the title header.
header2 = 'Views'  # A string variable to hold the views header.
header3 = 'Author'  # A string variable to hold the author header.
header4 = 'Date'  # A string variable to hold the date header.

# A string variable to hold the precentage header.
header5 = 'Percentage of Errors'

sql1 = 'select a.title, count(*) as count from log join \
articles a on substring(path,10)=slug group by title \
order by count desc limit 3'