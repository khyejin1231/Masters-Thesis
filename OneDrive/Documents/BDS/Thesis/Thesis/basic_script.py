# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:25:58 2022

@author: USER
"""
import twint
import nest_asyncio
import pandas as pd
import csv
nest_asyncio.apply()

c = twint.Config()
c.Username = "HiveOfJupiter"
c.Custom["tweet"] = ["id", "username", "tweet", "geo", "place", "retweet"]
#c.Custom["user"] = ["location"]
#c.Location = True
c.Limit = 20
c.Output = "tweets.csv"
c.Store_csv = True
twint.run.Search(c)


k = twint.Config()
k.Username = "HiveOfJupiter"
c.Custom['user'] = ["id", "username", "location", "bio", "likes", "tweets"]
k.Output = "user.csv"
k.Store_csv = True
twint.run.Lookup(k)


Tweets_df = pd.read_csv("tweets.csv")
User_df = pd.read_csv("user.csv")
