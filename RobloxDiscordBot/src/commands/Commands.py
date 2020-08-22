import discord
from discord import Color
from src.roblox import RobloxAPI

"""
    List of functions that handle commands
    @author Brandon
    Created: 8/21/2020
"""


def help_command(ctx, args):
    from src import main
    from src.settings import Config
    commands_list = ""
    for key in main.commands:
        commands_list += f"{key}\n"
    e = discord.Embed(title="Commands", colour=Color.teal(), description="List of available commands.") \
        .set_thumbnail(url=Config.THUMBNAIL_URL) \
        .add_field(name="Commands", value=commands_list, inline=True)
    return e


def roblox_profile(ctx, args):
    syntax_err = discord.Embed(title="Failed", colour=Color.red(), description="ERROR: !roblox/!profile <username>")

    if len(args) < 2:
        return syntax_err

    username = args[1]
    # Both Profile Commands can be optimized for sure, by reducing the amount of requests
    user = RobloxAPI.get_user_by_username(username).json()
    user_presence = RobloxAPI.get_user_presence(user['data'][0]['id']).json()
    user_id = user['data'][0]['id']

    pfp = RobloxAPI.get_pfp_by_id(user_id)
    status = RobloxAPI.get_user_status(user_id)
    display_name = user['data'][0]['displayName']
    presence_type = RobloxAPI.get_presence_type(user_presence['userPresences'][0]['userPresenceType'])
    presence_type_num = user_presence['userPresences'][0]['userPresenceType']
    game_name = "Not in game" if presence_type_num is 0 or presence_type_num is 1 else \
        user_presence['userPresences'][0][
            'lastLocation']
    game_id = user_presence['userPresences'][0]['placeId']
    game_url = None if presence_type_num is 1 or presence_type_num is 0 else RobloxAPI.get_game_link(game_id)

    e = discord.Embed(title=display_name, colour=Color.teal(), description="Information on Roblox Profile",
                      url=game_url)
    e.set_thumbnail(url=pfp)
    e.add_field(name="Status", value=status, inline=False)
    e.add_field(name="In-Game", value=presence_type, inline=True)
    e.add_field(name="Game", value=game_name, inline=False)

    return e


def profile_id(ctx, args):
    syntax_err = discord.Embed(title="Failed", colour=Color.red(), description="ERROR: !profileid <user id>")
    if len(args) < 2:
        return syntax_err

    user_id = args[1]
    user_presence = RobloxAPI.get_user_presence(user_id).json()
    user = RobloxAPI.get_user_by_id(user_id).json()

    pfp = RobloxAPI.get_pfp_by_id(user_id)
    status = RobloxAPI.get_user_status(user_id)
    display_name = user['displayName']
    presence_type = RobloxAPI.get_presence_type(user_presence['userPresences'][0]['userPresenceType'])
    presence_type_num = user_presence['userPresences'][0]['userPresenceType']
    game_name = "Not in game" if presence_type_num is 0 or presence_type_num is 1 else \
        user_presence['userPresences'][0][
            'lastLocation']
    game_id = user_presence['userPresences'][0]['placeId']
    game_url = None if presence_type_num is 1 or presence_type_num is 0 else RobloxAPI.get_game_link(game_id)

    e = discord.Embed(title=display_name, colour=Color.teal(), description="Information on Roblox Profile",
                      url=game_url)
    e.set_thumbnail(url=pfp)
    e.add_field(name="Status", value=status, inline=False)
    e.add_field(name="In-Game", value=presence_type, inline=True)
    e.add_field(name="Game", value=game_name, inline=False)

    return e


def search_username(ctx, args):
    if len(args) < 2:
        return "[ERROR] Syntax: !searchname <keyword>"
    keyword = args[1]
    all_users = RobloxAPI.search_for_users(keyword).json()
    all_users_data = all_users["data"]
    msg = f"Here are some results on {keyword}.\n```"

    for info in all_users_data:
        msg += f"{info['name']}, id:{info['id']}\n"

    return msg + "```"
