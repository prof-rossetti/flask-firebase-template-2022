### Google OAuth Client

> NOT USING

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id".

Click to "Configure Consent Screen". Leave the domain info blank, and leave the defaults / skip lots of the setup.


Return to actually creating the "OAuth Client Id". Choose "Web application", give it a name, and set the following "Authorized Redirect URIs" (for now, while the project is still in development):

  + http://127.0.0.1:5000/auth/google/callback
  + http://localhost:5000/auth/google/callback

After the client is created, note the `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET`, and set them as environment variables.
