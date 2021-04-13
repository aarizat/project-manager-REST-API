-- create database and user --
CREATE DATABASE IF NOT EXISTS projects_db;
CREATE user IF NOT EXISTS 'user_db'@'localhost' identified BY 'pwd_db';
GRANT usage ON *.* TO 'user_db'@'localhost';
GRANT all privileges ON projects_db.* TO 'user_db'@'localhost';
