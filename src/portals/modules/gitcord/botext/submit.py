import disnake
from disnake.ext import commands
from api.submission import available_langs

class SubmitCommand(commands.Cog):
    """Cog for submitting code."""

    @commands.slash_command()
    async def submit(self, inter: disnake.CommandInter, contestant: str, problem_name: str,
                   lang: str = commands.Param(choices=available_langs), *args):
        """Base command for submission"""

    @submit.sub_command()
    async def file(self, code_file: disnake.Attachment):
        """/submit file <contestant> <problem_name> <lang> <code_file>: Submit a solution"""
        
def setup(bot: commands.Bot):
    bot.add_cog(SubmitCommand())
