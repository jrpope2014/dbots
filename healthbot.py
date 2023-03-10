import requests

class SwoleBot:
    def __init__(self, session=None):
        """
        Bot for use with the health-challenge-bot
        
        Params
        ------
        session : requests.Session
            A preconfigured session for the Discord Bot to use in order to interact with Discord 
        """

        self.session = session or self.__configure_default_bot_session()
        self.api_url = 'https://discord.com/api'
        self.api_version = '10'
        self.url = f"{self.api_url}/v{self.api_version}"
    
    def __configure_default_bot_session(self):
        """
        Info on user agent reqs: https://discord.com/developers/docs/reference#user-agent
        """
        
        session = requests.Session()
        session.headers = {
            'Authorization': self.__configure_auth_header(),
            'Content-Type': 'application/json',
            'User Agent': f'DiscordBot ({requests.__url__, requests.__version__})'
        }
        return session

    def __configure_auth_header(self):
        with open("bot_token.txt", 'r') as token_file:
            token = token_file.read()
        auth_header = f'Bot {token}'
        return auth_header
    
    def get_guilds(self):
        """
        Returns
        -------
        list : [{guild_dict}]
        
        Notes
        -----
        * https://discord.com/developers/docs/resources/user#get-current-user-guilds
        """
        
        resp = self.session.get(f"{self.url}/users/@me/guilds")
        resp.raise_for_status()
        return resp.json()
    
    def get_guild_channels(self, guild_id):
        """
        Returns
        -------
        list : [{channel_dict}]
        
        Notes
        -----
        * https://discord.com/developers/docs/resources/guild#get-guild-channels
        """
        
        resp = self.session.get(self.url + f"/guilds/{guild_id}/channels")
        resp.raise_for_status()
        return resp.json()
    
    def get_guild_members(self, guild_id):
        """
        Params
        ------
        guild_id : str
            The id of the guild to retrieve all members for
        
        Returns
        -------
        list : [{user_dict}]
        
        Notes
        -----
        * https://discord.com/developers/docs/resources/guild#list-guild-members
        """
        params = {
            "limit": 1000
        }
        
        resp = self.session.get(self.url + f"/guilds/{guild_id}/members", params=params)
        resp.raise_for_status()
        return resp.json()
    
    def get_user_mention(self, user):
        """
        Generates a formatted message string for mentioning the passed user
        
        Params
        ------
        user : {user_dict}
            Note that a user_dict is a subcomponent of a guild member dict
        
        Returns
        -------
        str : a mention string for the specified user
        """
        
        return f"<@{user['id']}>"
    
    def send_message(self, channel_id, message):
        """
        Sends a message to Discord

        Params
        ------
        message : str
            A message to send to the Discord channel
            
        Returns
        -------
        dict: {message_dict}
        
        Notes
        -----
        * https://discord.com/developers/docs/resources/channel#create-messagey
        * https://discord.com/developers/docs/resources/channel#allowed-mentions-object
        """
        body = {
            "content": message,
            "allowed_mentions": {
                "parse": ["users"],
            }
        }
        resp = self.session.post(self.url + f"/channels/{channel_id}/messages", json=body)
        resp.raise_for_status()
        return resp.json()

