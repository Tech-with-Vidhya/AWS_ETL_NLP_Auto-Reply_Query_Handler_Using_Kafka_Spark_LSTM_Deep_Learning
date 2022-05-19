
# Send Tweets from twitter API
#Import necessary packages
import tweepy
from tweepy import OAuthHandler
import json
import random

from .References import References


class ReplyTweet(References):

    def __init__(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def sendReply(self, tweetId, user, text):
        try:
            text = "@" + user + " " + text
            print(text)
            self.api.update_status(text, int(tweetId))
            print("after reply")
            return True
        except Exception as e:
            print(e)
            return False

    def getReplyText(self, complain_type, ticketId):
        reply_txt = "Appologies for the inconvience cause. We are taking this via ticket id " + str(
            ticketId) + " and resolve asap. You can track the status at www.desyre.com"
        return reply_txt

    def reply_toTweet(self, tweetId, complain, complain_type, user):
        if bool(complain):
            ticketId = int(random.random() * 100000)
            txt = self.getReplyText(complain_type, ticketId)
            replied = self.sendReply(tweetId, user, txt)
        else:
            ticketId = ""
            replied = False
        return json.dumps({"replied": replied, "ticketId": ticketId})

