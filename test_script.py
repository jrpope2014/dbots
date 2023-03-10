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
