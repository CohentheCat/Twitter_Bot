import searchApp_config as config
import tweepy
import time

bearer_token = config.bearerToken
consumer_key = config.apiKey
consumer_secret = config.apiSecret
access_token = config.accessToken
access_token_secret = config.accessSecretToken
user_id = config.user_id
#this constructs the client
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

tweets = client.get_users_tweets(user_id)
tweets_array = [tweet.text for tweet in tweets.data]

def translate(tweets_array):
    for tw in tweets_array:
        if "RT" in tw:
            pass
        else:
            original = tw
            rep = original.replace('l', '%temp%').replace('r', 'w').replace('%temp%', 'w')
            print("-" * len(rep))
            print()
            print(rep)
            client.create_tweet(text= rep)
            print()
            print("-" * len(rep))
            time.sleep(1800)

translate(tweets_array)