

import os
from dotenv import load_dotenv

from flask import Flask
from authlib.integrations.flask_client import OAuth

from app import APP_ENV, APP_VERSION
from app.firebase_service import FirebaseService

from web_app.routes.home_routes import home_routes
from web_app.routes.auth_routes import auth_routes
from web_app.routes.user_routes import user_routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # IMPORTANT: override in production

APP_TITLE = "My App"

# https://icons.getbootstrap.com/
NAV_ICON_CLASS = "bi-globe"

# https://getbootstrap.com/docs/5.1/components/navbar/#color-schemes
# https://getbootstrap.com/docs/5.1/customize/color/#theme-colors
NAV_COLOR_CLASS = "navbar-dark bg-primary"

# for google oauth login:
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# for google analytics (universal analytics):
GA_TRACKER_ID = os.getenv("GA_TRACKER_ID", default="G-OOPS")
#GA_DOMAIN = os.getenv("GA_DOMAIN", default="http://localhost:5000") # in production set to "________"


def create_app(firebase_service=None):

    if not firebase_service:
        firebase_service = FirebaseService()

    #
    # INIT
    #

    app = Flask(__name__)

    #
    # CONFIG
    #

    # for flask flash messaging:
    app.config["SECRET_KEY"] = SECRET_KEY

    # for front-end (maybe doesn't belong here but its ok):
    app.config["APP_ENV"] = APP_ENV
    app.config["APP_VERSION"] = APP_VERSION
    app.config["APP_TITLE"] = APP_TITLE
    app.config["NAV_ICON_CLASS"] = NAV_ICON_CLASS
    app.config["NAV_COLOR_CLASS"] = NAV_COLOR_CLASS

    # for client-side google analytics:
    app.config["GA_TRACKER_ID"] = GA_TRACKER_ID
    #app.config["GA_DOMAIN"] = GA_DOMAIN

    # set timezone to mimic production mode when running locally:
    os.environ["TZ"] = "UTC"

    #
    # AUTH
    #

    oauth = OAuth(app)
    oauth.register(
        name="google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        #authorize_params={"access_type": "offline"} # give us the refresh token! see: https://stackoverflow.com/questions/62293888/obtaining-and-storing-refresh-token-using-authlib-with-flask
    )
    app.config["OAUTH"] = oauth

    #
    # SERVICES
    #

    app.config["FIREBASE_SERVICE"] = firebase_service

    #
    # ROUTES
    #

    app.register_blueprint(home_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)

    return app



if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
