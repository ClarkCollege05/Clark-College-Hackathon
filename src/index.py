import MySQLdb
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'CCST'

# mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('employee.html')

if __name__ == '__main__':
    app.run(debug=True)