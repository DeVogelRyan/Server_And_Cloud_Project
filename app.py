from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydata'

mysql = MySQL(app)

with app.app_context():
#Creating a connection cursor
    cursor = mysql.connection.cursor()

    #Executing SQL Statements
    cursor.execute('''  CREATE TABLE friends (id INT, name VARCHAR(256), age INT, gender VARCHAR(3)); ''')
    cursor.execute('''  INSERT INTO friends VALUES (1, 'Abhijeet', 32, 'm'); ''')

    #Saving the Actions performed on the DB
    mysql.connection.commit()

    #Closing the cursor
    cursor.close()