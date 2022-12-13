# Python
from typing import List
# Pydantic

# FastAPI
from fastapi import FastAPI, status

# Models
from models import *

app = FastAPI()

# Path Operations


## Users

@app.post(
    path = "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a User",
    tags = ["Users"]
)
def signup():
    pass

@app.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a User",
    tags = ["Users"]
)
def login():
    pass

@app.get(
    path = "/users",
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Get all User",
    tags = ["Users"]
)
def get_all_users():
    pass

@app.get(
    path = "/users/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Get a User",
    tags = ["Users"]
)
def get_a_user():
    pass

@app.delete(
    path = "/signup/{user_id}/delete",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a User",
    tags = ["Users"]
)
def delete_a_user():
    pass

@app.put(
    path = "/signup/{user_id}/update",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Update a User",
    tags = ["Users"]
)
def update_a_user():
    pass

## Tweets

@app.get(
    path = "/",
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK,
    summary = "Get all Tweets",
    tags = ["Tweets"]
)
def home():
    pass

@app.post(
    path = "/post",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags = ["Tweets"]
)
def post():
    pass

@app.get(
    path = "/tweets/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "get a tweet",
    tags = ["Tweets"]
)
def get_a_tweet():
    pass

@app.delete(
    path = "/tweets/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "delete a tweet",
    tags = ["Tweets"]
)
def delete_a_tweet():
    pass

@app.put(
    path = "/tweets/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "update a tweet",
    tags = ["Tweets"]
)
def update_a_tweet():
    pass