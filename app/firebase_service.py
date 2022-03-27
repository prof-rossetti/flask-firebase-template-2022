

import os
from pprint import pprint

from firebase_admin import credentials, initialize_app, firestore #, auth

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")

def fetch_products():
    return []

class FirebaseService:
    """
    Fetches data from the cloud firestore database.
    """
    def __init__(self):
        self.creds = credentials.Certificate(CREDENTIALS_FILEPATH)
        self.app = initialize_app(self.creds) # or set FIREBASE_CONFIG variable and initialize without creds
        self.db = firestore.client()

    def fetch_products(self):
        products_ref = self.db.collection("products")
        products = [doc.to_dict() for doc in products_ref.stream()]
        return products


if __name__ == "__main__":


    service = FirebaseService()

    print("PRODUCTS...")
    products = service.fetch_products()
    pprint(products)
