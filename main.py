# to start with fastapi we need to import fastapi

from fastapi import FastAPI

app = FastAPI() #to create an instance of fastapi

@app.get("/") # to create a route "/" is the root route
def welcome():
    return {"message": "welcome to fastapi tutorial"}

@app.get("/about")
def about():
    return {"message": "this is an about page"}

@app.get("/contact")
def contact():
    return {"message": "this page is about contact releated things"}

@app.get("/blog")
def blog():
    return {"message": "this page is about blogs"}