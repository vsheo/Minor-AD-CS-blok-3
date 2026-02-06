import os
from dotenv import load_dotenv

from typing import Final

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Bot is now starting up...')

load_dotenv()
API_TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_HANDLE: Final = '@Daughter1738Bot'


# Command to provide help information
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Here comes the help')

# Reactie om alles dat geen slash command is
async def text_without_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands."
    )

# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Start the bot
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('help', help_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, text_without_command))

    # Register error handler
    app.add_error_handler(log_error)

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=2)