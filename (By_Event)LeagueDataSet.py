import numpy as np
import pandas as pd
import pprint
from pymongo import MongoClient

##Data Structure of the Data Set
def DataStructure():
    
    ##MongoDB Parameters
    client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
    db = client['heroku_0dkc9rh7']
    matches = db['noschemas']
    projection = {"participants" : 1, '_id' : 0}
    cursor = matches.find({"matchId": 2398848900}, limit = 1)
    
    ##Lists
    matchIds = []
    events_time = []
    eventTypes = []
    
    ##Grab Data
    for doc in cursor:
        for frames in doc['timeline']['frames']:
            if 'events' in frames:
                for event in frames['events']:
                        matchIds.append(doc['matchId'])
                        events_time.append(event['timestamp'])
                        eventTypes.append(event['eventType'])

    ##MatchIDs
    for _ in range(0, len(matchIds)):
        matchIds[_] = int(matchIds[_])
        
    df_matchIds = pd.DataFrame(matchIds, columns = ['matchId'])
    df_events_time = pd.DataFrame(events_time, columns = ['timestamp(ms)'])
    df_eventTypes = pd.DataFrame(eventTypes, columns = ['eventType'])

    ##Final Data Set
    LeagueDataSet = pd.concat([df_matchIds, df_events_time, df_eventTypes], axis = 1)
    return(LeagueDataSet)

