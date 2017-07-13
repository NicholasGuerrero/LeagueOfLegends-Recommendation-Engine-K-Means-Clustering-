"""This is where it all starts to create the K-Means Clustering model."""
#pylint: disable=C0103
from libs import database
from libs import dataframes
from libs import items
from libs import matchId
import pandas as pd
import pickle

def main():
    "This is the main function. It all starts here."

    matchesDatabase = database.connect("noschemas")
<<<<<<< HEAD
    matches = matchesDatabase.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"}, limit=2)
=======
    matches = matchesDatabase.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"})
>>>>>>> 3256574527b8444b44592ff3c0b43a9c1ced829b

    dataSet = pd.DataFrame()
    for leagueOfLegendsMatch in matches:

        matchIds = dataframes.matchIdsDataFrame(leagueOfLegendsMatch)
        timestamps = dataframes.timeStampDataFrame(leagueOfLegendsMatch)
        goldDeltas = dataframes.goldDeltaDataFrame(leagueOfLegendsMatch)
        levels = dataframes.levelsDataFrame(leagueOfLegendsMatch)
        minionsKilled = dataframes.minionsKilledDataFrame(leagueOfLegendsMatch)
        jungleMinionsKilled = dataframes.jungleMinionsKilledDataFrame(leagueOfLegendsMatch)
        championIds = dataframes.championIdDataFrame(leagueOfLegendsMatch)
        shopItems = dataframes.itemsDataFrame(leagueOfLegendsMatch)

        dataFrames = pd.concat([matchIds,
                                timestamps,
                                goldDeltas,
                                levels,
                                minionsKilled,
                                jungleMinionsKilled,
                                championIds,
                                shopItems], axis=1)

        dataSet = dataSet.append(dataFrames, ignore_index=True)

    dataSet.dropna(inplace=True)
    dataSet.reset_index(inplace=True, drop=True)
<<<<<<< HEAD
    print(dataSet[0:10])

    # pickleOut = open("LeagueOfLegendsClusteringDataSet.pickle", "wb")
    # pickle.dump(dataSet, pickleOut)
    # pickleOut.close()

=======

    pickleOut = open("LeagueOfLegendsClusteringDataSet.pickle", "wb")
    pickle.dump(dataSet, pickleOut)
    pickleOut.close()
>>>>>>> 3256574527b8444b44592ff3c0b43a9c1ced829b

if __name__ == "__main__":
    main()
