

import os
from pprint import pprint
from datetime import datetime, timezone
from operator import itemgetter

from firebase_admin import credentials, initialize_app, firestore

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")


def generate_timestamp():
    return datetime.now(tz=timezone.utc)


class FirebaseService:
    """
    Fetches data from the cloud firestore database.

    Uses locally downloaded credentials JSON file.
    """
    def __init__(self):
        self.creds = credentials.Certificate(CREDENTIALS_FILEPATH)
        self.app = initialize_app(self.creds) # or set FIREBASE_CONFIG variable and initialize without creds
        self.db = firestore.client()

    #
    # PRODUCTS
    #

    def fetch_products(self):
        products_ref = self.db.collection("products")
        products = [doc.to_dict() for doc in products_ref.stream()]
        return products

    #
    # ORDERS
    #

    def create_order(self, user_email, product_info):
        """
        Params :

            user_email (str)

            product_info (dict) with name, description, price, and url

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

    def fetch_orders(self):
        orders_ref = self.db.collection("orders")
        orders = [doc.to_dict() for doc in orders_ref.stream()]
        return orders

    def fetch_user_orders(self, user_email):
        orders_ref = self.db.collection("orders")

        query_ref = orders_ref.where("user_email", "==", user_email)

        # sorting requires configuration of a composite index on the "orders" collection,
        # ... so to keep it simple for students, we'll sort manually (see below)
        #query_ref = query_ref.order_by("order_at", direction=firestore.Query.DESCENDING) #.limit_to_last(20)

        # let's return the dictionaries, so these are serializable (and can be stored in the session)
        docs = list(query_ref.stream())
        orders = []
        for doc in docs:
            order = doc.to_dict()
            order["id"] = doc.id
            #breakpoint()
            #order["order_at"] = order["order_at"].strftime("%Y-%m-%d %H:%M")
            orders.append(order)
        # sorting so latest
        orders = sorted(orders, key=itemgetter("order_at"), reverse=True)
        return orders





if __name__ == "__main__":


    service = FirebaseService()

    print("-----------")
    print("PRODUCTS...")
    products = service.fetch_products()
    pprint(products)

    print("-----------")
    print("ORDERS...")
    orders = service.fetch_orders()
    print(len(orders))

    print("-----------")
    print("NEW ORDER...")
    product = products[0]
    email_address = input("Email Address: ") or "hello@example.com"
    new_order, results = service.create_order(email_address, product)
    pprint(new_order)

    print("-----------")
    print("USER ORDERS...")
    user_orders = service.fetch_user_orders(email_address)
    print(len(user_orders))
