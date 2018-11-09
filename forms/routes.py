from flask import Blueprint, render_template
from flask import Flask, render_template, request
from flask_login import login_required
import pymysql.cursors
import sys

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='freedom',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


blueprint = Blueprint(
    'forms_blueprint',
    __name__,
    url_prefix='/forms',
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')

def subscribers():
    subscriber = "Select * from notifications"
    try:
        cursor = connection.cursor()
        cursor.execute(subscriber)
        print ("cursor.description: ", cursor.description)
        for row in cursor:
            print (" ----------- ")
            print("Row: ", row)
            print ("Status: ", row["Name"])
            
    finally:
        # Close connection.
        connection.close()
    return render_template('/form.html', subscribers=subscriber)
