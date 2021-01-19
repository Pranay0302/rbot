from decouple import config
import praw
import time

def auth():
    reddit = praw.Reddit(
     client_id=config("client_id"),
     client_secret=config("client_secret"),
     password=config("password"),
     username=config("username"),
     user_agent=config("user_agent")
    )
    # print(reddit.user.me())
    return reddit

def extract(reddit):
    subreddit = reddit.subreddit("ImaginarySliceOfLife")
    for submission in subreddit.hot(limit=10):
        print(submission.title)
    print("<----done---->")
    exit(0)

