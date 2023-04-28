# this is a sample dictionary of verbs that we can use in the game
# I made it as a separate file so we can change it as needed with verbs
# that fit the story
VERBS = {
    "go": ["move", "walk", "run", "travel"],
    "take": ["get", "grab", "pick up"],
    "drop": ["put down", "release"],
    "look": ["examine", "inspect"],
    "hit": ["attack", "strike", "punch"],
    "pull": ["drag", "tug"],
    "push": ["shove", "press"],
    "eat": ["consume", "devour"],
    "use": ["activate", "operate"],
    "talk": ["speak", "converse"]
}


def parse_verb(verb):
    for action, synonyms in VERBS.items():
        if verb in synonyms:
            print(f"You want to {action}.")


