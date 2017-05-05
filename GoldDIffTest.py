import numpy as np
import pandas as pd
import pprint
from pymongo import MongoClient


##MongoDB Parameters
client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
db = client['heroku_0dkc9rh7']
matches = db['noschemas']
projection = {"participants" : 1, '_id' : 0}
#cursor = matches.find({"matchId": 2398848900}, limit = 1)
cursor = matches.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"})

##Lists
totalGold_1 = []
totalGold_2 = []
totalGold_3 = []
totalGold_4 = []
totalGold_5 = []
totalGold_6 = []
totalGold_7 = []
totalGold_8 = []
totalGold_9 = []
totalGold_10 = []

##Get Data
for doc in cursor:
    for frames in doc['timeline']['frames']:
        if 'events' in frames:
            for event in frames['events']:
                totalGold_1.append(frames['participantFrames']['1']['totalGold'])
                totalGold_2.append(frames['participantFrames']['2']['totalGold'])
                totalGold_3.append(frames['participantFrames']['3']['totalGold'])
                totalGold_4.append(frames['participantFrames']['4']['totalGold'])
                totalGold_5.append(frames['participantFrames']['5']['totalGold'])
                totalGold_6.append(frames['participantFrames']['6']['totalGold'])
                totalGold_7.append(frames['participantFrames']['7']['totalGold'])
                totalGold_8.append(frames['participantFrames']['8']['totalGold'])
                totalGold_9.append(frames['participantFrames']['9']['totalGold'])
                totalGold_10.append(frames['participantFrames']['10']['totalGold'])

        else:
            continue;

##CurrentGold for every Participant
df_TotalGold_P1 = pd.DataFrame(totalGold_1, columns = ['P1_TotalGold'])
df_TotalGold_P2 = pd.DataFrame(totalGold_2, columns = ['P2_TotalGold'])
df_TotalGold_P3 = pd.DataFrame(totalGold_3, columns = ['P3_TotalGold'])
df_TotalGold_P4 = pd.DataFrame(totalGold_4, columns = ['P4_TotalGold'])
df_TotalGold_P5 = pd.DataFrame(totalGold_5, columns = ['P5_TotalGold'])
df_TotalGold_P6 = pd.DataFrame(totalGold_6, columns = ['P6_TotalGold'])
df_TotalGold_P7 = pd.DataFrame(totalGold_7, columns = ['P7_TotalGold'])
df_TotalGold_P8 = pd.DataFrame(totalGold_8, columns = ['P8_TotalGold'])
df_TotalGold_P9 = pd.DataFrame(totalGold_9, columns = ['P9_TotalGold'])
df_TotalGold_P10 = pd.DataFrame(totalGold_10, columns = ['P10_TotalGold'])


df_TotalGolds = pd.concat([df_TotalGold_P1, df_TotalGold_P2, df_TotalGold_P3, df_TotalGold_P4, df_TotalGold_P5, df_TotalGold_P6, df_TotalGold_P7, df_TotalGold_P8, df_TotalGold_P9, df_TotalGold_P10], axis = 1) 

##Get the Role and Lane of Every Player

##MongoDB Parameters
client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
db = client['heroku_0dkc9rh7']
matches = db['noschemas']
projection = {"participants" : 1, '_id' : 0}
#cursor = matches.find({"matchId": 2398848900}, limit = 1)
cursor = matches.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"})

##Lists
lanes = []
roles = []
teamIds = []

##Get Data
for doc in cursor:
    for frames in doc['timeline']['frames']:
        if 'events' in frames:
            for event in frames['events']:
                for participant in doc['participants']:
                    roles.append(participant['timeline']['role'])
                    lanes.append(participant['timeline']['lane'])
                    teamIds.append(participant['teamId'])
        else:
            #print("You done goofed")
            continue;

##Roles
df_roles = pd.DataFrame(roles)
#df_roles = pd.DataFrame(np.reshape(df_roles.values, (len(df_roles) / 10, 10)), columns = ['participant_1_role','participant_2_role','participant_3_role','participant_4_role','participant_5_role','participant_6_role','participant_7_role','participant_8_role','participant_9_role','participant_10_role'])


##Lanes
df_lanes = pd.DataFrame(lanes)
#df_lanes = pd.DataFrame(np.reshape(df_lanes.values, (len(df_lanes) / 10, 10)), columns = ['participant_1_lane','participant_2_lane','participant_3_lane','participant_4_lane','participant_5_lane','participant_6_lane','participant_7_lane','participant_8_lane','participant_9_lane','participant_10_lane'])

##TeamId
df_teamId = pd.DataFrame(teamIds)
#df_teamId = pd.DataFrame(np.reshape(df_teamId.values, (len(df_teamId) / 10, 10)), columns = ['participant_1_teamId','participant_2_teamId','participant_3_teamId','participant_4_teamId','participant_5_teamId','participant_6_teamId','participant_7_teamId','participant_8_teamId','participant_9_teamId','participant_10_teamId'])

##Role_Lane
df_role_lane = pd.concat([df_roles, df_lanes], axis = 1)
df_role_lane.columns = ['Role','Lane']

#TestDataSet = pd.concat([df_TotalGolds, df_role_lane], axis = 1)

GoldDiff = pd.DataFrame(columns = ['TopGold_Diff','MidGold_Diff','ADCGold_Diff','SupportGold_Diff','JungleGold_Diff'])

TopGold_Diff_T100 = []
TopGold_Diff_T200 = []

MidGold_Diff_T100 = []
MidGold_Diff_T200 = []

ADCGold_Diff_T100 = []
ADCGold_Diff_T200 = []

SupportGold_Diff_T100 = []
SupportGold_Diff_T200 = []

JungleGold_Diff_T100 = []
JungleGold_Diff_T200 = []

##Find All Combinations of Role/Lane
RoleLane = []
for i in range(0, len(df_role_lane)):
    RoleLane.append(df_role_lane['Role'][i] + '_' + df_role_lane['Lane'][i])

df_RoleLane = pd.DataFrame(RoleLane)

df_roles = pd.DataFrame(np.reshape(df_roles.values, (len(df_roles) / 10, 10)), columns = ['participant_1_role','participant_2_role','participant_3_role','participant_4_role','participant_5_role','participant_6_role','participant_7_role','participant_8_role','participant_9_role','participant_10_role'])
df_lanes = pd.DataFrame(np.reshape(df_lanes.values, (len(df_lanes) / 10, 10)), columns = ['participant_1_lane','participant_2_lane','participant_3_lane','participant_4_lane','participant_5_lane','participant_6_lane','participant_7_lane','participant_8_lane','participant_9_lane','participant_10_lane'])
df_role_lane = pd.concat([df_roles, df_lanes], axis = 1)
df_role_lane.columns = ['Role','Lane']
TestDataSet = pd.concat([df_TotalGolds, df_role_lane], axis = 1)

##for i in range(0, len(TestDataSet)):
##    if TestDataSet['participant_1_role'][i] == 'DUO' and TestDataSet['participant_1_lane'][i] == 'MIDDLE':
##        i
##    else:
##        TopGold_Diff_T100.append(TestDataSet['P1_TotalGold'][i]-TestDataSet['P6_TotalGold'][i])

