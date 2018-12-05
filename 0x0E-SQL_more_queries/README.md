# SQL - More queries
#### What I should learn:
- How to create a new MySQL user'- How to manage privileges for a user to a databaseor table
- What is a proxy
- What is a PRIMARY KEY
- What is a FOREIGN KEY
- How to use NOT NULL and UNIQUW constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

Import SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

### Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files are executed on Ubuntu 14.04 LTS using `MySQL 5.7`
- All SQL keywords are in uppercase

---
File | Description
0-privileges.sql | Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server.
1-create\_user.sql | Script that create the MySQL server user `user_0d_1`.
2-create\_read\_user.sql | Script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
3-force\_name.sql | Script that creates the table `force_name` on the MySQL server.
4-never\_empty.sql | Script that create the table `id_not_null` on the MySQL server.
5-unique\_id.sql | Script that creates the table `unique_id` on the MySQL server.
6-states.sql | Script that creates the database `hbtn_0d_usa` and the table `states` on the MySQL server.
7-cities.sql | Script that creates the database `hbtn_0d_usa` and the table `cities` on the MySQL server.
8-cities\_of\_california\_subquery.sql | Script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
9-cities\_by\_state\_join.sql | Script that lists all cities contained in the database `hbtn_0d_usa`.
10-genre\_id\_by\_show.sql | Script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked
11-genre\_id\_all\_shows.sql | Script that lists all shows contained in the database `hbtn_0d_tvshows`.
12-no\_genre.sql | Script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
13-count\_shows\_by\_genre.sql | Script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
14-my\_genres.sql | Script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
15-comedy\_only.sql | Script that lists all Comedy shows in the database `hbtn_0d_tvshows`.
16-shows\_by\_genre.sql | Script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
