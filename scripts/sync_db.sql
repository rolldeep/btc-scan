create database syncdb;

CREATE TABLE IF NOT EXISTS syncdb.currency (
  id SERIAL PRIMARY KEY,
  date TIMESTAMP, 
  pair varchar(200) NOT NULL,
  rates DECIMAL(20,3) NOT NULL
);