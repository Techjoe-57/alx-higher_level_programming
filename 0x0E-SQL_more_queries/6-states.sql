-- create the database hbtn_0d_usa and the table states
-- table description: id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- if database and table already exists, scripts should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id),UNIQUE (id));
