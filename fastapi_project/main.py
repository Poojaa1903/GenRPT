from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# "/" is called "Base Path" and "/about" is called "About Path"
# Get, Put, Post & Delete method are called "Operation" i.e. "Operation On The Path"
# @app.get('/) is called "Path Operation Decorator"
# The function on which we are defining the operation and the path using the app decorator is called "Path Operation Function"

@app.get('/blog')
def index(limit = 10, published : bool = True, sort : Optional[str] = None): #if i do not want a parameter to have default value then i will just keep it as optional, just like i did it with sort
    # published or unpublished blogs with few limits
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unplushed blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f"Blog is created with title as {request.title}"}