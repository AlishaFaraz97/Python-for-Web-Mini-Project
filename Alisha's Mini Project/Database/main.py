from flask import Flask, render_template, request
from urllib.request import urlopen
import mysql.connector

import json

app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="elicia938", database="fypgroups")

@app.route("/fyp")
def fyp():
mycursor = mydb.cursor()
mycursor.execute("select * from student_groups")
result = mycursor.fetchall()
return str(student_groups)

@app.route("/", methods=['GET'])
def alisha():


    url = "https://cms.mlcs.xyz/api/view/program_sessions/all/"

    response = urlopen(url)

    data_json = json.loads(response.read())

    cs_session = []
    for a in data_json:
        cs_session.append(a['Session_Title'])
    print (cs_session)
    return render_template("alisha.html", cs_session=cs_session)

@app.route("/login",  methods=['POST'])
def login():
   if request.method=='POST':
    uname = request.form.get("uname")
    password = request.form.get("password")
    print(uname, password)
    #db.execute("INSERT into login(user_name, password) VALUES (:user_name, :password)", {"user_name": uname, "password":password})
    #db.commit()
    return render_template("login.html" , login=login)
   else:
       return render_template("login.html", login=login)
@app.route("/staff",  methods=['POST'])
def staff():
    url = "https://cms.mlcs.xyz/api/view/teaching_staff/all/"

    response = urlopen(url)

    data_json = json.loads(response.read())

    teacher_name = []
    for b in data_json:
        teacher_name.append(b['teacher_name'])
    print(teacher_name)

    gname = request.form.get("gname")
    project_title= request.form.get("project_title")
    supervisor=request.form.get("supervisor")
    psw= request.form.get("psw")
   # db.execute("INSERT into project(group_leader_name, project_title, supervisor, members) VALUES (:group_leader_name, :project_title, :supervisor, :psw)",
    #     {"group_leader_name" : gname, "project_title" : project_title, "supervisor" :supervisor, "psw":psw})
    #db.commit()
    return render_template("staff.html" , teacher_name=teacher_name, gname=gname, project_title=project_title, supervisor=supervisor,psw=psw)
@app.route("/group",  methods=['POST'])
def group():
    url = "https://cms.mlcs.xyz/api/view/students_of/BSIT-2016/all/"

    response = urlopen(url)

    data_json = json.loads(response.read())

    student_name = []
    for s in data_json:
        student_name.append(s['student_name'])
    print(student_name)
    return render_template("group.html", student_name=student_name)
@app.route("/final" , methods=['GET', 'POST'])
def final():

    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)
