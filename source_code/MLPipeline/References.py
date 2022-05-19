"""
    File Name : References.py
    File Description : References class for keeping the constants, tokens and reference path
"""

import os
import sys

class References:

    ROOT_DIR = ""
    ONE = 1
    ZERO = 0
    BATCH_SIZE_BINARY_EVALUATE = 32

    BINARY_INPUT_LEN = 32
    MAX_FEATURES_BINARY = 2000

    OUTPUT = "output/"
    INPUT = "input/"

    # The maximum number of words to be used. (most frequent)
    MAX_NB_WORDS = 50000
    # Max number of words in each complaint.
    MAX_SEQUENCE_LENGTH = 250
    # This is fixed. Embedding
    EMBEDDING_DIM = 100

    PIPE_EXECPTIONS = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    # Training data for NER
    TRAIN_DATA = [
        ("Walmart is a leading e-commerce company", {"entities": [(0, 7, "ORG")]}),
        ("I reached Chennai yesterday.", {"entities": [(19, 28, "GPE")]}),
        ("I recently ordered a book from Amazon", {"entities": [(24, 32, "ORG")]}),
        ("I was driving a BMW", {"entities": [(16, 19, "PRODUCT")]}),
        ("I ordered this from ShopClues", {"entities": [(20, 29, "ORG")]}),
        ("Fridge can be ordered in Amazon ", {"entities": [(0, 6, "PRODUCT")]}),
        ("I bought a new Washer", {"entities": [(16, 22, "PRODUCT")]}),
        ("I bought a old table", {"entities": [(16, 21, "PRODUCT")]}),
        ("I bought a fancy dress", {"entities": [(18, 23, "PRODUCT")]}),
        ("I rented a camera", {"entities": [(12, 18, "PRODUCT")]}),
        ("I rented a tent for our trip", {"entities": [(12, 16, "PRODUCT")]}),
        ("I rented a screwdriver from our neighbour", {"entities": [(12, 22, "PRODUCT")]}),
        ("I repaired my computer", {"entities": [(15, 23, "PRODUCT")]}),
        ("I got my clock fixed", {"entities": [(16, 21, "PRODUCT")]}),
        ("I got my truck fixed", {"entities": [(16, 21, "PRODUCT")]}),
        ("Flipkart started it's journey from zero", {"entities": [(0, 8, "ORG")]}),
        ("I recently ordered from Max", {"entities": [(24, 27, "ORG")]}),
        ("Flipkart is recognized as leader in market", {"entities": [(0, 8, "ORG")]}),
        ("Virgin America is recognized as leader in market", {"entities": [(0, 14, "ORG")]}),
        ("Virgin America is the best airline ever", {"entities": [(0, 14, "ORG")]}),
        ("I recently ordered from Swiggy", {"entities": [(24, 29, "ORG")]}),
        ("Projectpro_test is a great airline.", {"entities": [(0, 15, "ORG")]}),
        ("Projectpro_test is a great airline.", {"entities": [(0, 15, "ORG")]}),
        ("Projectpro_test is a great airline.", {"entities": [(0, 15, "ORG")]}),
        ("Projectpro_test is a great airline.", {"entities": [(0, 15, "ORG")]})
    ]

    #Insert your IP with Port 9092 Eg- "34.221.72.51:9092"
    BOOTSTRAP_SERVER = ""

    TOPIC_NAME = "tweet-data"

    SINK_TOPIC="sink-data"

    # PARC_PATH = "./parc_sample"

    # Insert your credentials for Tweet
    access_token = "1412669800707330048-Axh3xFxNAYbSt7t7XnBEW7QIprLk0y"
    access_secret = "Zrzl6n5pkGzgiSBesIOooGwVqW6AHCEXmGGRXUw1bgMmt"

    consumer_key = "PA4SD4sL3OK4RewfUGR5I58tj"
    consumer_secret = "reDTNpU61whECGlWrZn0WERs5s1O7EdBSB0TdsG7VEDuz1Ybzz"

    TRACK_TWEET = "projectpro_test"

    # api-endpoint
    #Insert your IP with Port 5000 Eg- "http://34.221.72.51:5000/"
    URL = ""
