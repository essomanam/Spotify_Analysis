# -*- encoding: utf-8 -*-

from datetime import datetime
import json
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('your_mongo_uri')
db = client['your_database_name']

class Datas:

    def __init__(self, _id, acousticness, data):
        self.id = _id
        self.acousticness = acousticness
        self.data = data

    def save(self):
        db.datas.insert_one(self.to_dict())

    def update_data(self, new_data):
        db.datas.update_one({"_id": ObjectId(self.id)}, {"$set": {"data": new_data}})

    @classmethod
    def get_by_id(cls, _id):
        result = db.datas.find_one({"_id": ObjectId(_id)})
        if result:
            return cls(_id=str(result['_id']), acousticness=result['acousticness'], data=result['data'])
        return None

    def to_dict(self):
        return {
            "_id": ObjectId(self.id),
            "acousticness": self.acousticness,
            "data": self.data
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=str)
