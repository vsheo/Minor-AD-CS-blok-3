# Deze file bevat alle commands die via telegram chat uitgevoerd kunnen worden
from telegram import Update
from telegram.ext import ContextTypes
from functions import *

# ASCII banner
async def banner_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_banner())

# lijst van alle commands terug geven
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_command_list())

# Reactie om alles dat geen slash command is
async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands."
    )

# webcam recording maken
async def start_recording(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Webcam opname wordt gestart...")
    get_camRecording()

# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')