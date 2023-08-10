from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="flask"

mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "POST":
        name=request.form['name']
        subject=request.form['subject']
        email=request.form['email']
        message=request.form['message']
        cur_obj=mysql.connection.cursor()
        cur_obj.execute("INSERT INTO cv (name,subject,email,message) VALUES(%s,%s,%s,%s)",(name,subject,email,message))
        mysql.connection.commit()
        cur_obj.close()
        return "Data insert Successfully!!"
    return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
