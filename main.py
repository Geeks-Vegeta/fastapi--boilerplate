from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routers import blog_router


description = '''

This is an example of blog api
For NextJs Blogging Application
💋

'''

app = FastAPI(
    title="Blog API",
    description=description,
    version=0.1
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ok"}

app.include_router(blog_router.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)