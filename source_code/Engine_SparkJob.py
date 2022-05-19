import findspark
findspark.init()

#Tweet preprocessing and sentiment analysis
#Import the necessary packages
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json

from MLPipeline.BinaryInference import BinaryInference
from MLPipeline.MulticlassComplainInference import MulticlassComplainInference
from MLPipeline.NameEntityInference import NameEntitiesInference
from MLPipeline.RequestParams import RequestParams
from MLPipeline.References import References

class SparkJob(References):


    def check_complain(self, text):
        bi = BinaryInference()
        return str(bi.predict_complaint(text))



    def check_complain_type(self, text):
        multi = MulticlassComplainInference()
        return str(multi.predict_complaint_type(text))


    def get_name_entities(self, text):
        name_entity = NameEntitiesInference()
        return json.dumps(dict(name_entity.get_Entities(text)))


    def reply_to_tweet_u(self, tweetId, complain, complain_type, entities, user):
        request_reply = RequestParams()
        return str(request_reply.reply_to_tweet(tweetId, complain, complain_type, entities, user))


    def label_data(self, words):
        # complaint detection udf
        check_complain_udf = udf(self.check_complain, StringType())
        words = words.withColumn("complain", check_complain_udf(col("tweet")))

        words.printSchema()

        # complaint category udf
        check_complain_type_udf = udf(self.check_complain_type, StringType())
        words = words.withColumn("complain_type", check_complain_type_udf("tweet"))

        # entity detection udf
        get_name_entities_udf = udf(self.get_name_entities, StringType())
        words = words.withColumn("entities", get_name_entities_udf(col("tweet")))

        # reply to tweet and get ticketId
        reply_to_tweet_udf = udf(self.reply_to_tweet_u, StringType())
        words = words.withColumn("tickedId",
                                 reply_to_tweet_udf(col("tweet_id"), col("complain"), col("complain_type"), col("entities"),
                                                    col("user")))

        return words



    def init_job(self):
        try:

            # creating spark session
            spark = SparkSession.builder.appName('SampleTWEETOperation').getOrCreate()

            # createing spark streaming
            # read stream from kafka
            df = spark \
                .readStream \
                .format("kafka") \
                .option("kafka.bootstrap.servers", self.BOOTSTRAP_SERVER) \
                .option("subscribe", self.TOPIC_NAME) \
                .option("startingOffsets", "earliest") \
                .option("failOnDataLoss", "false") \
                .load()

            # Casting as JSON name
            lines = df.selectExpr("CAST(value AS STRING) as json")

            lines.printSchema()
            # Defining Schema for input
            jsonSchema = StructType([StructField("tweet", StringType(), True), StructField("user", StringType(), True),
                                     StructField("tweet_id", StringType(), True)])

            # Parsing and selecting the right column data
            lines = lines.withColumn("jsonData", from_json(col("json"), jsonSchema)) \
                .select("jsonData.*")

            lines.printSchema()
            # Enriching the data
            lines = self.label_data(lines)

            # Writing Stream to Parquet file
            query = lines.selectExpr("CAST(tickedId AS STRING) AS key", "to_json(struct(*)) AS value")\
                .writeStream.queryName("all_tweets20") \
                .outputMode("append").format("kafka") \
                .option("kafka.bootstrap.servers", self.BOOTSTRAP_SERVER) \
                .option("topic", self.SINK_TOPIC) \
                .option("checkpointLocation", "./check20") \
                .trigger(processingTime='30 seconds').start()

            query.awaitTermination()
        except Exception as e:
            print(e)


j = SparkJob()
j.init_job()

# ./lib/python3.7/site-packages/pyspark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2  ./code/testStream.py localhost 9999 --master local[*]

# ./lib/python3.7/site-packages/pyspark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --py-files ./modular/source/MLPipeline.zip  ./modular/source/Engine_SparkJob.py localhost 9999 --master local[*]

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --py-files MLPipeline.zip  Engine_SparkJob.py localhost 9999

# kafka-console-consumer.sh --topic tweet-data --bootstrap-server localhost:9092