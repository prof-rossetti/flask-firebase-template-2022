from flask import Blueprint, render_template, session

from app.firebase_service import fetch_products

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return render_template("about.html")

@home_routes.route("/products")
def products():
    products = fetch_products()
    return render_template("products.html", products=products)
