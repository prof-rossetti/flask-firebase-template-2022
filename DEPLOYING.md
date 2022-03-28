# Deployer's Guide

## Services Setup

Ideally create a separate Google Cloud project and Firebase project for your user-facing production application, following the instructions in the README.

## Server Setup

Provisioning the server (first time only), using a name like "flask-firebase-template-2022" (but yours will need to be different / unique):

```sh
heroku create flask-firebase-template-2022
```

Set environment variables (first time only):

```sh
heroku config:set APP_ENV="production"

# use your own secret password (to protect / encrypt data in the session):
heroku config:set SECRET_KEY="________"

# use your own google oauth client credentials:
heroku config:set GOOGLE_CLIENT_ID="______.apps.googleusercontent.com"
heroku config:set GOOGLE_CLIENT_SECRET="____________"

#heroku config:set GA_TRACKER_ID="G-________"
```

## Server Deploy

Deploy:

```sh
git push heroku main
#git push heroku mybranch:main
```

```sh
#heroku buildpacks:set heroku/python
heroku buildpacks:add https://github.com/s2t2/heroku-google-application-credentials-buildpack
heroku config:set GOOGLE_CREDENTIALS="$(< google-credentials-prod.json)" # references local creds

heroku config:set GOOGLE_APPLICATION_CREDENTIALS="google-credentials.json" # references remote creds
```
