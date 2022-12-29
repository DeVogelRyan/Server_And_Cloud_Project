from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydata'
 
mysql = MySQL(app)
with app.app_context():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
    
    #Executing SQL Statements
    cursor.execute(''' CREATE TABLE users (name VARCHAR(20) NOT NULL)''')
    cursor.execute(''' INSERT INTO users VALUES('ryan') ''')
    
    #Saving the Actions performed on the DB
    mysql.connection.commit()
    
    #Closing the cursor
    cursor.close()