from flask import Blueprint, render_template, session

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def homepage():
    user = session.get("user")
    return render_template("home.html", user=user)