##TOTAL GOLD DATAFRAME
def get_totalGold():

    ##MongoDB Parameters
    client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
    db = client['heroku_0dkc9rh7']
    matches = db['noschemas']
    projection = {"participants" : 1, '_id' : 0}
    cursor = matches.find({"matchId": 2398848900}, limit = 1)    
    
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
    
    levels_1 = []
    levels_2 = []
    levels_3 = []
    levels_4 = []
    levels_5 = []
    levels_6 = []
    levels_7 = []
    levels_8 = []
    levels_9 = []
    levels_10 = []
    
    minionsKilled_1 = []
    minionsKilled_2 = []
    minionsKilled_3 = []
    minionsKilled_4 = []
    minionsKilled_5 = []
    minionsKilled_6 = []
    minionsKilled_7 = []
    minionsKilled_8 = []
    minionsKilled_9 = []
    minionsKilled_10 = []
    
    jungleMinionsKilled_1 = []
    jungleMinionsKilled_2 = []
    jungleMinionsKilled_3 = []
    jungleMinionsKilled_4 = []
    jungleMinionsKilled_5 = []
    jungleMinionsKilled_6 = []
    jungleMinionsKilled_7 = []
    jungleMinionsKilled_8 = []
    jungleMinionsKilled_9 = []
    jungleMinionsKilled_10 = []
    
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

                    levels_1.append(frames['participantFrames']['1']['level'])
                    levels_2.append(frames['participantFrames']['2']['level'])
                    levels_3.append(frames['participantFrames']['3']['level'])
                    levels_4.append(frames['participantFrames']['4']['level'])
                    levels_5.append(frames['participantFrames']['5']['level'])
                    levels_6.append(frames['participantFrames']['6']['level'])
                    levels_7.append(frames['participantFrames']['7']['level'])
                    levels_8.append(frames['participantFrames']['8']['level'])
                    levels_9.append(frames['participantFrames']['9']['level'])
                    levels_10.append(frames['participantFrames']['10']['level'])

                    minionsKilled_1.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_2.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_3.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_4.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_5.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_6.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_7.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_8.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_9.append(frames['participantFrames']['1']['minionsKilled'])
                    minionsKilled_10.append(frames['participantFrames']['1']['minionsKilled'])

                    jungleMinionsKilled_1.append(frames['participantFrames']['1']['jungleMinionsKilled'])
                    jungleMinionsKilled_2.append(frames['participantFrames']['2']['jungleMinionsKilled'])
                    jungleMinionsKilled_3.append(frames['participantFrames']['3']['jungleMinionsKilled'])
                    jungleMinionsKilled_4.append(frames['participantFrames']['4']['jungleMinionsKilled'])
                    jungleMinionsKilled_5.append(frames['participantFrames']['5']['jungleMinionsKilled'])
                    jungleMinionsKilled_6.append(frames['participantFrames']['6']['jungleMinionsKilled'])
                    jungleMinionsKilled_7.append(frames['participantFrames']['7']['jungleMinionsKilled'])
                    jungleMinionsKilled_8.append(frames['participantFrames']['8']['jungleMinionsKilled'])
                    jungleMinionsKilled_9.append(frames['participantFrames']['9']['jungleMinionsKilled'])
                    jungleMinionsKilled_10.append(frames['participantFrames']['10']['jungleMinionsKilled'])

            else:
                print("You done goofed")

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

    df_levels_P1 = pd.DataFrame(totalGold_1, columns = ['P1_Levels'])
    df_levels_P2 = pd.DataFrame(totalGold_2, columns = ['P2_Levels'])
    df_levels_P3 = pd.DataFrame(totalGold_3, columns = ['P3_Levels'])
    df_levels_P4 = pd.DataFrame(totalGold_4, columns = ['P4_Levels'])
    df_levels_P5 = pd.DataFrame(totalGold_5, columns = ['P5_Levels'])
    df_levels_P6 = pd.DataFrame(totalGold_6, columns = ['P6_Levels'])
    df_levels_P7 = pd.DataFrame(totalGold_7, columns = ['P7_Levels'])
    df_levels_P8 = pd.DataFrame(totalGold_8, columns = ['P8_Levels'])
    df_levels_P9 = pd.DataFrame(totalGold_9, columns = ['P9_Levels'])
    df_levels_P10 = pd.DataFrame(totalGold_10, columns = ['P10_Levels'])

    df_minionsKilled_P1 = pd.DataFrame(totalGold_1, columns = ['P1_minionsKilled'])
    df_minionsKilled_P2 = pd.DataFrame(totalGold_2, columns = ['P2_minionsKilled'])
    df_minionsKilled_P3 = pd.DataFrame(totalGold_3, columns = ['P3_minionsKilled'])
    df_minionsKilled_P4 = pd.DataFrame(totalGold_4, columns = ['P4_minionsKilled'])
    df_minionsKilled_P5 = pd.DataFrame(totalGold_5, columns = ['P5_minionsKilled'])
    df_minionsKilled_P6 = pd.DataFrame(totalGold_6, columns = ['P6_minionsKilled'])
    df_minionsKilled_P7 = pd.DataFrame(totalGold_7, columns = ['P7_minionsKilled'])
    df_minionsKilled_P8 = pd.DataFrame(totalGold_8, columns = ['P8_minionsKilled'])
    df_minionsKilled_P9 = pd.DataFrame(totalGold_9, columns = ['P9_minionsKilled'])
    df_minionsKilled_P10 = pd.DataFrame(totalGold_10, columns = ['P10_minionsKilled'])    

    df_jungleMinionsKilled_P1 = pd.DataFrame(totalGold_1, columns = ['P1_jungleMinionsKilled'])
    df_jungleMinionsKilled_P2 = pd.DataFrame(totalGold_2, columns = ['P2_jungleMinionsKilled'])
    df_jungleMinionsKilled_P3 = pd.DataFrame(totalGold_3, columns = ['P3_jungleMinionsKilled'])
    df_jungleMinionsKilled_P4 = pd.DataFrame(totalGold_4, columns = ['P4_jungleMinionsKilled'])
    df_jungleMinionsKilled_P5 = pd.DataFrame(totalGold_5, columns = ['P5_jungleMinionsKilled'])
    df_jungleMinionsKilled_P6 = pd.DataFrame(totalGold_6, columns = ['P6_jungleMinionsKilled'])
    df_jungleMinionsKilled_P7 = pd.DataFrame(totalGold_7, columns = ['P7_jungleMinionsKilled'])
    df_jungleMinionsKilled_P8 = pd.DataFrame(totalGold_8, columns = ['P8_jungleMinionsKilled'])
    df_jungleMinionsKilled_P9 = pd.DataFrame(totalGold_9, columns = ['P9_jungleMinionsKilled'])
    df_jungleMinionsKilled_P10 = pd.DataFrame(totalGold_10, columns = ['jungleMinionsKilled'])    
    
    ##All current gold DataFrames
    df_TotalGolds = pd.concat([df_TotalGold_P1, df_TotalGold_P2, df_TotalGold_P3, df_TotalGold_P4, df_TotalGold_P5, df_TotalGold_P6, df_TotalGold_P7, df_TotalGold_P8, df_TotalGold_P9, df_TotalGold_P10], axis = 1) 
    df_levels = pd.concat([df_levels_P1, df_levels_P2, df_levels_P3, df_levels_P4, df_levels_P5, df_levels_P6, df_levels_P7, df_levels_P8, df_levels_P9, df_levels_P10], axis =1)
    df_minionsKilled = pd.concat([df_minionsKilled_P1, df_minionsKilled_P2, df_minionsKilled_P3, df_minionsKilled_P4, df_minionsKilled_P5, df_minionsKilled_P6, df_minionsKilled_P7, df_minionsKilled_P8, df_minionsKilled_P9, df_minionsKilled_P10], axis = 1)
    df_jungleMinionsKilled = pd.concat([df_jungleMinionsKilled_P1,df_jungleMinionsKilled_P2, df_jungleMinionsKilled_P3, df_jungleMinionsKilled_P4, df_jungleMinionsKilled_P5, df_jungleMinionsKilled_P6, df_jungleMinionsKilled_P7, df_jungleMinionsKilled_P8, df_jungleMinionsKilled_P9, df_jungleMinionsKilled_P10], axis = 1)

    df_Totals = pd.concat([df_TotalGolds, df_levels, df_minionsKilled, df_jungleMinionsKilled], axis = 1)
    return(df_Totals)

