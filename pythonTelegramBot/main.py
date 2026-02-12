import os
from dotenv import load_dotenv
from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands import *

print('Bot is now starting up...')

load_dotenv()
API_TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
# BOT_HANDLE: Final = '@Daughter1738Bot'


# Start the bot
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('banner', banner_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('webcam', record_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, no_command))

    # Register error handler 
    app.add_error_handler(log_error)

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=2)