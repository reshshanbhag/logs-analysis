# Project - Logs Analysis
The project as part of the Udacity Full Stack Nanodegree involves building an internal reporting tool that will use information from a new database to discover what kind of articles the site's readers like.
This reporting tool is a Python program using the psycopg2 module to connect to the database. The report presents the below 3 in a text file.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
### Prerequisites
Python 2.x is required to execute this program
Download and install vagrant
### Installing
Download the project zip file locally to your computer and unzip in the directory with vagrant
Download the newsdata.sql database to the same directory.
CD into the vagrant directory and do "vagrant up" and "vagrant ssh". Then cd /vagrant and cd into the loganalysis directory
Execute the views
		Follow the below steps to setup the DB and execute the views
psql -d news -f newsdata.sql (load data into the DB)
psql -d news (connect to DB)
Then run the python file loganalysisdb.py to view the results
### Executing Views for the SQL queries
Problem 1: What are the most popular three articles of all time?
create view path_count as select path, count(*) as num from log where path != '/' group by path order by num desc limit 3;
Problem 2: Who are the most popular article authors of all time?
create view author_name as  select name, title, slug from articles, authors where articles.author=authors.id;
create view path_count as select path, count(*) as num from log where path != '/' group by path order by num desc;
Problem 3: On which days did more than 1% of requests lead to errors?
create view httpTemp as select date(time) as date, count(status) filter (where status='404 NOT FOUND') as errors, count(status) from log group by date(time);
## Authors
* **Reshma Shanbhag** (https://github.com/reshshanbhag)
## Acknowledgments
* Udacity README course
* Initial Readme template https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
