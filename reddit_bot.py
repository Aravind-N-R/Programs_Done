import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Skill issue fr v1.0")
    return r

def run_bot(r):
    for comment in r.subreddit('testing273').comments(limit=25):
        if "skill issue" in comment.body:
            print("Skill issue fr")
            comment.reply("Skill issue ong")

r = bot_login()
run_bot(r)