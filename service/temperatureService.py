from pymongo import MongoClient
import pymongo
import json
import bson.json_util as json_util

class temperatureService():
    def get_database(self):
        client = pymongo.MongoClient("mongodb+srv://user:user@cluster0.gwusa.mongodb.net/?retryWrites=true&w=majority")
        db = client.grow_temperature
        collection = db['temperature']
        return collection

    def getTemperature():
        c = temperatureService()
        databaseClient = c.get_database()
        cursor = list(databaseClient.find({}))
        sizeArray = int((len(cursor))) - 1
        return json.loads(json_util.dumps(cursor[sizeArray]))

    def timelineTemp():
        c = temperatureService()
        databaseClient = c.get_database()
        cursor = list(databaseClient.find({}))
        return json.loads(json_util.dumps(cursor))