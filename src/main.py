"""A code just to show that it works"""
import asyncio
from api import ThemisInstance
from portals.modules.gitcord import Gitcord
from validators import Group

osd = input("OSD: ")
validator = Group([])
AWTRES = True

tinst = ThemisInstance(osd, validator, AWTRES)
portal = Gitcord(None, judge=tinst.submit)

async def run():
    """Run the routine"""
    await portal.listen()

asyncio.run(run())
