#!/usr/bin/env python
# coding: utf-8

# # **First**
# #### Import the libraries that you need to parse the tweet data from twitter

# In[3]:


# Import the libraries you need

get_ipython().system('pip install git+https://github.com/tweepy/tweepy.git')
import tweepy as tw
from tweepy import OAuthHandler
import pandas as pd

# API set-ups for the use of Twitter API
# Insert your keys and tokens below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

tweets = [] # create an empty list to contain the tweets data you parsed

count = 1 # number of iteration

for tweet in tw.Cursor(api.search, q="sexual harrasment", count=200, since='2020-06-06').items(400):
    
    print(count)
    count += 1
    
    try:
        data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
        data = tuple(data)
        tweets.append(data)
        
    except tw.TweepError as e:
        print(e.reason)
        continue
        
    except StopIteration:
        break
        
result_df = pd.DataFrame(tweets)
result_df.to_csv('sexualHarrasment.csv', index=None) # Save your dataframe into csv format
        


# In[ ]:




