"""This file has to do with loading the data that has been pickled as preprocessing
the data into a train test split"""
#pylint: disable=C0103
#pylint: disable=C0301
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

def preprocess(LeagueFile="LeagueOfLegendsClusteringDataSet.pickle"):
    """
        this function takes a pre-made dataSet (by default LeagueOfLegendsClusteringDataSet.pickle)
        and performs a number of preprocessing steps:
            -- splits into training/testing sets (10% testing)
            -- selects/keeps most helpful features by dimensionality reductiong

        after this, the feaures and labels are put into numpy arrays, which play nice with sklearn functions

        4 objects are returned:
            -- training/testing features
            -- training/testing labels

    """
    pickleIn = open(LeagueFile, "rb")
    dataSet = pickle.load(pickleIn)

    dataSetFeatures = dataSet[["p1_GoldDiff",
                               "p1_Levels",
                               "p1_minionsKilled",
                               "p1_jungleMinionsKilled",
                               "p1_ChampionId"]]

    dataSetLabels = dataSet["p1_items"]

    sums = []
    for label in dataSetLabels:
        sums.append(sum(label))
    dataSetLabels = pd.DataFrame(sums)

    dataSetFeatures = dataSetFeatures.values
    dataSetLabels = dataSetLabels.values

    features_train, features_test, labels_train, labels_test = train_test_split(dataSetFeatures, dataSetLabels, test_size=0.1, random_state=42)

    print("no. of training points:", len(labels_train))
    print("no. of testing points:", len(labels_test))

    return features_train, features_test, labels_train, labels_test

# preprocess(LeagueFile="LeagueOfLegendsClusteringDataSet.pickle")
