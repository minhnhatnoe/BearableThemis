"""A code just to show that it works"""
import asyncio
from client.themis import ThemisInstance
from client.portals.manual import ManualPortal
from client.validators import Duplicate, LastSubmit, StartTime, EndTime

osd = input("OSD: ")
validator = [Duplicate(), LastSubmit(), StartTime(), EndTime()]

tinst = ThemisInstance(osd)
portal = ManualPortal(judge=tinst.submit)

async def run():
    """Run the routine"""
    await portal.listen()

asyncio.run(run())
