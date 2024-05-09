Task Meta-Info
# Introduction
The `docker-compose.yml` file provides access to `Feddit` which is a fake reddit API built to complete the Allianz challenge. 

# How-to-run
1. Please make sure you have docker installed.
2. To run `Feddit` API locally in the terminal, replace `<path-to-docker-compose.yml>` by the actual path of the given `docker-compose.yml` file in `docker compose -f <path-to-docker-compose.yml> up -d`. It should be available in [http://0.0.0.0:8080](http://0.0.0.0:8080). 
3. To stop `Feddit` API in the terminal,  replace `<path-to-docker-compose.yml>` by the actual path of the given `docker-compose.yml` file in `docker compose -f <path-to-docker-compose.yml> down`.

# API Specification
Please visit either [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs) or [http://0.0.0.0:8080/redoc](http://0.0.0.0:8080/redoc) for the documentation of available endpoints and examples of the responses.
There are 3 subfeddits available. For each subfeddit there are more than 20,000 comments, that is why we use pagination in the JSON response with the following parameters:

+ `skip` which is the number of comments to be skipped for each query
+ `limit` which is the max returned number of comments in a JSON response.

# Data Schemas
## Comment

+ **id**: unique identifier of the comment.
+ **username**: user who made/wrote the comment.
+ **text**: content of the comment in free text format.
+ **created_at**: timestamp in unix epoch time indicating when the comment was made/wrote.

## Subfeddit
+ **id**: unique identifier of the subfeddit
+ **username**: user who started the subfeddit.
+ **title**: topic of the subfeddit.
+ **description**: short description of the subfeddit.
+ **comments**: comments under the subfeddit.


TASK
A)Problem Statement

You are asked to design and develop a small microservice application offering a RESTful API that identifies if comments on a given subfeddit or category are positive or negative.

Given the name of a subfeddit the application should return: - A list of the most recent comments. Suppose a limit of 25 comments.

For each comment:

1)The unique identifier of the comment

2)The polarity score and the classification of the comment (positive, or The text of the comment negative) based on that score.

Optionally, you should allow the user to modify the query by Filter comments by a specific time range Sort the results by the comments polarity score.

Define a GitHub workflow to run linting checks and tests for the built RESTful API

B)Requirements

The application must be written in Python and non-code deliveries must be in the English language. Please ensure that your code is understandable and production-ready.


C)Hints

Get familiar with Feddit, which stands for fake Reddit, and mocks the Reddit API. All the related information to Feddit is in the zip file attached.

Additional hints

Keep in mind that we will be focusing on the engineering aspects of the task, so you are not required to build a ML model from scratch. If you prefer, you can use an external API for the ML model.

We are expecting to be able to run the code.

# Task Solution Info
## Structure
Created a "polarity_check" folder with the following structure:

- main.py: Contains all code related to API creation and polarity logic.
- app (sub-folder): Contains meta-information files like models.py and views.py.
- requirements.txt: Includes all packages required for the application to work.
- Dockerfile: Facilitates easier deployment and ensures environment independence.
## Solution
- Utilized FastAPI for creating the REST APIs.
- Developed custom logic for polarity analysis, capable of handling cross-functional API calls to meet the requirements.
- Leveraged Python packages for generating polarity scores for comment text:
- Experimented with NLTK and TextBlob packages; ultimately, NLTK performed better with our text data, thus chosen.
- Aimed to simplify setup and utilization of this microservice by using Docker, making the project independent. Integrated it into the existing docker-compose.yml for easy service startup.
- Note: Alternative packages or models can be substituted to replace the sentiment analysis logic.
- Note: The sentiment analysis logic can also be replaced by making API calls to a model.

## Steps For Starting the Services
- Ensure Docker is installed and the repository is cloned.
- Build all required containers from images using the command: docker-compose -f .\docker-compose.yml build.
- Start all required containers with the command: docker-compose -f .\docker-compose.yml up.
