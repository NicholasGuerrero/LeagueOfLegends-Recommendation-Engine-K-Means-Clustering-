"""This file contains all functions that find or analyze timestamps from a match."""

def findTimestamp(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total items at each frame for the participantId.
    Example: findItems(match, participantId) -> [3303, 2010, 2010, 3340, 2010 ... nth frame]
    """

    timstamps = []
    for frame in match["timeline"]["frames"]:
        timstamps.append(frame["timestamp"])

    return timstamps
