import numpy as np
import pandas as pd
import pprint
from pymongo import MongoClient


client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')

db = client['heroku_0dkc9rh7']

matches = db['noschemas']

projection = {"participants" : 1, '_id' : 0}

cursor = matches.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"}, limit = 5)
#cursor = matches.find({"matchId": 2398848900}, limit = 1)

##Lists
timestamps = []
matchIds = []
championIds = []

##Grabbing the data from Mongo and appending to Lists
for doc in cursor:
    for timestamp in doc['timeline']['frames']:
        timestamps.append(timestamp['timestamp'])
        matchIds.append(doc['matchId'])
        for participants in doc['participants']:
            championIds.append(participants['championId'])

##Player ChampionIds(1-10) Field
df_championIds = pd.DataFrame(championIds)
df_championIds = pd.DataFrame(np.reshape(df_championIds.values, (len(df_championIds)/10,10)), columns = ['participant_1_champ','participant_2_champ','participant_3_champ','participant_4_champ','participant_5_champ','participant_6_champ','participant_7_champ','participant_8_champ','participant_9_champ','participant_10_champ'])

##Timestamp Field
df_timestamps = pd.DataFrame(timestamps, columns = ['timestamp(ms)'])

##Changes the floats in the list in matchIds to integer values
for _ in range(0, len(matchIds)):
    matchIds[_] = int(matchIds[_])
    
##MatchIds Field
df_matchIds = pd.DataFrame(matchIds, columns = ['matchId'])

##Data Set
League_Data_Set = pd.concat([df_matchIds, df_timestamps, df_championIds], axis = 1)


