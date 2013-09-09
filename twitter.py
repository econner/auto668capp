"""Twitter posting that you dont even have to think about.

This lets you post from one twitter account automatically
with a very easy interface.

Steps to make this work.

1. Create a twitter app on the developer site.
2. Make sure in settings to give the app read and write permissions.
3. Generate an access token for your personal account.
4. Set the environment variables to the consumer key and secret.
5. Set those environment variables.

"""

import tweepy
import os


class TwitterPoster():

    """Make it really easy to post to our twitter account."""

    ## The consumer key. There is one of these which belongs
    ## to the app.
    CONSUMER_KEY = os.environ['CAPP_KEY']

    ## Consumer secret. There is one of these which belongs
    ## to the app.
    CONSUMER_SECRET = os.environ['CAPP_SECRET']

    ## This is genereated to help log in for one account. Once
    ## you have a token/secret for a user you dont need to do
    ## the oauth dance each time. Since we are only using one
    ## account, we just save the token/secret in the environment
    ## variables.
    ## USER_TOKEN is the access token on the site.
    ## USER_SECRET is the access token secret on the twitter site.
    ## Make sure
    USER_TOKEN = os.environ['CAPP_TOKEN']
    USER_SECRET = os.environ['CAPP_TOKEN_SECRET']

    def __init__(self):
        """Setup oath just for this account.

        The tokens and secrets are saved in environment
        variables. Save a reference to api for later.

        """
        auth = tweepy.OAuthHandler(
            TwitterPoster.CONSUMER_KEY,
            TwitterPoster.CONSUMER_SECRET)
        auth.set_access_token(
            TwitterPoster.USER_TOKEN,
            TwitterPoster.USER_SECRET)

        self.api = tweepy.API(auth)

    def post(self, status):
        """Post status to twitter."""
        self.api.update_status(status)
        print "Posted status to Twitter."


if __name__ == "__main__":
    twitter = TwitterPoster()
    twitter.post("Hello there!")
