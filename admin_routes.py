from flask import render_template,Blueprint

admin = Blueprint("admin", __name__, static_folder="static",template_folder="template")

@admin.route("/")
def home():
  return "hi"

