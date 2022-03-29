# Deployer's Guide

## Services Setup

Ideally create a separate Google Cloud project and Firebase project for your user-facing production application, following the instructions in the README.

Setup a production "OAuth Client". Obtain the web client's `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`. After you create your server for the first time (see server setup instructions below), you'll know what it's URL is, at which point your can return to this section to set the following "Authorized Redirect URIs":

  + https://YOUR_SERVER_NAME.herokuapp.com/auth/google/callback

Download the production service account credentials JSON file and store it in this repo as "google-credentials-prod.json", and use it when configuring the server (see below).

## Server Setup

Provisioning the server (first time only), using a name like "flask-firebase-template-2022" (but yours will need to be different / unique, i.e. YOUR_SERVER_NAME):

```sh
#heroku create flask-firebase-template-2022
heroku create YOUR_SERVER_NAME
```

Set environment variables (first time only):

```sh
heroku config:set APP_ENV="production"

# use your own secret password (to protect / encrypt data in the session):
heroku config:set SECRET_KEY="________"

# use your own google oauth client credentials:
heroku config:set GOOGLE_CLIENT_ID="______.apps.googleusercontent.com"
heroku config:set GOOGLE_CLIENT_SECRET="____________"

heroku config:set GA_TRACKER_ID="G-________"
```

## Server Deploy

Deploying:

```sh
git push heroku main
#git push heroku mybranch:main
```

Configuring remote credentials file:

```sh
#heroku buildpacks:set heroku/python
heroku buildpacks:add https://github.com/s2t2/heroku-google-application-credentials-buildpack

# stores contents of local credentials file into an environment variable on the server
# ... references local creds file (e.g. "google-credentials-prod.json"):
heroku config:set GOOGLE_CREDENTIALS="$(< google-credentials-prod.json)"

# references the remote credentials file on the server (not necessary right now):
#heroku config:set GOOGLE_APPLICATION_CREDENTIALS="google-credentials.json"
```
