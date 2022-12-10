"""Receives code from Discord"""
import disnake
from disnake.ext import commands
from portals.modules.portalabc import Portal
from api.submission import Submission

class Gitcord(Portal):
    """Portal for Discord"""
    bot: commands.Bot
    token: str
    def __init__(self, token: str|None=None, *args, **kwargs) -> None:
        """Initializes with token"""
        super().__init__(*args, **kwargs)
        if token is None:
            token = input("Bot token: ")
        self.token = token
        self.bot = commands.Bot(intents=disnake.Intents.all())
        self.bot.load_extension("portals.modules.gitcord.botext.submit")
    
    async def listen(self) -> None:
        """S"""
        await self.bot.start(token=self.token, reconnect=True)
