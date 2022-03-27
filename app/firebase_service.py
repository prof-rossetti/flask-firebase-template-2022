

import os
from pprint import pprint
from datetime import datetime, timezone

from firebase_admin import credentials, initialize_app, firestore #, auth

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")


def generate_timestamp():
    return datetime.now(tz=timezone.utc),


class FirebaseService:
    """
    Fetches data from the cloud firestore database.

    Uses locally downloaded credentials JSON file.
    """
    def __init__(self):
        self.creds = credentials.Certificate(CREDENTIALS_FILEPATH)
        self.app = initialize_app(self.creds) # or set FIREBASE_CONFIG variable and initialize without creds
        self.db = firestore.client()

    def fetch_products(self):
        products_ref = self.db.collection("products")
        products = [doc.to_dict() for doc in products_ref.stream()]
        return products

    def fetch_orders(self):
        orders_ref = self.db.collection("orders")
        orders = [doc.to_dict() for doc in orders_ref.stream()]
        return orders

    def create_order(self, user_email, product_info):
        """
        Params :

            new_order (dict) like ...

                {
                    "user_email": user_email, #> str
                    "product_id": product_id, #> dict
                    "product_info": product_info,
                }

        """
        orders_ref = self.db.collection("orders")
        order_ref = orders_ref.document() # new document with auto-generated id

        new_order = {
            "user_email": user_email,
            "product_info": product_info,
            "order_at": generate_timestamp()
        }
        results = order_ref.set(new_order)
        #print(results) #> {update_time: {seconds: 1648419942, nanos: 106452000}}
        return new_order, results




if __name__ == "__main__":


    service = FirebaseService()

    print("-----------")
    print("PRODUCTS...")
    products = service.fetch_products()
    pprint(products)

    print("-----------")
    print("NEW ORDER...")
    product = products[0]
    email_address = input("Email Address: ") or "hello@example.com"
    new_order, results = service.create_order(user_email=email_address, product_info=product)
    pprint(new_order)

    print("-----------")
    print("ORDERS...")
    orders = service.fetch_orders()
    print(len(orders))
