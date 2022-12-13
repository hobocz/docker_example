import mysql.connector
from flask import Flask, render_template
app = Flask(__name__)

# This will be updated with the "keyring" library
mysql_pwd = 'p@ssw0rd1'

def init_db():
    mydb = mysql.connector.connect(
        host = 'mysqldb',
        user = 'root',
        password = mysql_pwd
    )
    cursor = mydb.cursor()
    cursor.execute('DROP DATABASE IF EXISTS testDB')
    cursor.execute('CREATE DATABASE testDB')
    cursor.close()

    mydb = mysql.connector.connect(
        host = 'mysqldb',
        user = 'root',
        password = mysql_pwd,
        database = 'testDB'
    )
    cursor = mydb.cursor()
    cursor.execute('DROP TABLE IF EXISTS items')
    cursor.execute('CREATE TABLE items (sentence VARCHAR(255))')
    cursor.execute('INSERT INTO items (sentence) VALUES ("Picture yourself on a boat on a river")')
    cursor.execute('INSERT INTO items (sentence) VALUES ("with tangerine trees and marmalade skies.")')
    cursor.execute('INSERT INTO items (sentence) VALUES ("Somebody calls you, you answer quite slowly")')
    cursor.execute('INSERT INTO items (sentence) VALUES ("a girl with kaleidoscope eyes.")')
    mydb.commit()
    cursor.close()

@app.route('/')
def home():
    init_db()

    mydb = mysql.connector.connect(
        host = "mysqldb",
        user = "root",
        password = mysql_pwd,
        database = "testDB"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM items")
    results = cursor.fetchall()
    cursor.close()
    return render_template('index.html', results = results)

if __name__ == '__main__':
    app.run(host ='0.0.0.0')