# flask-firebase-template-2022


## Repo Setup

Clone this repo onto your local machine. Navigate there from the command-line.

Setup and activate a new virtual environment:

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


### Firebase Project

Visit the [Google Firebase Console](https://console.firebase.google.com/) to **create a new Firebase project**. When you create the project:

  1. Select the Google Cloud project you just created from the dropdown.
  2. Enable Google Analytics.
  3. Configure Google Analytics:
     1. Choose an existing Google Analytics account or create a new one.
     2. Automatically create a new property in this account.

### Firebase Auth

After creating the Firebase project, visit it's "Authentication" settings, and "Get Started" to **enable the "Google" sign-in option**.

Click the gear icon to visit the "Project Settings" page, locate the "Your Apps" section, and **create a Web App**, or use an existing one. When you create the app (or in the future by visiting its settings page, finding the "Firebase SDK snippet", and clicking "Config"), you'll see the **Firebase SDK credentials**. Use these values for the `FIREBASE_` environment variables (see "Configuration" section below).

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


### Google APIs Service Account Credentials

In order to fetch data from the database, we'll need to use the credentials generated during the firebase project setup.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials?) page, find the service account called something like "firebase-adminsdk", or create a new service account. For the given service account, create new JSON credentials file as necessary from the "Keys" menu, and download the resulting JSON file into the root directory of this repo, specifically named "google-credentials.json".

> NOT NECESSARY?:
>
>Then from the root directory of this repo, set the credentials as an >environment variable:
>
>```sh
>export GOOGLE_API_CREDENTIALS="$(< google-credentials.json)"
>echo $GOOGLE_API_CREDENTIALS
> ```

### Google Analytics

> Visit https://analytics.google.com/ and navigate to the web property you created via the Firebase project creation process. Visit the web property's admin settings, specifically the "Property Settings", and find the numeric **Property Id** (e.g. "XXXXXXXXXX"). Use this value for the `GA_TRACKER_ID` environment variable, in this format: `"UA-XXXXXXXXXX-1"` (see "Environment Variables" section below).


## Configuration

Create a file called ".env" in the root directory of this repository, and specify your own credentials, as obtained in the "Setup" section above:

```sh
FLASK_APP="web_app"

#
# GOOGLE OAUTH
#

GOOGLE_CLIENT_ID = "..."
GOOGLE_CLIENT_SECRET = "..."

#
# FIREBASE
#

#FIREBASE_API_KEY="_______"
#FIREBASE_AUTH_DOMAIN="my-project-123.firebaseapp.com"
#FIREBASE_PROJECT_ID="my-project-123"
#FIREBASE_STORAGE_BUCKET="my-project-123.appspot.com"
#FIREBASE_MESSAGING_SENDER_ID="_______"
#FIREBASE_APP_ID="_______"
##FIREBASE_MEASUREMENT_ID="G-XXXXXXXXXX"
#FIREBASE_DATABASE_URL="https://my-project-123.firebaseio.com"
```




## Usage

### Firebase Service

After configuring the cloud firestore database and populating it with products, you should be able to test out the app's ability to fetch them (and generate new orders):

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

Instructions TBA
