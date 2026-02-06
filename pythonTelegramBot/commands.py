from telegram import Update
from telegram.ext import ContextTypes

# Command to provide help information
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Here comes the help')

# Reactie om alles dat geen slash command is
async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands."
    )


# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')