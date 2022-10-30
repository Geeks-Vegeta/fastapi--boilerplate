from fastapi import APIRouter, status
from typing import List, Union
from schema.blog_schema import BlogData, BlogResponse
from services.blog import create_blog, all_blog, update_blog, find_blog, delete_blog

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


@router.post("/create",status_code=status.HTTP_201_CREATED)
async def Create(blog:BlogData):
    return await create_blog(blog)


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[BlogResponse])
async def AllBlogs():
    return await all_blog()


@router.put("/update", status_code=status.HTTP_200_OK)
async def Update(blog:BlogData):
    return await update_blog(blog)


@router.get("/getblog", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def GetOneBlog(title:str):
    return await find_blog(title)

@router.delete("/delete", status_code=status.HTTP_200_OK)
async def DeleteBlog(title:str):
    return await delete_blog(title)