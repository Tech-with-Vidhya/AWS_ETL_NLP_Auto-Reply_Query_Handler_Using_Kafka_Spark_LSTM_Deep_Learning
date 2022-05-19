

from tweepy.streaming import StreamListener
import json

from .References import References

# Create a StreamListener instance
class TweetsListener(StreamListener):

    def __init__(self, producer, topic_name):
        self.producer = producer
        self.topic_name = topic_name

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print("new message")
            # if tweet is longer than 140 characters

            if "extended_tweet" in msg:
                # add at the end of each tweet "t_end"
                out_data = '{ "tweet":" ' +str(msg['extended_tweet']['full_text']).replace("\n"
                                                                                           ,"" ) +'","user":" ' +str \
                    (msg['user']['screen_name'] ) +'", "tweet_id":" ' +str(msg['id_str'] ) +'" }'
                self.producer.send(self.topic_name, str.encode(out_data))
            else:
                # add at the end of each tweet "t_end"
                out_data = '{ "tweet":" ' +str(msg['text']).replace("\n" ,"" ) +'","user":" ' +str \
                    (msg['user']['screen_name'] ) +'", "tweet_id":" ' +str(msg['id_str'] ) +'" }'
                self.producer.send(self.topic_name, str.encode(out_data))
            return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


    def on_error(self, status):
        print(status)
        return True

    def on_exception(self, exception):
        print(exception)
        return