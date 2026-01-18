from pymongo import MongoClient
from dotenv import dotenv_values

env = dotenv_values(".env")

if env["STATUS"] == "PROD":
    client = MongoClient(host=env["MONGO_URL"])
else:
    client = MongoClient(host=env["HOST"], port=env["PORT"])

database = client.beccatk
