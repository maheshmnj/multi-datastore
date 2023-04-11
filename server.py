import os
from pymongo import MongoClient
import urllib.parse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv

from firebase import *

load_dotenv()
username = os.getenv("USERNAME_MONGO")
password = os.getenv("PASSWORD_MONGO")

cluster_url = os.getenv("CLUSTER_URL_MONGO")
connection_string = os.getenv("CONNECTION_STRING_MONGO")

class Server:
    def __init__(self):
        self.db_mongo = None
        self.db_firebase = None

    def connect_mongo(self):
        client = MongoClient(connection_string)
        db = client['mydb']
        return db

    def connect_firebase(self):
        cred = credentials.Certificate("serviceaccount.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db

    def connect(self):
        self.db_mongo = self.connect_mongo()
        self.db_firebase = self.connect_firebase()
        return self.db_mongo, self.db_firebase

if __name__ == '__main__':

    server = Server()
    server.connect()
    event = Event()
    user = User()
     # Insert Bookmarks

    # for i in range(0, len(event_dicts)):
    #     event_dict = event_dicts[i]
    #     user_dict = user_dicts[i% len (user_dicts)]
    #     event = event.event_from_dict(event_dict)
    #     user = user.user_from_dict(user_dict)
    #     event.insert_bookmark(user)
    #     print(event.event_to_dict()['id'])

    # Get Bookmarks

    user = user.user_from_dict(user_dicts[1])
    bookmarked_events = event.get_bookmarks(user)
    for bookmarked_event in bookmarked_events:
       temp_event = event.bookmarked_event_from_dict(bookmarked_event)
       temp_event.user = user
       print(temp_event.name)


