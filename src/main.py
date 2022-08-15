"""A code just to show that it works"""
import asyncio
from api import ThemisInstance
from portals.modules.manual import ManualPortal
from validators import Group

osd = input("OSD: ")
validator = Group([])
AWTRES = True

tinst = ThemisInstance(osd, ["B05"], validator, AWTRES)
portal = ManualPortal(tinst.submit)

FUNCT = portal.start()

asyncio.run(FUNCT)
