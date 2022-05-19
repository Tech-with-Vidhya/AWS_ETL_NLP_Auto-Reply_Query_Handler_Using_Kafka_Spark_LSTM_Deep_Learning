

from tweepy import Stream
import time

from .TwitterAuth import TwitterAuth
from .TweetsListener import TweetsListener
from .References import References


class TwitterStreamer(References):

    """SET UP STREAMER"""
    def __init__(self, producer):
        self.twitterAuth = TwitterAuth()
        self.producer = producer

    def stream_tweets(self):
        """Stream through tweets"""

        while True:
            try:
                listener = TweetsListener(self.producer, self.TOPIC_NAME)
                auth = self.twitterAuth.authenticateTwitterApp()
                stream = Stream(auth, listener)
                stream.filter(track=[self.TRACK_TWEET], stall_warnings=True, languages= ["en"])
            except Exception as e:
                print(e)
                print('Disconnected...')
                time.sleep(5)
                continue
