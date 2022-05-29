from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/home")
def home():
    return render_template("index.html")

@views.route("/creator")
def creator():
    return render_template("creator.html")

@views.route("/information")
def information():
    return render_template("information.html")

@views.route("/learn")
def learn():
    return render_template("learn.html")