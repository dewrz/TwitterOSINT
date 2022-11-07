import tweepy
import config
import pandas as pd
import csv

#GET CLIENT AUTHENTICATION

def getClient():
    client = tweepy.Client(bearer_token= config.BEARER_TOKEN,
                        consumer_key = config.API_KEY,
                        consumer_secret = config.API_KEY_SECRET,
                        access_token = config.ACCESS_TOKEN,
                        access_token_secret = config.ACCESS_TOKEN_SECRET)
    return client

# DEFINE FUNCTION TO PARSE DATA

def getUserInfo():
    client = getClient()
    user = client.get_user(username='evan_ottinger')
    return user.data.id

user = getUserInfo()

def getUserIntel():
    client = getClient()
    intel = client.get_users_tweets(id=user,
                                    tweet_fields=['created_at','text', 'geo', 'source'],
                                    max_results=100)
    return intel

intel = getUserIntel()

# CREATE DF
recon_data = []

for tweet in intel.data:
    recon_data.append(tweet)

recon_df = pd.DataFrame(recon_data)
recon_df.to_csv("recon.csv", header=None, index=None, sep=',', mode='w')

# SCAN CSV FOR KEYWORDS

words_to_find = ['vacation', 'not home', 'the key is under the mat']

with open('recon.csv', 'r') as reader:
     recon_reader = csv.DictReader(reader)
     if words_to_find is recon_reader:
         print("We're in the money!")
     else:
         print("We're still broke!")





