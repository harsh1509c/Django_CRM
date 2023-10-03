# Install MYSQL on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'harsh1509',
)

# prepare cursor object
cursorObj = dataBase.cursor()

# create database
cursorObj.execute("CREATE DATABASE CRM_DB")

print("Successful!!")