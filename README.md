# Discours
This is a pet project created to explore (revise) API usage and relevant technologies.

# Setting up
- Create a new python environment, activate it and run the command to install dependencies:
- - ``pip install -r requirements.txt``
- Run the following command to activate the local hosting
- - ``uvicorn app.main:app --reload``
- Use curl or postman to experiment with the various available commands

# Available Commands
The URL will be ``http://127.0.0.1:8000`` across all of these commands
- GET {{URL}}/posts:
- - This will print all the existings posts (requires login)
- GET {{URL}}/posts/{id}
- - This will print the post with the referred id (requires login)
- DELETE {{URL}}/posts/{id}
- - This will delete the post with the referred id (requires login)
- UPDATE {{URL}}/posts/{id}
- - This will update the post with the referred id (requires login)
- POST {{URL}}/posts
- - THis will create a new post with the given content (requires login)
- POST {{URL}}/users
- - This will create a new user with the given email (should be unique) and password
- GET {{URL}}/users/{id}
- - This will return some basic information about the user with the given id
- POST {{URL}}/login
- - This will let a user login by returning an access_token to use in other commands, if provided the correct email and password combination
- POST {{URL}}/vote
- - This will let a user vote on any given post, the total vote count of a post will shown when using GET method for it, every vote on a post requires a unique user, the user may remove the vote too by implying direction in this method. Finally, there is no downvote, the user can only add a vote or remove their pre-existing vote.


# The plan
Implemented:
- There is a fully functioning backend for an online forum-esque app where users can post and delete content
- Posts can be created, deleted, updated, and voted on
- Authentication is implemented using JWT Tokens and is enforced
- Technologies used:
- - PostgreSQL for the database
- - Python with FASTAPI for setting up APIs 
- - SQLAlchemy and Alembic to abstract and automate communication with the database
- - While not packaged up as part of the application, POSTMAN was used for managing API requests

In Progress:
- Heroku

Future work:
- NGINX technologies implement
- Shifting from a windows to linux environment and dockerizing the whole application
- Automating Testing
- CI/CD