import praw
import config

def signIn():
    r = praw.Reddit(client_id='CLIENT_ID',
                client_secret="CLIENT_SECRET",
                password='PASSWORD',
                user_agent='USERAGENT',
                username='USERNAME')
return r

