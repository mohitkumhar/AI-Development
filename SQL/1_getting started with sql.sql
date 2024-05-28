-- what is a database?
-- A collection of data and holds this data in the form of tables

-- what is a table?
-- holds the data in form of rows and columns.

-- It is similar to excel spreadsheet

-- The database provides us the capability to access and manipulate this data.


-- Two types of Databases
-- ===========================
-- 1. Relational Database- rows and columns and also the tables have relation between them.
--               MySQL
--               SQL Server
--               PostgreSQL
--               SQLite
--               MariaDB     

-- 2. NOSQL Databse- Key Value, Document, Graph
--               Hbase
--               MongoDB
--               cassandra


-- SQL - Structured Query Language

-- MySQL vs SQL

-- SQL - Query

SHOW DATABASES;  -- show the list of database
CREATE DATABASE database_name; -- to create database
DROP DATABASE database_name; -- to delete database
USE database_name; -- to appply any operation on any database
SELECT DATABASE(); -- to check in which database we currently are
SHOW TABLES; -- it will shows the list of tables 

CREATE TABLE table_name  -- to create table
(
    -- column1_name datatype(max_limit of data can be stored),
    -- column2_name datatype(No max limit for INT)
);

simple DATA_TYPE
			INT for numeric
			varchar for string 


DESCRIBE table_name;  -- it will descripe the table completely
DESC table_name; -- it will shows the same result

DROP TABLE table_name; -- this will delete the table 

CREATE TABLE table_name.database_name  -- this will create table without selecting database
(
    -- column1_name datatype(max_limit of data can be stored),
    -- column2_name datatype(No max limit for INT)
)



