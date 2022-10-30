from fastapi import Body
from typing import Union, List
from pydantic import BaseModel, Field
from functions.db_functions import PyObjectId
from bson.objectid import ObjectId


class BlogData(BaseModel):
    id:PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    body: str
    tags: List[str] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
        schema_extra = { 
            "example": {
                "title": "STL in C++",
                "body": "<html>what is css</html>",
                "tags": ["c++", "programming", "dsalgo"]
            }
        }


class BlogResponse(BaseModel):
    id:PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}