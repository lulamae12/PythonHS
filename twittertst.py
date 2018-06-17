from credentials import *
Import tweepy
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
text2Tweet = (input('enter text to tweet:'))
print("I have just tweeted:",text2Tweet)
api.update_status(text2Tweet)
