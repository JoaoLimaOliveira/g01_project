from flask import Flask, render_template, request, session
from classes.student import Student
from datafile import filename
from classes.course import Course
from classes.department import Department
from classes.course_student import Course_Student
from classes.userlogin import Userlogin
from subs.apps_course import apps_Course
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)
Department.read(filename + 'business.db')
Course.read(filename + 'business.db')
Student.read(filename + 'business.db')
Course_Student.read(filename + 'business.db')
Userlogin.read(filename + 'business.db')
app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()  