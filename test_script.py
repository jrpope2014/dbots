# coding: utf-8
from healthbot import SwoleBot
bot = SwoleBot()
guild_response = bot.session.get(f"{bot.api_url}/v{bot.api_version}/users/@me/guilds")
guilds = guild_response.json()
myguild = guilds[0]['id']
guild_channels = bot.get_guild_channels(myguild)
health_channel = list(filter(lambda channel: channel['name'] == 'healthbot-test', guild_channels))[0]
health_channel_id = health_channel['id']
members = bot.get_guild_members(myguild)
user_dicts = [{'username': user['username'], 'display_name': user['display_name'], 'id': user['id']} for user in map(lambda member: member['user'], members)]

def get_registered_users(userfile='registered_usernames.txt'):
    with open(userfile, 'r') as f:
        registered_users = f.read().split('\n')
    return registered_users

registered_users = get_registered_users()
registered_user_dicts = filter(lambda user: user['username'] in registered_users, user_dicts)

registered_user_message = f"Currently registered users: {', '.join(map(lambda user: bot.get_user_mention(user), registered_user_dicts))}"
print(registered_user_message)
