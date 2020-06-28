import re

# Location class (data type to store information about a location)
class Location:
    def __init__(self, ending, loc, linksys, ignore):
        self.ending = ending
        self.loc = loc
        self.linksys = linksys
        self.ignore = ignore

# Function to get all locations
# Returns: Array of type Location
def get_locations():
    locations = []
    f = open("locations.txt", "r")
    for l in f:
        gps = re.match(r'^(.*)(?:\, ")(.*)(?:"\,\ linksys=)(.*)(?:\,\ ignore=)(.*)(?:\,)$', l).groups()
        ending, locationName, linksys, ignore = gps[0], gps[1], gps[2], gps[3]
        locations.append(Location(int(ending), locationName, linksys=="True", ignore=="True"))
    return locations

get_locations()