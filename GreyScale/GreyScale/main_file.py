import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import json
import pymysql

pymysql.install_as_MySQLdb()

with open("config.json", 'r') as c:
    config = json.load(c)
    URI = config["URI"]
local_server = URI['local_server']

app = Flask(__name__)
app.secret_key = "AAFTAB-alam"
app.config['UPLOAD_FOLDER'] = URI['upload_folder']

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = URI['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = URI['prod_uri']

db = SQLAlchemy(app)


class Emails(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=False)


class Projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=True)
    date = db.Column(db.String(12), nullable=False)
    uname = db.Column(db.String(50), nullable=True)


class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    uname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


session = {}


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect("/dashboard")
    if request.method == 'POST':
        username = request.form.get("uname")
        password = request.form.get("pass")
        users = Users.query.with_entities(Users.uname).all()
        popup = None
        for i in range(len(users)):
            if username in users[i]:
                user = Users.query.filter_by(uname=username).first()
                if password == user.password:
                    print(user.password)
                    session['user'] = username
                    return redirect("/dashboard")
                return render_template("login_page2.html", page=config["about"], layout=config["layout"],
                                       popup="wrongpass")
        return render_template("login_page2.html", page=config["about"], layout=config["layout"], popup="notfound")
    return render_template("login_page2.html", page=config["about"], layout=config["layout"])


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    print(session)
    if 'user' in session:
        posts = Projects.query.filter_by(uname=session['user']).all()
        return render_template("dashboard.html", page=config["about"], layout=config["layout"], posts=posts)

    return render_template("login_page2.html", page=config["about"], layout=config["layout"])


@app.route("/dashboard/edit-<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session:
        post = Projects.query.filter_by(sno=sno).first()
        if request.method == 'POST':
            file = request.files['file1']
            print(file)
            if file.filename == '':
                filename = post.img
            else:
                filename = secure_filename(file.filename)
                print("filename", filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            post.img = filename
            post.sno = sno
            post.heading = request.form.get("heading")
            post.description = request.form.get("description")
            post.date = datetime.now()
            db.session.commit()
            return redirect("/dashboard")
        return render_template("edit.html", page=config["contact"], layout=config["layout"], post=post)
    return redirect('/login')


@app.route("/dashboard/delete-<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if 'user' in session and session['user'] == "aadilkhan891316@gmail.com":
        post = Projects.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        qry = f"update projects set sno=sno-1 where sno > {sno};"
        db.engine.execute(qry)

        return redirect("/dashboard")
    return redirect("/login")


@app.route("/dashboard/upload", methods=['GET', 'POST'])
def upload():
    if 'user' in session:
        if request.method == 'POST':
            file = request.files['file1']
            img = None
            if file.filename == '':
                flash('No image selected for uploading')
                # return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                img = filename
            heading = request.form.get("heading")
            description = request.form.get("description")
            entry = Projects(heading=heading, description=description, img=img, date=datetime.now(),
                             uname=session['user'])
            db.session.add(entry)
            db.session.commit()
            last = db.engine.execute("select *from projects order by sno desc limit 1;")
            print(last)
            return redirect("/dashboard")
        return render_template("upload.html", page=config["contact"], layout=config["layout"])

    return render_template("login_page2.html", page=config["about"], layout=config["layout"])


@app.route("/signout")
def signout():
    session.popitem()
    return redirect('/dashboard')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get("email")
        if email:
            entry = Emails(email=email, date=datetime.now())
            db.session.add(entry)
            db.session.commit()
    return render_template("index.html", page=config["home"], layout=config["layout"])


@app.route("/about")
def about():
    return render_template("about.html", page=config["about"], layout=config["layout"])


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = Users.query.with_entities(Users.uname).all()
        name = request.form.get('name')
        uname = request.form.get('uname')
        password = request.form.get('pass')
        conpass = request.form.get('conpass')
        popup = None
        for i in range(len(users)):
            if uname in users[i]:
                popup = "userexist"
                return render_template("signup.html", page=config["about"], layout=config["layout"], popup=popup)
        if password != conpass:
            popup = "wrongpass"
            return render_template("signup.html", page=config["about"], layout=config["layout"], popup=popup)
        entry = Users(name=name, uname=uname, password=password)
        db.session.add(entry)
        db.session.commit()
        return "<html> <body> login successfull </body> </html>"
    return render_template("signup.html", page=config["about"], layout=config["layout"])


@app.route("/contact")
def contact():
    return render_template("contact.html", page=config["contact"], layout=config["layout"])


@app.route("/projects/<int:pg_number>")
def project(pg_number):
    posts = Projects.query.order_by(Projects.date.desc()).all()

    no_of_posts = config["projects"]["no_of_posts"]
    no_of_pages = len(posts) // no_of_posts
    print(no_of_pages)
    if pg_number == 0:
        posts = posts[0:no_of_posts]
    if 0 < pg_number < no_of_pages:
        posts = posts[pg_number * no_of_posts:no_of_posts + pg_number * no_of_posts]
        print(posts)
    if pg_number >= no_of_pages:
        posts = posts[pg_number * no_of_posts:len(posts)]
    users = []
    for i in range(len(posts)):
        user = Users.query.filter_by(uname=posts[i].uname).first()
        users.append(user.name)
    size = len(posts)
    return render_template("project.html", page=config["projects"], layout=config["layout"], posts=posts,
                           number=pg_number, no_of_pages=no_of_pages, size=size, users=users)


app.run(debug=True)
