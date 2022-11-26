from pymongo import MongoClient
import pymongo
class temperatureService():
    def get_database(self):
 
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        
        client = pymongo.MongoClient("mongodb+srv://user:user@cluster0.gwusa.mongodb.net/?retryWrites=true&w=majority")
        db = client.employer
        collection = db['employers']
        cursor = collection.find({})
        for document in cursor:
          return document
        print(db)
        # This is added so that many files can reuse the function get_database()
    def getTemperature():
        c = temperatureService()
        
        return c.get_database()