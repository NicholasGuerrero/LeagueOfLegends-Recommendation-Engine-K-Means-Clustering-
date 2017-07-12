"""This file contains all functions that find or analyze the matchId of a match."""

def findMatchId(match):
    """
    Args:
        match (dict): One match from the league of legends API. See Riot API Docs for details.
    Returns:
        List: The matchId for each match.
    Example: findMatchId(match) -> [2542522246, 2542622246, 2582522246, 2742522246, ... nth frame]
    """

    return [int(match["matchId"])]
