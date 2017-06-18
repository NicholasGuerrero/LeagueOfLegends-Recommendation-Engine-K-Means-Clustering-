"""Contains a connection to the MongoDb and a function to return a cursor"""

from pymongo import MongoClient

def connect(collection):
    """Connects to the Heroku Mongo DB and returns the specified connection."""

    ##MongoDB Parameters
    client = MongoClient("mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7")
    database = client["heroku_0dkc9rh7"]

    return database[collection]
