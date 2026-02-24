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

Welke host zijn allemaal actief op jouw netwerk
<img width="1297" height="340" alt="image" src="https://github.com/user-attachments/assets/eb34088d-e6e1-47e1-aed4-1ce43bb74063" />
command dat ik heb gebruikt:``sudo netdiscover``

---

## Opdracht 4: Network discovery (ip route – layer 3)
[command dat ik heb gebruikt](https://medium.com/infosecmatrix/understanding-routing-in-linux-configuring-routes-and-gateways-289bc67fe76a#:~:text=Using%20ip%20route%20to%20View%20Routing%20Table):
```
ip route
```

<img width="1409" height="287" alt="image" src="https://github.com/user-attachments/assets/12f865e1-2e96-45e7-8f96-334c1a3f5579" />

Welke netwerken bestaan er achter de router:
-  [default via `192.168.58.2`](https://medium.com/infosecmatrix/understanding-routing-in-linux-configuring-routes-and-gateways-289bc67fe76a#:~:text=1.100-,default%20via%20192.168.1.1%20dev%20eth0,-%3A%20This%20shows%20the) de default route
-  docker0 & br-00452fe8ed6f -> met ip adress: `172.17.0.0/16` & `172.18.0.0/16`, zijn [zelf gegenereerd door docker](https://docs.docker.com/engine/network/?utm_source=chatgpt.com#automatic-subnet-allocation) om conflicten te voorkomen
-  plc: `192.168.2.0/24`
-  scada: `192.168.3.0/24`
-  [`192.168.58.0/24` dev eth0](https://medium.com/infosecmatrix/understanding-routing-in-linux-configuring-routes-and-gateways-289bc67fe76a#:~:text=the%20eth0%20interface.-,192.168.1.0/24%20dev%20eth0,-%3A%20This%20indicates%20that), indicates that traffic for the network

---

## Opdracht 5: Overzicht van apparaten op de verschillende netwerken (nmap)
Bij network discovery heb ik verschillende netwerken gevonden.  
Maak en overzicht van apparaten op de verschillende netwerke.  

> sudo nmap -sn IP address -> sn = alleen host discovery 
sudo nmap -sV IP address -> sV = service detectie  
### plc:
```
sudo nmap -sn 192.168.2.0/24
```
<img width="1166" height="454" alt="image" src="https://github.com/user-attachments/assets/d15b315a-ad8d-40ad-9677-2255634669fe" />  

gevonden IP adressen:  
- `192.168.2.10`  
- `192.168.2.254`
- `192.168.2.1`
256 Ip adressen -> 3 hosts up

```
sudo nmap -sV 192.168.2.10 192.168.2.254 192.168.2.1
```  
<img width="1692" height="952" alt="image" src="https://github.com/user-attachments/assets/7cb2bc67-79e5-4e76-b6a7-0bde50108506" />

| IP-adres      | Port     | State    | Service     | Versie                                 | MAC-adres           |
|---------------|----------|----------|-------------|----------------------------------------|---------------------|
| 192.168.2.10  | 8080/tcp | open     | http        | Werkzeug httpd 2.3.7 (Python 3.11.2)   | 02:42:C0:A8:02:0A   |
| 192.168.2.254 | 8000/tcp | open     | http        | aiohttpd 3.12.13 (Python 3.11.2)       | 02:42:C0:A8:02:FE   |
| 192.168.2.1   | 443/tcp  | filtered | https       |                                        |                     |
| 192.168.2.1   | 8080/tcp | filtered | http-proxy  |                                        |                     |


### scada:
```
sudo nmap -sn 192.168.3.0/24
```
<img width="1190" height="422" alt="image" src="https://github.com/user-attachments/assets/833a4262-e778-415d-b4c3-4f754e30ad2b" />

gevonden IP adressen:  
- `192.168.3.20`  
- `192.168.3.254`
- `192.168.3.1`
256 Ip adressen -> 3 hosts up


```
sudo nmap -sV 192.168.3.20 192.168.3.254 192.168.3.1
```  
<img width="1673" height="919" alt="image" src="https://github.com/user-attachments/assets/f840b2c7-2760-41ec-8b63-4b04da7b667b" />

| IP-adres      | Port     | State    | Service     | Versie                                 | MAC-adres           |
|---------------|----------|----------|-------------|----------------------------------------|---------------------|
| 192.168.3.20  | 8080/tcp |      |         |    | 02:42:C0:A8:02:14   |
| 192.168.3.254 | 8000/tcp | open     | http        | aiohttpd 3.12.13 (Python 3.11.2)       | 02:42:C0:A8:03:FE   |
| 192.168.3.1   | 443/tcp  | filtered | https       |                                        |                     |
| 192.168.3.1   | 8080/tcp | filtered | http-proxy  |                                        |                     |
> 192.168.3.20 -> geen open ports gevonden

---

## Opdracht 6: Protocol enumeratie (specifieke poort en service – [PLCSCAN](https://ot-pentesting.readthedocs.io/en/latest/plcscan/))
Zoek naar apparaten (IP) met modbus protocol/service.  

Uit de ReadME van `plcscan/README.md`
## Usage examples:
```
sudo python2 plcscan.py 192.168.0.1
plcscan.py --timeout 2 192.168.0.1:102 10.0.0.0/24
plcscan.py --hosts-list hosts.txt'
```
result van `sudo python2 plcscan.py 192.168.0.1` geeft modbus apparaten terug

### plc
```
sudo python2 plcscan.py 192.168.2.1
sudo python2 plcscan.py 192.168.2.10
sudo python2 plcscan.py 192.168.2.254
```
<img width="765" height="682" alt="image" src="https://github.com/user-attachments/assets/3d0e9bed-356b-40d0-ae63-09b0a80d6492" />

| IP-adres     | Protocol    | Port | PLC/Device gevonden |
|--------------|-------------|------|---------------------|
| 192.168.2.1  | -           | -    | Nee                 |
| 192.168.2.10 | Modbus/TCP  | 502  | Ja                  |
| 192.168.2.254| -           | -    | Nee                 |

### scada
```
sudo python2 plcscan.py 192.168.3.1
sudo python2 plcscan.py 192.168.3.20
sudo python2 plcscan.py 192.168.3.254
```
<img width="756" height="514" alt="image" src="https://github.com/user-attachments/assets/00bdd465-0a36-4044-b37c-6f50f5cd6acd" />

geen modbusd apparaten gevonden

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
