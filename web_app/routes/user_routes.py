
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from web_app.routes.wrappers import authenticated_route

user_routes = Blueprint("user_routes", __name__)

#
# USER ORDERS
#

@user_routes.route("/user/orders")
@authenticated_route
def orders():
    print("USER ORDERS...")
    current_user = session.get("current_user")
    service = current_app.config["FIREBASE_SERVICE"]
    orders = service.fetch_user_orders(current_user["email"])
    return render_template("user_orders.html", orders=orders)


@user_routes.route("/user/orders/create", methods=["POST"])
@authenticated_route
def create_order():
    print("CREATE USER ORDER...")

    form_data = dict(request.form)
    print("FORM DATA:", form_data)
    product_info = {
        "id": form_data["product_id"],
        "name": form_data["product_name"],
        "description": form_data["product_description"],
        "price": form_data["product_price"],
        "url": form_data["product_url"],
    }

    current_user = session.get("current_user")

    service = current_app.config["FIREBASE_SERVICE"]

    try:
        service.create_order(user_email=current_user["email"], product_info=product_info)
        flash(f"Order received!", "success")
        return redirect("/user/orders")
    except Exception as err:
        print(err)
        flash(f"Oops, something went wrong: {err}", "warning")
        return redirect("/products")


#
# USER PROFILE
#

@user_routes.route("/user/profile")
@authenticated_route
def profile():
    print("USER PROFILE...")
    current_user = session.get("current_user")
    #user = fetch_user(email=current_user["email"])
    return render_template("user_profile.html", user=current_user) # user=user
