# Week 3: Pre-exploitation reconnaissance in OT-Omgevingen

We hebben nu onze OT-lab omgeving opgezet en werkend gekregen. Nu gaan we aan de slag met verschillende tooling voor het pentesten van de OT-omgeving. De opdrachten zijn meer doe-opdrachten en bij sommige opdrachten zul je het zelf moeten gaan uitzoeken. Noteer de commando’s die je hebt gebruikt. Leg het resultaat uit en ondersteun dit met screenshots.

---

## Opdracht 1: Start de containers

Start de containers als die niet zijn opgestart:  
```
docker-compose up -d
```

Controleer welke containers draaien:
```
docker ps
```

Maak een screenshot van de containers die draaien.

> [Screenshot invoegen]

---

## Opdracht 2: Netwerkadres

Leg uit hoe jij jouw netwerkadres vindt.  
Commando dat ik heb gebruikt:
`ip a` of `ifconfig`

Uitleg:  
Met dit commando zie ik mijn IP-adres en subnetmask.  
Voorbeeld:
- `inet 192.168.2.15/24`  

Dit betekent:
- IP-adres: 192.168.2.15  
- Subnetmask: /24  
- Netwerkadres: 192.168.2.0/24  

Mijn netwerkadres is:  


[Hier jouw netwerk invullen]

[Screenshot invoegen]

---

## Opdracht 3: Host discovery (netdiscover – layer 2)
Commando dat ik heb gebruikt:  
```
sudo netdiscover -r 192.168.2.0/24
```

Uitleg:  
Netdiscover werkt op Layer 2 (ARP). Hiermee worden actieve hosts binnen het lokale netwerk gevonden.

Welke hosts zijn actief op mijn netwerk:  

- IP-adres:
- MAC-adres:
- Vendor:

- IP-adres:
- MAC-adres:
- Vendor:

[Screenshot invoegen]

---

## Opdracht 4: Network discovery (ip route – layer 3)
Commando dat ik heb gebruikt:
```
ip route
```

Uitleg:  
Met dit commando zie ik welke netwerken bereikbaar zijn via de router.

Voorbeeld output:
- default via 192.168.2.1 dev eth0  
- 192.168.2.0/24 dev eth0  
- 192.168.3.0/24 via 192.168.2.1  

Welke netwerken bestaan er achter de router:

-  
-  
-  

[Screenshot invoegen]

---

## Opdracht 5: Overzicht van apparaten op de verschillende netwerken (nmap)
Bij network discovery heb ik verschillende netwerken gevonden.  
Commando voor host discovery:
```
sudo nmap -sn 192.168.2.0/24
```

Commando voor service scan:
```
sudo nmap -sV 192.168.2.0/24
```

Uitleg:  
- sn = alleen host discovery  
- sV = service detectie  

Overzicht van apparaten:

- IP-adres:  
- Open poorten:  
- Services:  

- IP-adres:  
- Open poorten:  
- Services:  

[Screenshot invoegen]

---

## Opdracht 6: Protocol enumeratie (specifieke poort en service – PLCSCAN)
Zoek naar apparaten (IP) met modbus protocol/service.  
Commando dat ik heb gebruikt:
```
plcscan 192.168.2.0/24
```
of specifiek:
```
plcscan -m modbus 192.168.2.0/24
```

Uitleg: 
PLCSCAN zoekt naar PLC-apparaten en industriële protocollen zoals Modbus (poort 502).

Gevonden Modbus apparaten:

- IP-adres:  
- Poort: 502  
- Protocol: Modbus  

[Screenshot invoegen]

---

## Opdracht 7: Enumeratie met modbuscripts
Zoeken naar modbus scripts voor de Nmap Scripting Engine (.nse):
```
ls /usr/share/nmap/scripts/ | grep modbus
```
We gaan nu het gevonden script gebruiken in combinatie met NMAP.  
Commando dat ik heb gebruikt:
```
sudo nmap -Pn [ip-adres] -p [poortnummer] --script [naam van het script].nse
```

Voorbeeld:
```
sudo nmap -Pn 192.168.2.10 -p 502 --script modbus-discover.nse
```

Wat voor output krijg ik te zien:

- Bevestiging dat poort 502 open staat  
- Device informatie  
- Mogelijke slave ID  
- Eventuele foutmeldingen  

[Screenshot invoegen]

---

## Opdracht 8: Metasploit
Start Metasploit:
```
msfconsole
```

Zoek naar modbus modules:
```
search modbus
```

Noteer en omschrijf de modules die je ziet:

- auxiliary/scanner/scada/modbusdetect  
- auxiliary/scanner/scada/modbusclient  

Selecteer de modbusdetect module:
```
use auxiliary/scanner/scada/modbusdetect
```


Zet de RHOSTS op 192.168.2.0/24:

set RHOSTS 192.168.2.0/24

Run de module:

run

Resultaat van de modbusdetect module:

- IP-adressen met open Modbus poort  
- Bevestiging dat poort 502 open staat  
- Eventuele device informatie  

[Screenshot invoegen]
