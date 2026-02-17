# Week 3: Pre-exploitation reconnaissance in OT-Omgevingen

We hebben nu onze OT-lab omgeving opgezet en werkend gekregen. Nu gaan we aan de slag met verschillende tooling voor het pentesten van de OT-omgeving. De opdrachten zijn meer doe-opdrachten en bij sommige opdrachten zul je het zelf moeten gaan uitzoeken. Noteer de commando’s die je hebt gebruikt. Leg het resultaat uit en ondersteun dit met screenshots.

---

## Opdracht 1: Start de containers
Start de containers als die niet zijn opgestart:  
```
docker-compose up -d
```
> Controleer welke containers draaien:`docker ps`

<img width="2697" height="832" alt="image" src="https://github.com/user-attachments/assets/cf379322-2936-4cf9-8f6e-6469569c87fe" />

---

## Opdracht 2: Netwerkadres
Leg uit hoe jij jouw netwerkadres vindt.  

Met de command `ifconfig -a` of `ip addr show` krijg ik alle interfaces op mijn laptop te zien.  
Ik heb `ip addr show` gebruikt omdat deze kleur geeft en het daardoor makkelijker te lezen is.  
In de lijst staat:  
- `eth0`: dat is de first Ethernet network, dit heeft de grootste kan om mijn IP te zijn  
- `lo`: dat is de [loopback](https://www.juniper.net/documentation/us/en/software/junos/junos-getting-started/interfaces-fundamentals/topics/concept/interface-security-loopback-understanding.html) (een virtuele interface)  
- `docker0`: dit is een Docker virtuele interface
> door docker even te stoppen kon ik zien welke door docker-compose gemaakt zijn, mijn ip kan dus niet daartussen liggen

`lo` is een loopback, dat betekent dat het een virtuele interface is met een 127.0.0.1 soort IP-adres.  
Het wordt gebruikt om netwerk verkeer van de computer naar zichzelf te sturen voor interne communicatie en testen.  
Dus dit kan niet mijn IP-adres zijn.  

`docker0` is [iets dat docker gebruikt voor networking](https://plaxidityx.com/blog/engineering-blog/docker-networking-behind-the-scenes/#:~:text=it%20works%20differently.-,Docker%20Networking,-Now%20that%20we),  
dus dit is ook niet mijn netwerk-IP.  

Daarom blijft `eth0` over, met een `192.168.*.*` IP-adres, wat wel lijkt op een IP-adres dat van mijn laptop kan zijn.  
Dit is dus het IP-adres dat ik gebruik voor mijn lokale netwerk.

---

## Opdracht 3: Host discovery (netdiscover – layer 2)
- [wat is netdiscover?](https://www.hackercoolmagazine.com/beginners-guide-to-netdiscover/?srsltid=AfmBOooMv5JlFJ4BpMa8dCDQ_bc_GjWj0-quRxGpl0XOSKsShZdaysdY)  
- [scan een network adress](https://www.hackercoolmagazine.com/beginners-guide-to-netdiscover/?srsltid=AfmBOooMv5JlFJ4BpMa8dCDQ_bc_GjWj0-quRxGpl0XOSKsShZdaysdY#:~:text=the%20%E2%80%9C%2Df%E2%80%9D%20option.-,Interface%20mode,-Netdiscover%20can%20be)

<img width="1297" height="340" alt="image" src="https://github.com/user-attachments/assets/eb34088d-e6e1-47e1-aed4-1ce43bb74063" />


command dat ik heb gebruikt:``sudo netdiscover``

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
