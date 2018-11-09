from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='freedom',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

blueprint = Blueprint(
    'ui_blueprint',
    __name__,
    url_prefix='/ui',
    template_folder='templates',
    static_folder='static'
)
@blueprint.route('/general_elements', methods=['POST'])
def Conf():
   if request.method=='POST':
     status=request.form['options']
     Station=request.form['Station']
     try:
      with connection.cursor() as cursor:
        sql =  "UPDATE notifications SET `Status`=%s  WHERE `Station`=%s"  
        cursor.execute(sql,[status,Station])
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

