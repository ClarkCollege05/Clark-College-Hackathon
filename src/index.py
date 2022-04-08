import MySQLdb
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'CCST'

mysql = MySQL(app)

@app.route("/IndeX",  methods = ['GET',"POST"])
def index():

                 
    if request.method == 'POST':
        usernames = request.form
        name = usernames['firstName']
        cur = mysql.connection.cursor()
        lastname = usernames['lastName']
        position = request.form['position']
        credits = '0'
        hourly= '0'
        VacationL = '0'
        cur.execute("INSERT INTO employee(firstname, lastname,position,SickLeaveCredits,VacationLeave,hourlyRate) VALUES(%s, %s,%s, %s, %s,%s)",(name,lastname,position,credits,VacationL,hourly))
        mysql.connection.commit()
        cur.close()
        TY = 'Registered Successfully!'
        return render_template('index.html',TY=TY)
    return render_template('index.html')


@app.route("/employee_list",  methods = ['GET',"POST"])
def list_empl():

    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM employee")


    if results > 0:
        result = cur.fetchall()
        TEXT = 'EMPLOYEE LIST' 
        if request.method == 'POST':
            VacationC = request.form["VacationCredits"] 
            SickC = request.form['SickCredits']   

            Hrate = request.form['HourlyRate']
            IDs = request.form['IDs']
            curs = mysql.connection.cursor()
                    


            curs.execute("UPDATE employee set SickLeaveCredits = %s where id = %s",(SickC,IDs))
            mysql.connection.commit()
            curs.execute("UPDATE employee set hourlyRate = %s where id = %s",(Hrate,IDs))

            mysql.connection.commit()

            curs.execute("UPDATE employee set VacationLeave  = %s where id = %s",(VacationC,IDs))
            mysql.connection.commit()

            curs.close()
            return redirect('/employee_list')
            
        return render_template('employee_list.html',TEXT=TEXT,result=result)
    else:
        TEXT = 'EMPTY'
        return render_template('employee_list.html',TEXT=TEXT)
        
    return render_template('employee_list.html',TEXT=TEXT,result=result)


@app.route("/delete_admin",  methods = ['GET',"POST"])
def Delete_ADMIN():

    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM admin")


    if results > 0:
        result = cur.fetchall()
        TEXT = 'DELETE ADMIN' 
        if request.method == 'POST':


            IDs = request.form["IDs"]    
            curs = mysql.connection.cursor()
            curs.execute("DELETE FROM admin WHERE id = '"+IDs+"'")
            mysql.connection.commit()
            curs.close()


            return redirect('/delete_admin')


            
        return render_template('delete_admin.html',TEXT=TEXT,result=result)
    else:
        TEXT = 'EMPTY'
        return render_template('delete_admin.html',TEXT=TEXT)
        
    return render_template('delete_admin.html',TEXT=TEXT,result=result)


    
@app.route("/delete_employee",  methods = ['GET',"POST"])
def Delete_empl():

    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM employee")


    if results > 0:
        result = cur.fetchall()
        TEXT = 'DELETE EMPLOYEE' 
        if request.method == 'POST':


            IDs = request.form["IDs"]    
            curs = mysql.connection.cursor()
            curs.execute("DELETE FROM employee WHERE id = '"+IDs+"'")
            mysql.connection.commit()
            curs.close()        

            
        return render_template('delete_employee.html',TEXT=TEXT,result=result)
    else:
        TEXT = 'EMPTY'
        return render_template('delete_employee.html',TEXT=TEXT)
        
    return render_template('delete_employee.html',TEXT=TEXT,result=result)


    

@app.route("/",  methods = ['GET',"POST"])
def Landing():
    return render_template("landing.html")



@app.route("/ADMIN_list",  methods = ['GET',"POST"])
def list_ADD():

    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM admin")


    if results > 0:
        result = cur.fetchall()
        TEXT = "ADMIN LIST"
        return render_template('admins_list.html',result=result,TEXT=TEXT)
    else:
        resultt = "empty"
        TEXT = "EMPTY"
        return render_template('admins_list.html',resultt=resultt,TEXT=TEXT)


@app.route("/AdminMain", methods = ['GET',"POST"])
def loginADMINN():
    
    if request.method == 'POST':
        username = request.form["email"]
        Password = request.form["password"]

              
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Mainadmin WHERE email =  '"+username+"'")
  
        result = cur.fetchone()
        
        
    
        if result:
            OrigPass = result['password']
            if Password != OrigPass:
                NotFound = "Wrong Password!"
                return render_template('MainAdmin.html',NotFound=NotFound)

            return redirect('/ADMIN_list')
        else:
            NotFound = "Email not found!"
            return render_template('MainAdmin.html',NotFound=NotFound)

    return render_template('MainAdmin.html')

@app.route("/AddAddmin", methods = ['GET',"POST"])
def ADdmin():

    if request.method == 'POST':
        usernames = request.form
        name = usernames['firstName']
        cur = mysql.connection.cursor()
        lastname = usernames['lastName']
        email = request.form['email']
        password = request.form['password']
        clearance = request.form['clearance']

        cur.execute("INSERT INTO admin(firstname, lastname,email,password,clearance) VALUES(%s, %s,%s, %s, %s)",(name,lastname,email,password,clearance))
        mysql.connection.commit()
        cur.close()
        return redirect('/ADMIN_list')
    return render_template('ADDadmin.html')








@app.route("/LogIn_admin", methods = ['GET',"POST"])
def loginADMIN():
    
    if request.method == 'POST':
        username = request.form["email"]
        Password = request.form["password"]

              
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM admin WHERE email =  '"+username+"'")
  
        result = cur.fetchone()
        
        
    
        if result:
            OrigPass = result['password']
            if Password != OrigPass:
                NotFound = "Wrong Password!"
                return render_template('Admin_login.html',NotFound=NotFound)

            return redirect('/employee_list')
        else:
            NotFound = "Email not found!"
            return render_template('Admin_login.html',NotFound=NotFound)

    return render_template('Admin_login.html')

if __name__ == '__main__':
    app.run(debug=True)