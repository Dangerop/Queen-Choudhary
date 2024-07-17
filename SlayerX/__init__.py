from Queen-Choudhary.core.bot import Slayer
from Queen-Choudhary.core.dir import dirr
from Queen-Choudhary.core.git import git
from Queen-Choudhary.core.userbot import Userbot
from Queen-Choudhary.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Slayer()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
