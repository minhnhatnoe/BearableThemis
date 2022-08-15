import asyncio
from api import ThemisInstance
from portals.modules.manual import ManualPortal
from validators import Group

osd = input("OSD: ")
validator = Group([])
await_result = True

tinst = ThemisInstance(osd, ["B05"], validator, await_result)
portal = ManualPortal(tinst.submit)

funct = portal.start()

asyncio.run(funct)
