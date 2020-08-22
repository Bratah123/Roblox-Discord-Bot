import requests

from src.settings import Config

"""
    I would not recommend using functions that get info by username as they request more data unless you only plan to 
    use it once in a command 
    @author Brandon
"""

cookies = {
    '.ROBLOSECURITY': Config.ROBLOX_COOKIE
}


def get_pfp_by_id(user_id):
    return f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width=420&height=420&format=png"


def get_user_status(user_id):
    r = requests.get(f"https://users.roblox.com/v1/users/{user_id}/status")
    return r.json()['status']


def get_status_by_name(username):
    user_id = get_user_id_by_username(username)
    return get_user_status(user_id)


def get_user_presence(user_id):
    payload = {
        "userIds": user_id
    }
    r = requests.post("https://presence.roblox.com/v1/presence/users", data=payload, cookies=cookies)
    return r


def get_user_by_username(username):
    payload = {
        "usernames": username
    }
    r = requests.post("https://users.roblox.com/v1/usernames/users", data=payload, cookies=cookies)
    return r


def get_user_by_id(user_id):
    r = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
    return r


def get_user_id_by_username(username):
    r = get_user_by_username(username)
    data = r.json()
    user_id = data['data'][0]['id']
    return user_id


def get_pfp_by_username(username):
    user_id = get_user_id_by_username(username)
    return get_pfp_by_id(user_id)


def get_presence_type(type):
    if type is 0:
        return "Offline"
    elif type is 1:
        return "Online"
    elif type is 2:
        return "In-Game"
    else:
        return "undefined"


def get_game_link(game_id):
    return f"https://www.roblox.com/games/{game_id}/"


def search_for_users(keyword):
    # limit param can be changed to reduce/increase searches
    r = requests.get(f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit=10")
    return r
