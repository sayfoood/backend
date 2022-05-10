from sqlite3 import OperationalError
from traceback import print_tb
from flask import  Flask,render_template,request,jsonify
from methods import df_to_json
from operations import *
from methods import mess , stud
from admin_routes import admin
from student_routes import student

app = Flask(__name__)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(student,url_prefix="/student")

@app.route("/")
def root():
  db = MessOps()
  db = db.disp_db()
  return df_to_json(db)

@app.route("/menu")
def menu():
  res = stud.view_menu_db()
  return df_to_json(res)