##CURRENT GOLD DATAFRAME
def get_currentGold():

    ##MongoDB Parameters
    client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
    db = client['heroku_0dkc9rh7']
    matches = db['noschemas']
    projection = {"participants" : 1, '_id' : 0}
    cursor = matches.find({"matchId": 2398848900}, limit = 1)
    
    ##Lists
    currentGold_1 = []
    currentGold_2 = []
    currentGold_3 = []
    currentGold_4 = []
    currentGold_5 = []
    currentGold_6 = []
    currentGold_7 = []
    currentGold_8 = []
    currentGold_9 = []
    currentGold_10 = []

    ##Get Data
    for doc in cursor:
        for frames in doc['timeline']['frames']:
            if 'events' in frames:
                for event in frames['events']:
                    currentGold_1.append(frames['participantFrames']['1']['currentGold'])
                    currentGold_2.append(frames['participantFrames']['2']['currentGold'])
                    currentGold_3.append(frames['participantFrames']['3']['currentGold'])
                    currentGold_4.append(frames['participantFrames']['4']['currentGold'])
                    currentGold_5.append(frames['participantFrames']['5']['currentGold'])
                    currentGold_6.append(frames['participantFrames']['6']['currentGold'])
                    currentGold_7.append(frames['participantFrames']['7']['currentGold'])
                    currentGold_8.append(frames['participantFrames']['8']['currentGold'])
                    currentGold_9.append(frames['participantFrames']['9']['currentGold'])
                    currentGold_10.append(frames['participantFrames']['10']['currentGold'])
            else:
                print("You done goofed")

    ##CurrentGold for every Participant
    df_currentGold_P1 = pd.DataFrame(currentGold_1, columns = ['P1_CurrGold'])
    df_currentGold_P2 = pd.DataFrame(currentGold_2, columns = ['P2_CurrGold'])
    df_currentGold_P3 = pd.DataFrame(currentGold_3, columns = ['P3_CurrGold'])
    df_currentGold_P4 = pd.DataFrame(currentGold_4, columns = ['P4_CurrGold'])
    df_currentGold_P5 = pd.DataFrame(currentGold_5, columns = ['P5_CurrGold'])
    df_currentGold_P6 = pd.DataFrame(currentGold_6, columns = ['P6_CurrGold'])
    df_currentGold_P7 = pd.DataFrame(currentGold_7, columns = ['P7_CurrGold'])
    df_currentGold_P8 = pd.DataFrame(currentGold_8, columns = ['P8_CurrGold'])
    df_currentGold_P9 = pd.DataFrame(currentGold_9, columns = ['P9_CurrGold'])
    df_currentGold_P10 = pd.DataFrame(currentGold_10, columns = ['P10_CurrGold'])

    ##All current gold DataFrames
    df_currentGolds = pd.concat([df_currentGold_P1, df_currentGold_P2, df_currentGold_P3, df_currentGold_P4, df_currentGold_P5, df_currentGold_P6, df_currentGold_P7, df_currentGold_P8, df_currentGold_P9, df_currentGold_P10], axis = 1) 

    return(df_currentGolds)

