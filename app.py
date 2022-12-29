from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'RyanProject'
app.config['MYSQL_PASSWORD'] = 'Password!321'
app.config['MYSQL_DB'] = 'mydata'
 
mysql = MySQL(app)

#Creating a connection cursor
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' INSERT INTO friends VALUES (4, 'Ryan', 20, 'm') ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the cursor
cursor.close()