import tweepy
from textblob import TextBlob

# Twitter API info
consumer_key = 
consumer_secret = 

access_token = 
access_token_secret = 
#---------------------------------

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('paladins')


for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
