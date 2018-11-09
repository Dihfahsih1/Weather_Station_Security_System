from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='freedom',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def my_form():
    return render_template("index2.html")

@app.route('/', methods=['POST'])

def saveContent():
    if request.method=='POST':
     Name=request.form['Name']
     Email=request.form['Email']
     Station=request.form['Station']
     Phone=request.form['Phone']
     try:
  

      with connection.cursor() as cursor:
        sql =  "Insert into notifications (Name,Email,Station,Phone) " \
         + " values (%s, %s) "  
        cursor.execute(sql, (Name,Email,Station,Phone ) )
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"
    

if __name__ == '__main__':
    app.run()

