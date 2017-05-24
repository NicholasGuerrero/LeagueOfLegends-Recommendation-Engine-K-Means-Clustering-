"""This file contains all functions that find or analyze events from a match."""

def findEventType(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        List: The events at each event frame for in the match passed.
    Example: findEventType(match) -> ["ITEM_PURCHASED", "WARD_PLACED",  ... nth frame]
    """

    eventTypes = []

    for frame in match["timeline"]["frames"]:
        if "events" in frame:
            for event in frame["events"]:
                eventTypes.append(event["eventType"])

    return eventTypes

def findEventTimestamp(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        List: The event timestamp at each event frame for in the match passed.
    Example: findEventType(match) -> [2095, 2290, 2453 ... nth frame]
    """

    eventTimestamp = []

    for frame in match["timeline"]["frames"]:
        if "events" in frame:
            for event in frame["events"]:
                eventTimestamp.append(event["timestamp"])

    return eventTimestamp
