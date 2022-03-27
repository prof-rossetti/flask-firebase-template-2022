
from flask import Blueprint, render_template, flash, redirect, current_app, url_for, session, request #, jsonify

from web_app.routes.wrappers import authenticated_route

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/user/orders")
@authenticated_route
def orders():
    print("USER ORDERS...")
    current_user = session.get("current_user")
    #user = fetch_user(email=current_user["email"])
    #orders = fetch_orders(user_email=current_user["email"])
    orders = []
    return render_template("user_orders.html", orders=orders)


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





@user_routes.route("/user/gyms")
@authenticated_route
def my_gyms():

    user_email = session["current_user"]["email"]

    # todo: single query! (with joins)
    user = User.query.filter_by(email=user_email).first()
    gyms = Gym.query.join(Membership).filter(Membership.user_id==user.id).all()

    #if any(gyms):
    #    return render_template("user_gyms.html", gyms=gyms)
    #else:
    #    flash("Oh, no gym memberships found. Please select a gym and provide an access code to continue.", "warning")
    #    return redirect("/gyms")
    return render_template("user_gyms.html", gyms=gyms)


@user_routes.route("/user/reservations")
@authenticated_route
def my_reservations():
    user_email = session["current_user"]["email"]

    user = User.query.filter_by(email=user_email).first()
    # TODO: single query maybe?
    reservations = user.upcoming_reservations()

    #if any(reservations):
    #    return render_template("user_reservations.html", user=user, reservations=reservations)
    #else:
    #    flash("Oh, no reservations found. Why don't you try making one?", "warning")
    #    return redirect("/user/gyms")


    return render_template("user_reservations.html", user=user, reservations=reservations, relative_weekday=relative_weekday)
