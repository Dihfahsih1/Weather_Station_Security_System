from flask import Flask
from flask import Blueprint, render_template,request,url_for,redirect
from flask_login import login_required
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='freedom',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='/home',
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html')

@blueprint.route('/index2', methods=['POST'])
def register():
    if request.method=='POST':
     Name=request.form['Name']
     Email=request.form['Email']
     Phone=request.form['Phone']
     Station=request.form['Station']
     try:
      with connection.cursor() as cursor:
        sql =  "Insert into notifications (Name,Email,Phone,Station) " \
         + " values (%s, %s, %s, %s) "  
        cursor.execute(sql, (Name, Email,Phone,Station ) )
        connection.commit()
     finally:
    #   connection.close()
      print ("Saved successfully.")
      return redirect(url_for('home_blueprint.index'))
      
    else:
      return "error"  

@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
       
