embed_commands = [
    "!help",
    "!profile",
    "!roblox",
    "!profileid"
]


# instead of having a list of embed commands, you can check if the return type is not a string instead

def is_embed_message(command):
    if command in embed_commands:
        return True
    return False
