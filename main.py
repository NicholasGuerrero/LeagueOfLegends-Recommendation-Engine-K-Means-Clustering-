"""This is where it all starts to create the random forests model."""
from libs import database
from libs import dataframes
import pandas as pd

def main():
    "This is the main function. It all starts here."

    matches = database.connect("noschemas")
    # match = matches.find({"matchId":2398848900}, limit=1)[0]
    match = matches.find({"queueType": "TEAM_BUILDER_RANKED_SOLO"}, limit = 20)

    goldDeltas = dataframes.goldDeltaDataFrame(match)
    levels = dataframes.levelsDataFrame(match)
    minionsKilled = dataframes.minionsKilledDataFrame(match)
    jungleMinionsKilled = dataframes.jungleMinionsKilledDataFrame(match)

    dataSet = pd.concat([goldDeltas, levels, minionsKilled, jungleMinionsKilled], axis=1)
    print dataSet.describe()

if __name__ == "__main__":
    main()
