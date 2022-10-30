from pymongo import MongoClient
from fastapi import HTTPException
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv 

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client['nextblogs']
blog = db['blog']


async def check_title(title):
    try:
        blog_exists = blog.find_one({"title":title})
        return blog_exists

    except Exception as e:
      print(e)



class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

