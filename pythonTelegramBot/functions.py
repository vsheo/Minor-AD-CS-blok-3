# deze file bevat alle functies die aangeroepen worden wanneer een command uitgevoerd wordt

# functies die afgedraaid worden om de banner te maken
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
