from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/home")
def Home():
    return render_template("home.html", name= "joe")