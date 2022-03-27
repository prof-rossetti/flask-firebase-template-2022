
from flask import session, flash, redirect, current_app
from flask import Blueprint, session, redirect, url_for #request, render_template, , jsonify

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/login")
def login():
    print("LOGIN...")
    oauth = current_app.config["OAUTH"]
    redirect_uri = url_for("auth_routes.google_oauth_callback", _external=True) # see corresponding route below
    return oauth.google.authorize_redirect(redirect_uri) # send the user to login with google, then hit the callback route

@auth_routes.route("/auth/google/callback")
def google_oauth_callback():
    print("GOOGLE OAUTH CALLBACK...")
    oauth = current_app.config["OAUTH"]
    token = oauth.google.authorize_access_token()
    user_info = token.get("userinfo")
    if user_info:
        print("STORING USER INFO IN THE SESSION...")
        print(user_info)
        session["current_user"] = user_info # add user info to the session
    else:
        print("NO USER INFO")
    return redirect("/")

@auth_routes.route("/logout")
def logout():
    print("LOGGING OUT...")
    session.pop("current_user", None) # remove user info from the session
    return redirect("/")
