from dataclasses import dataclass

from items.storage import Storage


@dataclass
class Location:
    title: str
    locations: list = []
    loot: Storage = Storage([])
    
locations = {
    "spawn": ['location_1', 'location_2'],
    "blacksmith_house": ['spawn', 'location_3'],
    "house": ['spawn', 'location_3'],
    "guild_house": ['spawn', 'location_2'],
}

def print_location_info(location):
    print(f"You re in location '{location}'")
    print(f"You can change your location: ")
    for l in location[locations]:
        print(l)

def movement(location):
    while True:
        print_location_info(location)
        movement  = input("Enter the name of the location: ")
        if movement in locations[location]:
            location = movement
            print(f"You moved to the location: '{location}'")
            break
        else:
            print("Invalid location")

    