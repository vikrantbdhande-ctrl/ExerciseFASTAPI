
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"Message": "Hello  NEW Vikrant's World!"}

@app.get("/name/{item}")
def put(item:str):
    return { "Message" : "Hello " + item + "!" + " How are you?" }

@app.get("/posts") 
def get_post():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print( post.dict())
    return {"data": post} 
# Title str, content str
