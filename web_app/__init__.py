

import os
from dotenv import load_dotenv

from flask import Flask
from authlib.integrations.flask_client import OAuth

#from app import APP_ENV, APP_VERSION
#from app.firebase_service import FirebaseService
#from app.gcal_service import SCOPES as GCAL_SCOPES
#from web_app.firebase_auth import FirebaseAuth, FIREBASE_CONFIG

from web_app.routes.home_routes import home_routes
from web_app.routes.auth_routes import auth_routes
from web_app.routes.user_routes import user_routes

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # IMPORTANT: override in production

APP_ENV = os.getenv("APP_ENV", default="development") # IMPORTANT: set to "production" in production
APP_VERSION = os.getenv("APP_VERSION", default="v0.0.1") # TODO: update upon new releases

APP_TITLE = "My App"
# https://icons.getbootstrap.com/
NAV_ICON_CLASS = "bi-globe"
# https://getbootstrap.com/docs/5.1/components/navbar/#color-schemes
# https://getbootstrap.com/docs/5.1/customize/color/#theme-colors
NAV_COLOR_CLASS = "navbar-dark bg-primary"

GA_TRACKER_ID = os.getenv("GA_TRACKER_ID", default="G-OOPS")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")




def create_app():

    #
    # INIT
    #

    app = Flask(__name__)

    #
    # CONFIG
    #

    #app.secret_key = SECRET_KEY
    app.config["SECRET_KEY"] = SECRET_KEY # for flask flash messaging

    #app.config.from_object('config')
    app.config["APP_ENV"] = APP_ENV
    app.config["APP_VERSION"] = APP_VERSION
    app.config["APP_TITLE"] = APP_TITLE
    app.config["NAV_ICON_CLASS"] = NAV_ICON_CLASS
    app.config["NAV_COLOR_CLASS"] = NAV_COLOR_CLASS

    app.config["GA_TRACKER_ID"] = GA_TRACKER_ID # for client-side google analytics
    #app.config["GA_TRACKER_ID"] = FIREBASE_CONFIG["measurementId"] # GA_TRACKER_ID # for client-side google analytics

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

    #app.config["FIREBASE_AUTH"] = FirebaseAuth().auth

    #
    # SERVICES
    #

    #app.config["FIREBASE_SERVICE"] = FirebaseService()

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
