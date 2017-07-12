"""This file contains all functions that find or analyze items from a match."""

def findItems(match, participantId):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
        participantId (integer 1- 10): The particpantId of a player in match.
    Returns:
        List: The total items at each frame for the participantId.
    Example: findItems(match, participantId) -> [3303, 2010, 2010, 3340, 2010 ... nth frame]
    """

    if participantId < 1 or participantId > 10:
        raise IndexError(("participantId %d out of range."
                          " participantId only takes values 1-10." %  participantId))

    items = []
    placeholder = []
    for frame in match["timeline"]["frames"]:
        timestamp = frame["timestamp"]
        if "events" in frame:
            for event in frame["events"]:
                eventType = event["eventType"]
                if eventType == "ITEM_PURCHASED" and event["participantId"] == participantId and event["timestamp"] <= timestamp:
                    placeholder.append(event["itemId"])
        items.append(placeholder)
        placeholder = []

    for itemPosition, item in enumerate(items):
        # print(itemPosition, item)
        if item != []:
            try:
                items[itemPosition + 1] = items[itemPosition + 1] + items[itemPosition]
            except:
                pass
    return items
