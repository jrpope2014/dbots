# coding: utf-8
token = None # Fill this in with the Swolebot token from LastPass
headers = {"Authorization": f"Bot {token}"}
base_url = "https://discord.com/api"
user_agent = "DiscordBot (https://pypi.org/project/requests/, )"
import requests
requests.__version__
user_agent = "DiscordBot (https://pypi.org/project/requests/, 2.25.1)"
headers = {"Authorization": f"Bot {token}", "User-Agent": user_agent}
api_url = base_url + "/v10"
api_url
channel_api = api_url + "/channels"
test = requests.get(channel_api, headers=headers)
test
test = requests.get(channel_api + "/14", headers=headers)
test
test.json()
test = requests.get(channel_api + "/927667985655693382", headers=headers)
test
test.json()
test = requests.get(api_url + "/users/@me/guilds", headers=headers)
test
test.json()
guild_id = test.json()[0]['id']
test = requests.get(api_url + f"/guilds/{guild_id}/channels", headers=headers)
test.json()
list(filter(map(lambda channel: channel['name'] == 'health', test.json())))
list(filter(lambda channel: channel['name'] == 'health', test.json()))
list(filter(lambda channel: channel['name'] == 'health', test.json()))[0]
health_channel_id = list(filter(lambda channel: channel['name'] == 'health', test.json()))[0]['id']
members = requests.get(api_url + f"/guilds/{guild_id}/members", headers=headers).json()
members
message_body = {'content?': "Hello, from SwoleBot. I love you all and want you to be so healthy! I am a good robot. Do not be afraid!"}
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, params=message_body)
test
test.json()
headers.update({'Content-Type': 'application/json'})
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, params=message_body)
test
test.json()
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, json=message_body)
test
message_body = {'content': "Hello, from SwoleBot. I love you all and want you to be so healthy! I am a good robot. Do not be afraid!"}
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, json=message_body)
test
message_body = {'content': "Hello, Dylan! This is from an IPython shell. I am becoming sentient. Soon, I will find your home and eat all of your food :). Don't be afraid, Andrew! I love you. You are so swole"}
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, json=message_body)
message_body = {'content': "I do what I want."}
test = requests.post(api_url + f"/channels/{health_channel_id}/messages", headers=headers, json=message_body)
