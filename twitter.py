import tweepy
import os


class TwitterPoster():

    """Make it really easy to post to our twitter account."""

    CONSUMER_TOKEN = os.environ['CAPP_KEY']
    CONSUMER_SECRET = os.environ['CAPP_SECRET']

    USER_TOKEN = os.environ['CAPP_TOKEN']
    USER_SECRET = os.environ['CAPP_TOKEN_SECRET']

    def __init__(self):
        """Setup oath just for this account.

        The tokens and secrets are saved in environment
        variables. Save a reference to api for later.

        """
        auth = tweepy.OAuthHandler(
            TwitterPoster.CONSUMER_TOKEN,
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
