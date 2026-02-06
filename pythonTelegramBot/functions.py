# deze file bevat alle functies die aangeroepen worden wanneer een command uitgevoerd wordt

# functie die afgedraaid wordt om de banner te maken
def get_banner() -> str:
    """
    Geeft de ASCII banner terug als string.
    """
    return r"""
┌─┐┬  ┬  ┬─┐  ┌─┐ ┬     ┌─┐ 
├─┘│  │  ├┬┘  ├─┘ │     ├┤  
┴    └─┘   ┴└─  ┴     ┴─┘ └─┘ 
                             
┌┬┐ ┬ ┌┬┐ ┌┬┐┌─┐ ┬─┐ ┌┬┐
│││ │    ││   │   ├┤   ├ ┬┘  │││
┴   ┴ ┴ ─┴┘   ┴   └─┘ ┴ └─ ┴   ┴

====================================
Viresh & Muazma
====================================
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