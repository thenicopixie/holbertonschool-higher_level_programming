# 0x0D SQL - Introduction
#### What I should learn:
- What is a database
- What is a relational database
- What does SQL stand for?
- What is MySQL?
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions



---
File | Description
-----|------------
0-list\_databases.sql | Script that lists all databases of the MySQL server
1-create\_database\_if\_missing.sql | Create a database with given name if it does not exist. Not allowed to use `SELECT` or `SHOW`.
2-remove\_database.sql | Script that deletes the given database from the MySQL if it exists. Now allowed to use the SELECT of SHOW statements.
3-list\_tables.sql | Script that lists all the tables of a database from the MySQL server.
4-first\_table.sql | Script that creates a table in the current database of the MySQL server.
5-full\_table.sql | Script that prints the full description of a given table from a given database in the MySQL server
6-list\_values.sql | Script that lists all rows of a given table from a given database in the MySQL server.
7-insert\_value.sql | Script that inserts a new row in the given table from a given database in the MySQL server.
8-count\_89.sql | Script that displays the number of records with given vales in the given table of the given database of the MySQL server.
9-full\_creation.sql | Script that creates a table in a database in the MySQL server and adds multiple rows.
10-top\_score.sql | Script that lists all records of a table of a database in the MySQL server
11-best\_score.sql | Script that lists all records with a score >= 10
12-no\_cheating.sql | Script that changed the score to 10 if the name is Bob
13-change\_class.sql | Script that removes all records with a score <= 5
14-average.sql | Script that computes the score average of all records in the table of the database
15-groups.sql | Script that lists the number of records with the same score in the table of the database
16-no\_link.sql | Script that lists all records of the talbe of the database
100-move\_to\_utf8.sql | Script that converts a database to UTF8 in a MySQL server
101-avg\_temperatures.sql | Import in a databse a table. Script that displays the average temperature by city ordered by temperature.
102-top\_city.sql | Import in a database a table dump. Script displays the top 3 cities temperatures during July and August ordered by temperature.
103-max\_state.sql | Import in a database a table dump. Script that displays the max temperature of each state.

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