##Get the Role and Lane of Every Player
def get_role_lane():

    ##MongoDB Parameters
    client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
    db = client['heroku_0dkc9rh7']
    matches = db['noschemas']
    projection = {"participants" : 1, '_id' : 0}
    ##cursor = matches.find({"matchId": 2398848900}, limit = 1)
    cursor = matches.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"}, limit = 5)

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
                print("You done goofed")

    ##Roles
    df_roles = pd.DataFrame(roles)
    df_roles = pd.DataFrame(np.reshape(df_roles.values, (len(df_roles) / 10, 10)), columns = ['participant_1_role','participant_2_role','participant_3_role','participant_4_role','participant_5_role','participant_6_role','participant_7_role','participant_8_role','participant_9_role','participant_10_role'])


    ##Lanes
    df_lanes = pd.DataFrame(lanes)
    df_lanes = pd.DataFrame(np.reshape(df_lanes.values, (len(df_lanes) / 10, 10)), columns = ['participant_1_lane','participant_2_lane','participant_3_lane','participant_4_lane','participant_5_lane','participant_6_lane','participant_7_lane','participant_8_lane','participant_9_lane','participant_10_lane'])

    ##TeamId
    df_teamId = pd.DataFrame(teamIds)
    df_teamId = pd.DataFrame(np.reshape(df_teamId.values, (len(df_teamId) / 10, 10)), columns = ['participant_1_teamId','participant_2_teamId','participant_3_teamId','participant_4_teamId','participant_5_teamId','participant_6_teamId','participant_7_teamId','participant_8_teamId','participant_9_teamId','participant_10_teamId'])
    
    ##Role_Lane
    df_role_lane = pd.concat([df_roles, df_lanes, df_teamId], axis = 1)

    return(df_role_lane)
    
##Get the ChampionId
def get_championId():

    ##MongoDB Parameters
    client = MongoClient('mongodb://nick:jewel@ds161630.mlab.com:61630/heroku_0dkc9rh7')
    db = client['heroku_0dkc9rh7']
    matches = db['noschemas']
    projection = {"participants" : 1, '_id' : 0}
    cursor = matches.find({"matchId": 2398848900}, limit = 1)

    championIds = []

    for doc in cursor:
        for frames in doc['timeline']['frames']:
            if 'events' in frames:
                for event in frames['events']:
                    for champid in doc['participants']:
                        championIds.append(champid['championId'])
                    
            else:
                print("You done goofed")

    df_championId = pd.DataFrame(championIds)
    df_championId = pd.DataFrame(np.reshape(df_championId.values, (len(df_championId) / 10, 10)), columns = ['ChampionId_P1','ChampionId_P2','ChampionId_P3','ChampionId_P4','ChampionId_P5','ChampionId_P6','ChampionId_P7','ChampionId_P8','ChampionId_P9','ChampionId_P10'])
    
    return(df_championId)















