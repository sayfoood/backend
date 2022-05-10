from flask import render_template,Blueprint,request
from operations import studOps
from methods import *

student = Blueprint("student", __name__, static_folder="static",template_folder="template")

@student.route("/")
def home():
  return "hi stud"

@student.route("/<roll>")
def detail(roll):
  details = stud.stu_det(roll)
  return details.to_json()


@student.route("/<roll>/order/",methods=["get","post"])
def order(roll):
  orders = ['A1','A2','B1','B2']
  ans = takeorder(orders,roll)
  return jsonify(str(ans))
  


@student.route("/<roll>/complain",methods=["post"])
def complain(roll):
  # reg_no = request.form['reg_no']
  # complaint = request.form['complaint']
  reg_no = 1234
  complaint = "not good 123 FGDF"
  stud.complain(reg_no,complaint)
  return "complain done"

     