


from kafka import KafkaProducer
from MLPipeline.TwitterStreamer import TwitterStreamer

from MLPipeline.References import References

class Engine_kafka(References):

    def __init__(self):
        """ Setup Kafka Producer"""
        self.producer = KafkaProducer(bootstrap_servers=self.BOOTSTRAP_SERVER)  # Same port as your Kafka server

    def stream_tweets_kafka(self):
        """Stream Through Tweets"""
        TS = TwitterStreamer(self.producer)
        TS.stream_tweets()



e = Engine_kafka()
e.stream_tweets_kafka()

