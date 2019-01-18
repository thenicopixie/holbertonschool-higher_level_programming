# 0x0F. Python - Object-relational mapping
#### What I should learn:
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

Install `MySQLdb` module version `1.3.x`

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.12'
```

Install `SQLAlchemy module verion `1.2.x`

```
$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
```

---
File | Description
-----|------------
0-select_states.py | Script that lists all `states` from the database `hbtn_0e_0_usa`
1-filter_states.py | Script that lists all `states` with a `name` starting with `N` from the database
2-my_filter_states.py | Script that takes in an arguments and displays all values in the `states` tables of a database where `name` matches the argument
3-my_safe_filter_states.py | Script that takes in an argument and displays all values in the `states` tables of a database where `name` matches the argument. Written so that it is safe from MySQL injections
4-cities_by_state.py | Script that lists all `cities` from a database
5-filter_cities.py | Script that takes in the name of a state as an argument and lists all `cities` of the state, using a database
model_state.py | A python file that contains the class definition of a `State` and an instance `Base = declarative_base()`
7-model_state_fetch_all.py | Script that lists all `State` objects from a database
8-model_state_fetch_first.py | Script that prints the first `State` object from a database
9-model_state_filter_a.py | Script that lists all `State` objects that contain the letter `a` from a database
10-model_state_my_get.py | Script that prints the `State` object with the `name` passed as argument from a database.
11-model_state_insert.py | Script that adds the `State` objects "Louisiana" to a database
12-model_state_update_id_2.py | Script that changes the name of a `State` object from a database
13-model_state_delete_a.py | Script that deletes all `State` objects with a name containing the letter `a` from a database
model_city.py, 14-model_city_fetch_by_state.py | Python file that contains the class definition of a `City`
relationship_city.py, relationship_state.py, 100-relationship_states_cities.py | Improve files and rename them
101-relationship_states_cities_list.py | Script that lists all `State` objects, and corresponding `City` objects, contained in a database
102-relationship_cities_states_list.py | Script that lists all `City` objects from a database

#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan)
