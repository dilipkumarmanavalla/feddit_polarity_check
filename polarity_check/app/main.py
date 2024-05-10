"""
Main module for the Polarity Check API
"""

from fastapi import FastAPI, HTTPException, Query
from models import Comment  # Importing Comment model from models module
import requests
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

app = FastAPI()

FEDDIT_URL = "http://feddit:8080"

# Endpoint to retrieve comments from Feddit
@app.get("/comments")
async def get_comments(
    subfeddit_id: str,
    skip: int = 0,
    limit: int = 25,
    start_time: int = None,
    end_time: int = None,
    sort_by_score: bool = False,
):
    params = {
        "subfeddit_id": subfeddit_id,
        "skip": skip,
        "limit": limit,
    }
    try:
        response = requests.get(
            f"{FEDDIT_URL}/api/v1/comments",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        response = dict(response.json())
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving comments from Feddit: {e}")

    if len(response['comments']) > 0:
        comments = response['comments']

        # Filter comments based on start_time and end_time
        if start_time is not None:
            comments = [comment for comment in comments if comment["created_at"] >= start_time]
        if end_time is not None:
            comments = [comment for comment in comments if comment["created_at"] <= end_time]

        # Perform Sentiment Analysis on comments
        comments = analyse_and_generate_polarity(comments)

        if sort_by_score:
            comments.sort(key=lambda x: x.get("polarity_score", 0), reverse=True)

        formatted_comments = [
            Comment(id=str(comment["id"]), username=comment["username"], text=comment["text"],
                    created_at=comment["created_at"], polarity=comment["polarity"])
            for comment in comments
        ]
        response.update({'comments': formatted_comments})

    return response

# Function to perform Sentiment Analysis and generate polarity score for comments
def analyse_and_generate_polarity(comments):
    updated_comments = []
    for i in comments:
        temp_dict = dict(i)
        sentiment_scores = sia.polarity_scores(temp_dict['text'])

        if sentiment_scores['neg'] <= sentiment_scores['pos']:
            score, polarity = 1, 'positive'
        else:
            score, polarity = 0, 'negative'

        temp_dict['polarity_score'] = score
        temp_dict['polarity'] = polarity
        updated_comments.append(temp_dict)
    return updated_comments

# Endpoint for health check
@app.get("/health_check")
async def health_check():
    return {"Status": 'Up'}
