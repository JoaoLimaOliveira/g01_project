from flask import Flask, render_template, request, session
from classes.course import Course

prev_option = ""

def apps_Course():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow, butedit = "disabled", "enabled"
        elif option == "delete":
            obj = Course.current()
            Course.remove(obj.id)
            if not Course.previous():
                Course.first()
        elif option == "insert":
            butshow, butedit = "disabled", "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            strobj = str(Course.get_id(0))
            strobj = strobj + ';' + request.form["course_name"] + ';' + \
            request.form["credits"] + ';' + request.form["departments_id"]
            obj = Course.from_string(strobj)
            Course.insert(obj.id)
            Course.last()
        elif prev_option == 'edit' and option == 'save':
            obj = Course.current()
            obj.course_course_namee = request.form["course_name"]
            obj.credits = request.form["credits"]
            obj.departments_id = float(request.form["departments_id"])
            Course.update(obj.id)
        elif option == "first":
            Course.first()
        elif option == "previous":
            Course.previous()
        elif option == "next":
            Course.nextrec()
        elif option == "last":
            Course.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Course.current()
        if option == 'insert' or len(Course.lst) == 0:
            id = 0
            id = Course.get_id(id)
            course_name = credits = departments_id = ""
        else:
            id = obj.id
            course_name = obj.course_name
            credits = obj.credits
            departments_id = obj.departments_id
        return render_template("Course.html", butshow=butshow, butedit=butedit, 
                        id=id,course_name = course_name,credits=credits,departments_id=departments_id, 
                        ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

