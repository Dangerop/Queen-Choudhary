import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Queen-Chiudhary import LOGGER, app, userbot
from Queen-Choudhary.core.call import Slayer
from Queen-Choudhary.misc import sudo
from Queen-Choudhary.plugins import ALL_MODULES
from Queen-Choudhary.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Queen-Choudhary.plugins" + all_module)
    LOGGER("Queen-Choudhary.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Slayer.start()
    try:
        await Queen-Choudhary.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Queen-Choudhary").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Queen-Choudhary.decorators()
    LOGGER("Queen-Choudhary").info(
        "Queen-Choudhary Music Bot Started Successfully, JOIN @Great_society"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Queen-Choudhary").info("Stopping Queen-Choudhary Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
