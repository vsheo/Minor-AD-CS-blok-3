# Risicoanalyse Vanguard
hier hou ik de volgorde bij van wat ik gedaan heb.


## Router
### R1
- `en` -> password protected

### R2
- `en` -> password protected


## SwitchS1
### S1
- `en` -> password protected

### S2
- `en`-> password protected

---

## AccessPoint
### wifi Medewerkers
- geen WEP key, PSK pass phrase, user ID en ook geen password
- encryption type disabled

### wifi Gasten
- geen WEP key, PSK pass phrase, user ID en ook geen password
- encryption type disabled

---

## Server PT
### File Server
desktop > command prompt
- `ipconfig`
  - <img width="826" height="332" alt="1" src="https://github.com/user-attachments/assets/a52b4f8b-6d28-41c5-9080-3708a0ad4d3a" />
- ping default gateway: `ping 192.168.10.1`
  - <img width="581" height="140" alt="image" src="https://github.com/user-attachments/assets/cefc975c-4dd4-4526-b029-29f610f60dc3" />
- ping PC0 & PC1  
`ping 192.168.20.3` & `ping 192.168.20.1` -> request timed out

### Windows Server
desktop > command prompt
- `ipconfig`
  - <img width="817" height="303" alt="3" src="https://github.com/user-attachments/assets/84678f98-0ae3-4c08-a47f-5aadec488935" />
- ping default gateway
  - <img width="618" height="151" alt="image" src="https://github.com/user-attachments/assets/03124a9c-6077-4a1f-9698-69e62e7631c9" />
- ping PC0 & PC1  
`ping 192.168.20.3` & `ping 192.168.20.1` -> request timed out

---

## PC
### PC0
- `ipconfig`
  - <img width="814" height="558" alt="5" src="https://github.com/user-attachments/assets/1f1b89cf-fa6e-4005-b790-cbda989e8cf4" />
- ping default gateway
  - <img width="754" height="316" alt="6" src="https://github.com/user-attachments/assets/a1b8f8d0-a0fd-4ed9-a89f-968e6c616fcc" />
- ping server PT  
`ping 192.168.10.10` & `ping 192.168.10.11` -> request timed out
- tracert server  
  - `tracert 192.168.10.10`
    - <img width="779" height="166" alt="7" src="https://github.com/user-attachments/assets/99bffdaa-0fe5-4d49-828f-a9949ef66403" />
  - `tracert 192.168.10.11`
    - <img width="770" height="174" alt="8" src="https://github.com/user-attachments/assets/deca82b0-594d-41f2-be79-b21afb3da19b" />
  - bij beide zie ik 3 keer `*` en  daarna request timed out
- telnet router
ip van de pc is `192.168.20.3` dus de router ip is de default gateway en die ip is: 
- `telnet 192.168.20.0` 
  - connection timed out; remote host not responding

### PC1
- `ipconfig`
  - <img width="819" height="510" alt="9" src="https://github.com/user-attachments/assets/09d3a427-0501-48a4-94a8-2eb99f66f00d" />
- PC1 is op hetzelfde netwerk als PC0 en heeft dezelfde resulaten

---
### telnet
op PC0 heb ik verschillende IP adresses geprobeert met telnet:  
<img width="828" height="516" alt="10" src="https://github.com/user-attachments/assets/27275f48-16f4-4210-8fb4-52a280a2f967" />

connectie gevonden op:
- `telnet 192.168.20.2`

---

## Subnetmask berekenen
S0 is verbonden met;
- PC0
- PC1
- R1
- R2
- File server
- Windows server
S0 heeft 6 verbonden devices (zonder S1)  
`Aantal computers + 2 = 2^N`  
6+2 = 2^N -> N=3 -> `8 ip adressen`
3host bits  
netwerk bits -> 32-3=29 -> /29
subnet mask: `11111111.11111111.11111111.11111100`  
`11111000` -> 8+16+32+64+128=248  
subnet mask = `255.255.255.248`

### wat ik tot nu to weet
de ip's van de PC's zijn `192.168.20.3` & `192.168.20.1`  
de laagste ip is het netwerk: `192.168.20.0`  
de broadcast ip is de hoogste ip; `192.168.20.7`  
`192.168.20.2` had een connectie gemaakt met een router.
dus de volgende ip adressen kan ik nog testen met telnet:
- `192.168.20.4`
- `192.168.20.5`
- `192.168.20.6`
> deze ip's krijgen ook `request timed out; remote host not responsing`

op beide server-PT heb ik `telnet 192.168.20.2` geprobeert. hier krijgen ze ook `request timed out`.  
op PC1 kon ik wel een connection maken, maar had ook password nodig voordat ik verder kon

### wat de subnet mask eigenlijk is
op de PC in de config gui zie ik dat de subnet mask `255.255.255.0` is.  
wat ik zonet gedaan heb klopt niet.  
subnet mask = `255.255.255.0`  
netwerk: `192.168.20.0`  
broadcast: `192.168.20.255`  
dus ip `192.168.20.1` t/m `192.168.20.254` zijn bruikbare ip adressen,  
waarvan `192.168.20.3` & `192.168.20.1` de ip's van de pc's zijn  
en `192.168.20.2` een van de routers is.  

## telnet username & passwords uit proberen
ik ben terug gegaan naar les8: basis beveiliging en les17 beveiliging laag 2, en heb de username en passwords van die lessen uitgeprobeerd:
- username: Adnan, password: Welkom01
- username: Packettracer.nl, password: Welkom01

deze waren niet successvol

ip dat het ip eindig met 2 heb ik deze ook geprobeert:
- username: Welkom02, password: Welkom02
- username: Adnan, password: Welkom02
- username: Packettracer.nl, password: Welkom02

en daarna:
- username: Packet, password: tracer
- username: Adnan, password: Adnan
- username: Adnan, password: Adnan01
- username: Adnan, password: Adnan02

deze waren het ook niet
