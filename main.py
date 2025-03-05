# to start with fastapi we need to import fastapi

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI() #to create an instance of fastapi

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/") # to create a route "/" is the root route
def welcome():
    return {"message": "welcome to fastapi tutorial"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.published)
    return {"data": new_post}

# title 