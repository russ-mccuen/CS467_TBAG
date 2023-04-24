# define possible directions to move
DIRECTIONS = {
    "north": ["n", "north"],
    "south": ["s", "south"],
    "east": ["e", "east"],
    "west": ["w", "west"],
    "up": ["u", "up"],
    "down": ["d", "down"]
}


# define function to parse user input and return the corresponding direction
def parse_direction(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()
    if len(words) == 2 and words[0] == "move":
        for direction, aliases in DIRECTIONS.items():
            if words[1] in aliases:
                return direction
    return None
