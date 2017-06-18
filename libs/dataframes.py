"""This file contains all functions that create dataframes."""
from libs import gold
from libs import championId as champIdLib
from libs import resources
import pandas as pd
import numpy as np

def goldDeltaDataFrame(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        DataFrame: The total gold difference at each frame between participants
        and their lane opponnents.
    Example:
                       p1_GoldDiff  p2_GoldDiff  p3_GoldDiff  p4_GoldDiff  p5_GoldDiff /
            0             0            0            0            0            0
            1             0            0            0            0            0
            2            40            0           -3            0            0
            3            60         -125           -1            0         -131
            4           327         -156          -55          317          -83

                        p6_GoldDiff  p7_GoldDiff  p8_GoldDiff  p9_GoldDiff  p10_GoldDiff
            0             0            0            0            0             0
            1             0            0            0            0             0
            2             0            3            0            0           -40
            3           131            1            0          125           -60
            4            83           55         -317          156          -327
    """

    goldDeltas = []

    for participant in match["participants"]:
        goldDelta = gold.findGoldDeltas(match, participant["participantId"])
        goldDeltas.append(goldDelta)

    goldDeltas = pd.DataFrame(goldDeltas).T
    goldDeltas.columns = ["p1_GoldDiff",
                          "p2_GoldDiff",
                          "p3_GoldDiff",
                          "p4_GoldDiff",
                          "p5_GoldDiff",
                          "p6_GoldDiff",
                          "p7_GoldDiff",
                          "p8_GoldDiff",
                          "p9_GoldDiff",
                          "p10_GoldDiff"
                         ]

    return goldDeltas

def levelsDataFrame(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        DataFrame: The level of the participants at each frame.
    Example:
                        p1_Levels  p2_Levels  p3_Levels  p4_Levels  p5_Levels  p6_Levels  \
            0           1          1          1          1          1          1
            1           1          1          1          1          1          1
            2           1          1          1          2          1          1
            3           3          2          2          3          2          2
            4           4          3          3          4          4          4

                        p7_Levels  p8_Levels  p9_Levels  p10_Levels
            0           1          1          1           1
            1           1          1          1           1
            2           1          2          1           1
            3           2          3          2           3
            4           3          4          3           3
    """

    levels = []

    for participant in match["participants"]:
        level = resources.findLevels(match, participant["participantId"])
        levels.append(level)

    levels = pd.DataFrame(levels).T
    levels.columns = ["p1_Levels",
                      "p2_Levels",
                      "p3_Levels",
                      "p4_Levels",
                      "p5_Levels",
                      "p6_Levels",
                      "p7_Levels",
                      "p8_Levels",
                      "p9_Levels",
                      "p10_Levels"
                     ]

    return levels

def minionsKilledDataFrame(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        DataFrame: The minions killed by the participants at each frame.
    Example:
                    p1_minionsKilled  p2_minionsKilled  p3_minionsKilled  p4_minionsKilled  \
            0                  0                 0                 0                 0
            1                  0                 0                 0                 0
            2                  3                 0                 0                 0
            3                 15                 6                 3                 0
    """

    allMinionsKilled = []

    for participant in match["participants"]:
        minionsKilled = resources.findMinionsKilled(match, participant["participantId"])
        allMinionsKilled.append(minionsKilled)

    allMinionsKilled = pd.DataFrame(allMinionsKilled).T
    allMinionsKilled.columns = ["p1_minionsKilled",
                                "p2_minionsKilled",
                                "p3_minionsKilled",
                                "p4_minionsKilled",
                                "p5_minionsKilled",
                                "p6_minionsKilled",
                                "p7_minionsKilled",
                                "p8_minionsKilled",
                                "p9_minionsKilled",
                                "p10_minionsKilled"
                               ]

    return allMinionsKilled

def jungleMinionsKilledDataFrame(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        DataFrame: The jungle minions killed by the participants at each frame.
    Example:
                p1_jungleMinionsKilled  p2_jungleMinionsKilled  p3_jungleMinionsKilled  \
            0                        0                       0                       0
            1                        0                       0                       0
            2                        0                       0                       0
    """

    allJungleMinionsKilled = []

    for participant in match["participants"]:
        minionsKilled = resources.findJungleMinionsKilled(match, participant["participantId"])
        allJungleMinionsKilled.append(minionsKilled)

    allJungleMinionsKilled = pd.DataFrame(allJungleMinionsKilled).T
    allJungleMinionsKilled.columns = ["p1_jungleMinionsKilled",
                                      "p2_jungleMinionsKilled",
                                      "p3_jungleMinionsKilled",
                                      "p4_jungleMinionsKilled",
                                      "p5_jungleMinionsKilled",
                                      "p6_jungleMinionsKilled",
                                      "p7_jungleMinionsKilled",
                                      "p8_jungleMinionsKilled",
                                      "p9_jungleMinionsKilled",
                                      "p10_jungleMinionsKilled"
                                     ]

    return allJungleMinionsKilled

def championIdDataFrame(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        DataFrame: The champion played at each frame.
    Example:
    """

    championIds = {}

    for participant in match["participants"]:
        participantId = participant["participantId"]
        championIds["p%d_ChampionId" % participantId] = []
        # if participantId ==
        championId = champIdLib.findChampionId(match, participant["participantId"])
        for _ in range(0, len(match["timeline"]["frames"])):
            championIds["p%d_ChampionId" % participantId].append(championId)

    championIds = pd.DataFrame(championIds)

    return championIds
