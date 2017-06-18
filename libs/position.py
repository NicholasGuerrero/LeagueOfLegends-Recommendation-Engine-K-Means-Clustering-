"""All functions that relate to the position of a participantId."""

def findPositions(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        String: The position the participant played during the match. Valid outputs:
            "TOP", "MIDDLE", "ADC", "SUPPORT", "JUNGLE",
             If the position cannot be determined then the function returns False
        """

    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    for participant in match["participants"]:
        role = participant["timeline"]["role"]
        lane = participant["timeline"]["lane"]
        stats = participant["stats"]["minionsKilled"]
        matchDuration = match["matchDuration"]
        if participant["participantId"] == participantId:
            if role == "NONE" and lane == "JUNGLE":
                return "JUNGLE"
            elif role == "SOLO" and lane == "TOP":
                return "TOP"
            elif role == "DUO_CARRY" and lane == "BOTTOM":
                return "ADC"
            elif role == "DUO_SUPPORT" and lane == "BOTTOM":
                return "SUPPORT"
            elif role == "SOLO" and lane == "MIDDLE":
                return "MIDDLE"
            elif role == "DUO" and lane == "BOTTOM":
                if (stats / (matchDuration / 60)) > 4:
                    return "ADC"
                else:
                    return "SUPPORT"
            else:
                return False

def findLaneOpponentParticipantId(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        Integer (1- 10): the participantId of the lane opponent of the participantId passed.
    """

    position = findPositions(match, participantId)
    for participant in match["participants"]:
        opponentId = participant["participantId"]
        opponentPosition = findPositions(match, opponentId)
        if position == opponentPosition and participantId != opponentId:
            return opponentId
        elif position is False:
            return None
