"""This is where it all starts to create the random forests model."""
#pylint: disable=C0103
from libs import database
from libs import dataframes
import pandas as pd

def main():
    "This is the main function. It all starts here."

    matchesDatabase = database.connect("noschemas")
    matches = matchesDatabase.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"}, limit=3)

    dataSetPlaceholder = pd.DataFrame()
    for leagueOfLegendsMatch in matches:

        goldDeltas = dataframes.goldDeltaDataFrame(leagueOfLegendsMatch)
        levels = dataframes.levelsDataFrame(leagueOfLegendsMatch)
        minionsKilled = dataframes.minionsKilledDataFrame(leagueOfLegendsMatch)
        jungleMinionsKilled = dataframes.jungleMinionsKilledDataFrame(leagueOfLegendsMatch)
        championIds = dataframes.championIdDataFrame(leagueOfLegendsMatch)

        dataFrames = pd.concat([goldDeltas,
                                levels,
                                minionsKilled,
                                jungleMinionsKilled,
                                championIds], axis=1)

        dataSet = dataSetPlaceholder.append(dataFrames, ignore_index=True)

    dataSet.dropna(inplace=True)
    dataSet.reset_index(inplace=True)
    return dataSet

if __name__ == "__main__":
    main()
