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
        self.url = self.api_url + self.api_version
    
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
        auth_header = {'Authorization': f'Bot {token}'}
        return auth_header
    
    def send_message(self, message):
        """
        Params
        ------
        message : str
            A message to send to the 
        """
        pass

