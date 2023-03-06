# Deploying to Render

# Resources

  + https://render.com/docs/deploy-flask


## Render Setup

Login to [render](https://dashboard.render.com) and visit the dashboard.

Create a New Web Service. Choose repo via URL.

Specify start command:

```
gunicorn "web_app:create_app()"
```

Set environment variables:

```sh
GOOGLE_CLIENT_ID="______.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="______"
GOOGLE_CREDENTIALS_FILEPATH="/etc/secrets/google-credentials.json"
SECRET_KEY="YOUR SECRET HERE"
```

Set a [secret configuration file](https://community.render.com/t/using-google-application-credentials-json/6885) called "google-credentials.json", and paste the contents from your google service account credentials file. The render web service will then have access to the file as "/etc/secrets/google-credentials.json".


# Google Cloud Setup

Under [credentials](https://console.cloud.google.com/apis/credentials/) for your web client, configure a redirect url pointing to the render server: "https://YOUR_RENDER_APP.onrender.com/auth/google/callback" and save.

While the web client is in test mode, only tests users can use in production, in which case you may need to add your email address as a "Test User" in the OAuth consent screen. Otherwise publish the app.
