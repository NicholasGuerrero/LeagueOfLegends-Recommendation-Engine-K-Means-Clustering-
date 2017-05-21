"""This file contains all functions that find or analyze gold values from a match."""
import libs.position

def findTotalGold(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total gold at each frame for the participantId.
    Example: createGoldByFrameMatrix(match, participantId) -> [500, 1000, 1500, 2000, ... nth frame]
    """
    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    participantTotalGold = []

    for frame in match["timeline"]["frames"]:
        for playerId, playerFrame in frame["participantFrames"].items():
            if int(playerId) == participantId:
                participantTotalGold.append(playerFrame["totalGold"])

    return participantTotalGold

def findGoldDeltas(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total gold difference at each frame between participantId
              and their lane opponnent.
    Example: findGoldDeltas(match, participantId) -> [0, 50, -20, 30, ... nth frame]
    """

    opponentId = libs.position.findLaneOpponentParticipantId(match, participantId)

    participantTotalGold = findTotalGold(match, participantId)
    laneOpponentTotalGold = findTotalGold(match, opponentId)

    totalGoldDeltas = [(participantTotalGold[i] - laneOpponentTotalGold[i]) \
     for i in range(0, len(participantTotalGold))]

    return totalGoldDeltas
