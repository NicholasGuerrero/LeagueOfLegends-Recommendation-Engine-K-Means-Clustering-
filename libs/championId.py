"""This file contains all functions that find or analyze a championId from a match."""

def findChampionId(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        Integer: The championId the participant played during the match. Valid outputs:
            125, 132, 121, 15, 16
    """

    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    for participant in match["participants"]:
        if participant["participantId"] == participantId:
            championId = participant["championId"]
            return championId
