
    # ...

    oauth = OAuth(app)
    oauth.register(
        name="google",
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"}
        #client_id=GOOGLE_CLIENT_ID,
        #client_secret=GOOGLE_CLIENT_SECRET,
        #authorize_params={"access_type": "offline"} # give us the refresh token! see: https://stackoverflow.com/questions/62293888/obtaining-and-storing-refresh-token-using-authlib-with-flask
    )
    app.config["OAUTH"] = oauth

    # ...
