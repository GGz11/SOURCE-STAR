from STARXMusic.core.bot import Star
from STARXMusic.core.dir import dirr
from STARXMusic.core.git import git
from STARXMusic.core.userbot import Userbot
from STARXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Star()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
