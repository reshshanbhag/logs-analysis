#!/usr/bin/env python3

from datetime import datetime
import psycopg2
import pprint
import time

# Define our connection string
conn_string = "dbname='news'"

# get a connection
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object,
# you can use the cursor to perform queries
cursor = conn.cursor()

# perform the queries
cursor.execute("""select articles.title, num from articles, path_count
                  where path_count.path = concat('/article/',articles.slug)
                  order by num desc limit 3;""")
print ("1. The top three Articles of all time are\n")

# retrieve the records from the database for first problem
row_count = 0
for row in cursor:
    row_count += 1
    print ("\"%s\" --- %s views\n" % (row))

# perform the queries for second problem
cursor.execute("""select name, sum(num) as total from author_name, path_count
                  where path_count.path = concat('/article/',author_name.slug)
                  group by author_name.name order by total desc limit 3;""")

print ("2. The top three Authors of all time are\n")

# retrieve the records from the database for second problem
row_count = 0
for row in cursor:
    row_count += 1
    print ("\"%s\" --- %s views\n" % (row))


# Create a view for third problem -
# Days where more than 1% of requests lead to errors
# First step is create a view which has the count of errors(http status=404)
# and total statuses grouped by date

# Run a query against the above view
cursor.execute("""select date, round((100.0 * errors) / count) as percentage from
                  httpTemp where (100.0 * errors / count) > 1.0;""")
record = cursor.fetchall()
print ("3. The dates with more than 1% of requests that lead to errors\n")

# retrieve the records
for row in record:
    print ('{:%B %d, %Y} -- {:f}% errors'.format(row[0], row[1]))
    # close the connection
conn.close()
