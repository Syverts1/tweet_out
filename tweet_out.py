
# coding: utf-8

# In[1]:


import time
# Dependencies
import tweepy
import json

# Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[2]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[ ]:


i = 1
while(True):
    api.update_status("Tweet" + str(i))
    time.sleep(60)
    i = i +1
    if i == 5:
        break
        

