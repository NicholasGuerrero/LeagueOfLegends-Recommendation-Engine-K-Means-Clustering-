"""This file contains all functions that find or analyze a participants resources
 from a match. """

def findLevels(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total levels at each frame for the participantId.
    Example: findLevels(match, participantId) -> [1, 1, 3, 4, ... nth frame]
    """

    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    participantLevels = []

    for frame in match["timeline"]["frames"]:
        for playerId, playerFrame in frame["participantFrames"].items():
            if int(playerId) == participantId:
                participantLevels.append(playerFrame["level"])

    return participantLevels

def findMinionsKilled(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total minions killed at each frame for the participantId.
    Example: findMinionsKilled(match, participantId) -> [1, 1, 3, 4, ... nth frame]
    """
    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    participantMinionsKilled = []

    for frame in match["timeline"]["frames"]:
        for playerId, playerFrame in frame["participantFrames"].items():
            if int(playerId) == participantId:
                participantMinionsKilled.append(playerFrame["minionsKilled"])

    return participantMinionsKilled

def findJungleMinionsKilled(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total jungle minions killed at each frame for the participantId.
    Example: findJungleMinionsKilled(match, participantId) -> [1, 1, 3, 4, ... nth frame]
    """
    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    participantJungleMinionsKilled = []

    for frame in match["timeline"]["frames"]:
        for playerId, playerFrame in frame["participantFrames"].items():
            if int(playerId) == participantId:
                participantJungleMinionsKilled.append(playerFrame["jungleMinionsKilled"])

    return participantJungleMinionsKilled
