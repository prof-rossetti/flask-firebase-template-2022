
from flask import session, flash, redirect, current_app
from flask import Blueprint, session, redirect, url_for, render_template #request, , , jsonify

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/signup")
def signup():
    print("SIGNUP...")
    return render_template("signup.html")

@auth_routes.route("/login")
def login():
    print("LOGIN...")
    return render_template("login.html")

@auth_routes.route("/auth/google/login")
def google_login():
    print("GOOGLE OAUTH LOGIN...")
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
        #print(user_info)
        #> {
        #>     'iss': 'https://accounts.google.com',
        #>     'azp': '__________.apps.googleusercontent.com',
        #>     'aud': '__________.apps.googleusercontent.com',
        #>     'sub': '__________',
        #>     'email': 'example@gmail.com',
        #>     'email_verified': True,
        #>     'at_hash': '__________',
        #>     'nonce': '__________',
        #>     'name': 'First M Last',
        #>     'picture': 'https://lh3.googleusercontent.com/a-/__________',
        #>     'given_name': 'First M',
        #>     'family_name': 'Last',
        #>     'locale': 'en',
        #>     'iat': __________,
        #>     'exp': __________
        #> }
        print("USER INFO:", user_info["email"], user_info["name"], user_info["locale"])
        session["current_user"] = user_info # add user info to the session
    else:
        print("NO USER INFO")
    return redirect("/")

@auth_routes.route("/logout")
def logout():
    print("LOGGING OUT...")
    session.pop("current_user", None) # remove user info from the session
    return redirect("/")
