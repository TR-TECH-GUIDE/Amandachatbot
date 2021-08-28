from lycia.config import Config
from pyrogram import Client

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN

LYCIA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
