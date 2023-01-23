from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {
        'data': {
            'name': 'Sabanai'
        }}

@app.get('/blog')
def getBlog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}
        

@app.get('/blog/unplublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2', id}}

class Blog(BaseModel): 
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}
