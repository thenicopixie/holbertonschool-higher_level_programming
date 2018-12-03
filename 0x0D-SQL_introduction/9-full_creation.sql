-- Script that create a table second_table in the database hbtn_0c_0
-- in the MySQL server and adds multiples rows to it
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table
    (id, name, score)
VALUES
    (1, 'John', 10),
    (1, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

