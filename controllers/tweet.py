from typing import List

from fastapi import APIRouter, status

from schemas import Tweet

router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


## Tweets

@router.get(
    path = "/",
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK,
    summary = "Get all Tweets",
    tags = ["Tweets"]
)
def home():
    pass

@router.post(
    path = "/post",
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags = ["Tweets"]
)
def post():
    pass

@router.get(
    path = "/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "get a tweet",
    tags = ["Tweets"]
)
def get_a_tweet():
    pass

@router.delete(
    path = "/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "delete a tweet",
    tags = ["Tweets"]
)
def delete_a_tweet():
    pass

@router.put(
    path = "/{tweet_id}",
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "update a tweet",
    tags = ["Tweets"]
)
def update_a_tweet():
    pass