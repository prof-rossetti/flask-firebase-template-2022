
import functools
from flask import session, redirect, flash

def authenticated_route(view):
    """
    Wrap a route with this decorator to prevent unauthenticated access.

    If the user is logged in, the route will have access to the "current_user" info stored in the session.

    If user is not logged in, the route will redirect them to the login page.

    See: https://flask.palletsprojects.com/en/2.0.x/tutorial/views/#require-authentication-in-other-views
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get("current_user"):
            #print("CURRENT USER:", session["current_user"])
            return view(**kwargs)
        else:
            print("UNAUTHENTICATED...")
            flash("Unauthenticated. Please login!", "warning")
            return redirect("/login")
    return wrapped_view
