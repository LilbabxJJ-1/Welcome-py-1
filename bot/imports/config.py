import sys
sys.path.append('..')

from db.dbc          import client as connection_url
from db.mongo        import Document
from imports.discord import *
from imports.asyncio import *

intents      = discord.Intents.all()
ACTIVITY     = discord.Activity(type=discord.ActivityType.watching, name="discord.gg/FemboyCafe")
bot          = commands.Bot(command_prefix=commands.when_mentioned_or('.', '. '), intents=intents, activity=ACTIVITY, case_insensitive=True, tree_cls=app_commands.CommandTree)
bot.mongo    = motor.motor_asyncio.AsyncIOMotorClient(str(connection_url))
bot.db       = bot.mongo["Pybot00"]
bot.inbox    = Document(bot.db, "inbox")
bot.bio      = Document(bot.db, "bio")
bot.config   = Document(bot.db, "level_config")
bot.levels   = Document(bot.db, "levels") # users levels
bot.verifies = Document(bot.db, "verifications")