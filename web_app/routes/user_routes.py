
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
    #user = fetch_user(email=current_user["email"])
    #orders = fetch_orders(user_email=current_user["email"])
    orders = []
    return render_template("user_orders.html", orders=orders)

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


#@user_routes.route("/user/profile/edit")
#@authenticated_route
#def edit_profile():
#    print("EDIT PROFILE...")
#    current_user = session.get("current_user")
#    #user = fetch_user(email=current_user["email"])
#    return render_template("user_profile.html", user=current_user) # user=user

#@user_routes.route("/user/profile/update", methods=["POST"])
#@authenticated_route
#def update_profile():
#    #print("UPDATE PROFILE...")
#
#    form_data = dict(request.form)
#    print("FORM DATA:", form_data)
#    #full_name = form_data["full_name"]
#    first_name = form_data["first_name"]
#    last_name = form_data["last_name"]
#
#    current_user = session.get("current_user")
#    user = User.query.filter_by(email=current_user["email"]).first()
#    #user.full_name = full_name
#    user.first_name = first_name
#    user.last_name = last_name
#    db.session.add(user)
#    db.session.commit()
#
#    flash("Profile updated!", "success")
#    return render_template("user_profile.html", user=user)
#
