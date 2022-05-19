# AWS_ETL_NLP_Auto-Reply_Query_Handler_Using_Kafka_Spark_LSTM_Deep_Learning

<h3><b><u>Introduction:</u></b></h3>

This project covers the end to end implementation of deplying a Auto-Reply Twitter Handler that replies to query-related tweets with a trackable ticket ID generated based on the query category predicted using NLP Long Short-Term Memory (LSTM) deep learning model.

Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on enabling computers to interpret text and spoken words in the same manner that humans do. Several NLP jobs helpthe computer understand what it imbibes by breaking down human text in ways that make sense.

One such task is social media sentiment analysis, which obtains hidden data insights from social mediaplatforms. Natural language processing (NLP) has become an indispensable commercial tool. Sentiment Analysis extracts attitudes and emotions in reaction to products, promotions, and events by analyzing the language used in social media postings, comments, and reviews. Companies may utilize this data for various purposes, including product design, customer service, and advertising campaigns. These tools can be clubbed with NER (named entity recognition), a technique for recognizing words or sentences asvaluable entities. The whole process can be automated and deployed on the cloud using data ingestionand streaming services with distributed processing.

The objective of this Twitter Support project is to listen to live tweets with required tags and publish them to a Kafka topic which will be consumed using Spark Stream and passed through an NLP pipeline for further processing and replying. The tweets will then be classified based on sentiment and query category using machine learning models like LSTM before responding to them with a custom ticked ID using Flaskand tweepy API.

This project automatically replies to query-related tweets with a trackable ticket ID generated based on the query category predicted using deep learning models. The whole process is automated with tweepy API and Big Data techniques with final deployment on AWS.

<h3><b><u>Dataset:</u></b></h3>

<h3><a href="https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment" style="color: blue"><b><u>US Airlines Tweets Dataset</u></b></a></h3>

For the training purposes in this project, we have used an “airline tweets” dataset, which includes necessary fields like airline names as tags, actual text, sentiment class, i.e., positive, negative, or neutraland a topic class which can be one of these:

1. Baggage Issue
2. Customer Experience
3. Delay and Customer Service
4. Extra Charges
5. Online Booking
6. Reschedule and Refund
7. Reservation Issue
8. Seating Preferences

<h3><b><u>Project Implementation Steps:</u></b></h3>

1. Data Exploration and Analysis
2. Data Pre-processing (Tokenisation, Stop Words Removal, Lemmatization, Word Embeddings)
3. Training a Sequence Model with LSTM for Sentiment Analysis
4. Topic Labelling using Latent Dirichlet Allocation (LDA)
5. Training a Sequence Model with LSTM for Topic Classification
6. Extracting the Named Entity
7. Model Evaluation and Validation
8. Model Performance Metrics Measures
9. Saving the Finalized Models
10. Sink Enriched Data to a Parquet File
11. Sending Replies to the Tweet using Flask and Tweepy

<h3><b><u>Tools & Technologies:</u></b></h3>

Python, Confluent Kafka, Spark, os, pandas, numpy, matplotlib, nltk, pyspark, tweepy, Flask, spacy, kafka, sklearn, tensorflow, keras, AWS ECR, AWS EC2, boto3, AWS CLI, AWS IAM

<h3><b><u>References:</u></b></h3>

This project is referenced and inspired from ProjectPro list of project ideas.

<h4><a href="https://www.projectpro.io/project-use-case/twitter-kafka-spark-streaming-python" style="color: blue"><b><u>US Airlines Tweets Dataset</u></b></a></h4>
