# flask-firebase-template-2022

A web application starter template, created in Python with the Flask framework. Allows users to login with their Google accounts (via OAuth). Interfaces with a Google Cloud Firestore database.

![](https://user-images.githubusercontent.com/1328807/160312385-7ffbbada-4363-4b48-873d-9eca868afef0.png)

> NOTE: currently the login with google functionality works, but the login with email and password is not yet implemented.

## Prerequisites

This application requires a Python development environment:

  + Git
  + Anaconda, Python, Pip

For beginners, here are some instructions for how to install Anaconda, and [set up your local Python development environment](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/local-dev-setup/README.md#anaconda-python-and-pip).

## Repo Setup

Make a copy of this template repo (as necessary). Clone your copy of the repo onto your local machine. Navigate there from the command-line.

Setup and activate a new Anaconda virtual environment:

```sh
conda create -n flask-firebase-env python=3.8
conda activate flask-firebase-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Services Setup

This app requires a few services, for user authentication and data storage. Follow the instructions below to setup these services.

### Google Cloud Project

Visit the [Google Cloud Console](https://console.cloud.google.com). **Create a new project**, and name it. After it is created, select it from the project selection dropdown menu.

### Google OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id".

Click to "Configure Consent Screen". Leave the domain info blank, and leave the defaults / skip lots of the setup for now. If/when you deploy your app to a production server, you can return to populating this info (or you will be using a different project).

Return to actually creating the "OAuth Client Id". Choose a "Web application" type, give it a name, and set the following "Authorized Redirect URIs" (for now, while the project is still in development):

  + http://localhost:5000/auth/google/callback

After the client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`, and set them as environment variables (see configuration section below).

### Firebase Project

Visit the [Google Firebase Console](https://console.firebase.google.com/) to **create a new Firebase project**. When you create the project:

  1. Select the Google Cloud project you just created from the dropdown.
  2. Enable Google Analytics.
  3. Configure Google Analytics:
     1. Choose an existing Google Analytics account or create a new one.
     2. Automatically create a new property in this account.

### Google Analytics

From the Firebase project's "Analytics Dashboard" menu, find the web property that was created during the previous step.

If there was an issue and you don't see anything, no worries - you can click the web icon to "Add Firebase to your web app". Give the app a name and register it (hosting not necessary).

You should now be able to visit [Google Analytics](https://analytics.google.com/) and find the web property you created. From Google Analytics, visit the web property's admin settings, specifically the "Property Settings", and find the numeric **Property Id** (e.g. "XXXXXXXXXX"). Use this value for the `GA_TRACKER_ID` environment variable, in this format: `"UA-XXXXXXXXXX-1"` (see "Environment Variables" section below).


### Firestore Database Setup

Follow [this guide](https://firebase.google.com/docs/firestore/quickstart) to create a Firestore database for the Firebase project you just created. When you create the database, "start in test mode".

**Products Collection**

After the database has been created, create a new collection called "products" with a number of documents inside. Create each document using an auto-generated "Document Id", as well as the attributes:

  + `name` (string)
  + `description` (string)
  + `price` (number)
  + `url` (string)

Populate the "products" documents based on the following examples:

name | description | price | url
--- | --- | --- | ---
Strawberries | Juicy organic strawberries. | 4.99 | https://picsum.photos/id/1080/360/200
Cup of Tea | An individually-prepared tea or coffee of choice. | 3.49 | https://picsum.photos/id/225/360/200
Textbook | It has all the answers. | 129.99 | https://picsum.photos/id/24/360/200


**Orders Collection**

There will also be an "orders" collection, which will get auto-generated and populated as a result of running the app. It will have the following structure:

  + `user_email` (string)
  + `product_info` (map)
  + `order_at` (timestamp)

**Users Collection**

In the future, if you want to store more information about your users, for example their settings, preferences, and activities, you can create a "users" collection and extend this app's functionality as desired.

### Google APIs Service Account Credentials

To fetch data from the Firestore database (and use other Google APIs), the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, find the service account created during the firebase project setup process (it should be called something like "firebase-adminsdk"), or feel free to create a new service account.

For the chosen service account, create new JSON credentials file as necessary from the "Keys" menu, then download the resulting JSON file into the root directory of this repo, specifically named "google-credentials.json".



## Configuration

Create a file called ".env" in the root directory of this repository, and populate it with environment variables to specify your own credentials, as obtained in the "Setup" section above:

```sh
FLASK_APP="web_app"

#
# GOOGLE OAUTH
#
GOOGLE_CLIENT_ID = "..."
GOOGLE_CLIENT_SECRET = "..."

#
# GOOGLE ANALYTICS
#
GA_TRACKER_ID="UA-XXXXXXX-1"
```




## Usage

### Firebase Service

After configuring the Firestore database and populating it with products, you should be able to test out the app's ability to fetch products (and generate new orders):

```sh
python -m app.firebase_service
```

### Web Application

Run the local web server (then visit localhost:5000 in a browser):

```sh
FLASK_APP=web_app flask run
```


## Testing

Instructions TBA



## Deploying

See the [Deployer's Guide](/DEPLOYING.md) for instructions on deploying to a production server hosted by Heroku.
