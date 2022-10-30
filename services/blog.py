from fastapi import HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
from pymongo import MongoClient
from models.blog_model import Blog
from functions.db_functions import check_title
from fastapi import HTTPException, status
import os
from dotenv import load_dotenv 
from datetime import datetime, timedelta
from bson.objectid import ObjectId


load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
db = client['nextblogs']
blog = db['blog']



# new blog 
async def create_blog(blog):
    try:
        title_exists = await check_title(blog.title)

        if title_exists:
            return JSONResponse(
                status_code=400,
                content={"message": "title already exists"},
            )
 
        new_blog = Blog(
        title=blog.title,
        body=blog.body,
        tags=blog.tags
        )

        new_blog.save()

        return {"message": f"article created successfully"}

    except Exception as e:
      print(e)


async def all_blog():

    try:

        blogs = blog.find()
        return [x for x in blogs]

    except Exception as e:
      print(e)


async def update_blog(blog):

    try:
        blogs =  blog.find_one({"title":title})

        if blogs is None:
            return JSONResponse(
                status_code=404,
                content={"message": "This blog not found"},
            )

        blog.update_one({"title":title}, {"$set":{"title":blog.title, "body":blog.body, "tags":blog.tags}})
        return {"message": "article updated successfully"}
      
        return blogs
      
    except Exception as e:
      print(e)


async def find_blog(title):

    try:
        blogs =  blog.find_one({"title":title})

        if blogs is None:
            return JSONResponse(
                status_code=404,
                content={"message": "This blog not found"},
            )
        return blogs
      
    except Exception as e:
      print(e)



async def delete_blog(title):

    try:
        blogs =  blog.find_one({"title":title})

        if blogs is None:
            return JSONResponse(
                status_code=404,
                content={"message": "This blog not found"},
            )

        blog.delete_one({"title":title})
        
        return {"message":"deleted successfully"}
      
    except Exception as e:
      print(e)
