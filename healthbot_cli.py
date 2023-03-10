import argparse

from healthbot import SwoleBot

parser = argparse.ArgumentParser(description="Perform actions with the Discord healthbot")
parser.add_argument('action', choices=['send_registered_users_message'])
args = vars(parser.parse_args())

def __get_registered_users(userfile='registered_usernames.txt'):
    with open(userfile, 'r') as f:
        registered_users = f.read().split('\n')
    return registered_users

def send_registered_users_message():
    print("called")
    registered_users = __get_registered_users()
    bot = SwoleBot()
    
    #TODO: Refactor, parameterize, try to suck less
    
    # get specific guild
    guilds = bot.get_guilds()
    myguild = list(filter(lambda guild: guild['name'] == "JAMMING WITH POPERNICUS", guilds))[0]
    myguild_id = myguild['id']
    
    # get specific channel
    guild_channels = bot.get_guild_channels(myguild_id)
    health_channel = list(filter(lambda channel: channel['name'] == 'healthbot-test', guild_channels))[0]
    health_channel_id = health_channel['id']
    
    # get members in guild
    members = bot.get_guild_members(myguild_id)
    user_dicts = [
        {
            'username': user['username'],
            'display_name': user['display_name'],
            'id': user['id']
            } for user in map(lambda member: member['user'], members)
        ]
    registered_user_dicts = [user for user in user_dicts if user['username'] in registered_users]
    registered_user_list_string = ', '.join([bot.get_user_mention(user) for user in registered_user_dicts])
    registered_user_message = f"Currently registered users: {registered_user_list_string}"
    cli_test_message = "CLI test, registered user message:\n"
    bot.send_message(health_channel_id, cli_test_message + registered_user_message)
    
        

def main(args):
    if args['action'] == 'send_registered_users_message':
        send_registered_users_message()
    

if __name__ == "__main__":
    main(args)
