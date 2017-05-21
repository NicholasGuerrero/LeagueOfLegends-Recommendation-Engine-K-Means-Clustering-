"""This is where it all starts to create the random forests model."""
import pprint
from libs import database
from libs import gold
from libs import resources

def main():
    "This is the main function. It all starts here."

    matches = database.connect("noschemas")
    match = matches.find({"matchId":2398848900}, limit=1)[0]
    pprint.pprint(resources.findJungleMinionsKilled(match, 4))



if __name__ == "__main__":
    main()
