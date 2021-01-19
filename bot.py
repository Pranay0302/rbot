from decouple import config
import praw 

def auth():
    reddit = praw.Reddit(
     client_id=config("client_id"),
     client_secret=config("client_secret"),
     password=config("password"),
     username=config("username"),
     user_agent=config("user_agent")
    )
    print(reddit.user.me())

auth()
