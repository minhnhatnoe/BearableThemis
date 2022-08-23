"""A code just to show that it works"""
import asyncio
from api import ThemisInstance
from portals.modules.manual import ManualPortal
from validators import Group

osd = input("OSD: ")
validator = Group([])
AWTRES = True

tinst = ThemisInstance(osd, validator, AWTRES)
portal = ManualPortal().listen()

async def run():
    """Run the routine"""
    async for sub in portal:
        result = await tinst.submit(sub)
        await portal.asend(result)

asyncio.run(run())
