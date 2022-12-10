"""Receives code from Discord"""
import disnake
from portals.modules.portalabc import Portal
from api.submission import Submission

class Gitcord(Portal):
    """Portal for Discord"""
    bot: disnake.Client
    token: str
    def __init__(self, token: str|None=None, *args, **kwargs) -> None:
        """Initializes with token"""
        super().__init__(*args, **kwargs)
        if token is None:
            token = input("Input token: ")
        self.token = token
        self.bot = disnake.Client(intents=disnake.Intents.all())
    
    async def listen(self) -> None:
        """S"""
        await self.bot.start(token=self.token, reconnect=True)
