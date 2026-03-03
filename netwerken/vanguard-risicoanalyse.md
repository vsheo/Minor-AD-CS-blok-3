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
- ping default gateway: `ping 192.168.10.1`
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

---

## Hulpmiddel uit week 2 slide
in de powerpoint slides van week 2 stond dit:  
<img width="980" height="357" alt="image" src="https://github.com/user-attachments/assets/36dc216e-7b0b-4847-bedc-21d0e0ea6942" />

nu zal ik gericht op deze dingen gaan zoeken/testen in packettracer

## CDP (Cisco Discovery Protocol)
### R1
- `show cdp`
  - <img width="694" height="152" alt="image" src="https://github.com/user-attachments/assets/1105924b-019e-4e9e-9a4e-95010a11cda1" />
- `show cdp neighbors` & `show cdp neighbors detail` laten niks zien
  - <img width="1198" height="214" alt="image" src="https://github.com/user-attachments/assets/987e08fc-80f5-46fe-8ff1-46665dd2b6d4" />


### R2
- `show cdp`
  - <img width="719" height="158" alt="image" src="https://github.com/user-attachments/assets/4315b9ae-8bb3-4bdb-81ca-ded2c57ae62d" />
- `show cdp neighbors`
  - <img width="1175" height="212" alt="image" src="https://github.com/user-attachments/assets/e1de4d98-5430-417e-b926-0dde82ad844d" />
- `show cdp neighbors detail`
  - <img width="1203" height="1029" alt="image" src="https://github.com/user-attachments/assets/51a461f1-f7de-4add-ac1d-04c3b5815628" />



## S0
- `show cdp`
  - <img width="694" height="148" alt="image" src="https://github.com/user-attachments/assets/19410522-fb48-475e-a393-09d1d7fd1309" />
- `show cdp neighbors`
  - <img width="1216" height="394" alt="image" src="https://github.com/user-attachments/assets/716675b0-5f01-44ae-b757-39427ab02a25" />
- `show cdp neighbors detail`
  - werkt

### S1
- `show cdp`
  - <img width="707" height="137" alt="image" src="https://github.com/user-attachments/assets/a093b640-8b93-431d-906d-890152173717" />
- `show cdp neighbors`
  - <img width="1170" height="276" alt="image" src="https://github.com/user-attachments/assets/087f3f24-6dc5-4746-b4c2-f41c95f0161b" />
- `show cdp neighbors detail`
  - werkt

> **Risico:** CDP staat aan en lekt netwerkinformatie (IP's, IOS-versie, platform). Een aanvaller kan hiermee de topologie achterhalen.

---

## LLDP (Link Layer Discovery Protocol)
[lldp commands](https://www.cisco.com/c/en/us/td/docs/routers/nfvis/switch_command/b-nfvis-switch-command-reference/b-nfvis-switch-command-reference_chapter_010000.html)

### R1
- `show lldp`
  - <img width="1091" height="490" alt="image" src="https://github.com/user-attachments/assets/7fec850b-c6a3-453d-af30-3b7272762daa" />

### R2
- `show lldp`
  - <img width="1084" height="513" alt="image" src="https://github.com/user-attachments/assets/6160e3a9-32d9-4815-a35a-78317da980f6" />

### S0
- `show lldp`
  - <img width="1093" height="573" alt="image" src="https://github.com/user-attachments/assets/8d44fe24-495e-46d8-a4a1-6847180140c2" />

### S1
- `show lldp`
  - <img width="1092" height="567" alt="image" src="https://github.com/user-attachments/assets/4c25232f-90db-4b23-b41b-521ef03aed93" />

> **Risico:** Zelfde als CDP, lekt netwerkinformatie naar aanvallers.

---

## SNMP
### R1
`show running-config | include snmp`, `show snmp` & `show snmp community` kunnen niet uitgevoerd worden.  
met `show ?` heb ik gecontroleerd, deze commands staan niet in de lijst

### R2
`show running-config | include snmp`, `show snmp` & `show snmp community` kunnen niet uitgevoerd worden.  
met `show ?` heb ik gecontroleerd, deze commands staan niet in de lijst

### S0
`show running-config | include snmp`, `show snmp` & `show snmp community` kunnen niet uitgevoerd worden.  
met `show ?` heb ik gecontroleerd, deze commands staan niet in de lijst

### S1
`show running-config | include snmp`, `show snmp` & `show snmp community` kunnen niet uitgevoerd worden.  
met `show ?` heb ik gecontroleerd, deze commands staan niet in de lijst

---

## STP (Spanning Tree Protocol)
### S0
- `show spanning-tree`
  - werkt
- `show spanning-tree summary`
  - <img width="1137" height="648" alt="image" src="https://github.com/user-attachments/assets/ffb61988-e4fb-4b04-90fb-afffd7ebc0af" />

### S1
- `show spanning-tree`
  - werkt
- `show spanning-tree summary`
  - <img width="1150" height="640" alt="image" src="https://github.com/user-attachments/assets/3af099d3-faa3-43f1-9676-14e85c829d12" />


---

## DTP (Dynamic Trunking Protocol)
### S0
- `show interfaces switchport` (check per poort of mode "dynamic auto/desirable" is)
  - werkt
- `show interfaces trunk`
  - <img width="1047" height="497" alt="image" src="https://github.com/user-attachments/assets/0ef79185-d452-4bcb-a7b7-ab36473108f5" />

### S1
- `show interfaces switchport`
  - werkt
- `show interfaces trunk`
  - <img width="1063" height="605" alt="image" src="https://github.com/user-attachments/assets/9946aa95-c694-4012-9be0-1845ff56980e" />


---

## VLAN
### S0
- `show vlan`
  - werkt
- `show vlan brief`
  - <img width="1254" height="456" alt="image" src="https://github.com/user-attachments/assets/bc1029dd-49e4-4685-bc75-bc978f50c9b6" />


### S1
- `show vlan`
  - werkt
- `show vlan brief`
  - <img width="1240" height="458" alt="image" src="https://github.com/user-attachments/assets/7557b0fe-a822-4dd2-8733-bb5a7e51da14" />


---

## VTP (VLAN Trunking Protocol)
### S0
- `show vtp status`
  - <img width="1419" height="539" alt="image" src="https://github.com/user-attachments/assets/9149c0c9-2c33-4ca4-9169-2bc20eed9591" />
- `show vtp password`
  - Invalid input

### S1
- `show vtp status`
  - <img width="1191" height="512" alt="image" src="https://github.com/user-attachments/assets/96f8f853-256c-4c8e-9afe-1f19a046e1af" />
- `show vtp password`
  - Invalid input

---

## BPDU Guard
### S0 & S1
SNMP had ik al gezien dat de `show running-config` commands niet werken, dus deze zijn niet mogelijk:
- `show running-config | include bpduguard`
- `show running-config | include guard`

---

## EtherChannel
### S0
- `show etherchannel summary`
  - <img width="903" height="547" alt="image" src="https://github.com/user-attachments/assets/99917747-3c85-4f50-b44d-92a77cbfad99" />
- `show etherchannel load-balance`
  - Invalid input

### S1
- `show etherchannel summary`
  - <img width="900" height="550" alt="image" src="https://github.com/user-attachments/assets/5f1488f3-272d-4136-bf9e-c9e0fcc510f3" />
- `show etherchannel load-balance`
  - Invalid input

---

## DOT1Q / Trunking
### S0
- `show interfaces trunk`
  - <img width="1074" height="489" alt="image" src="https://github.com/user-attachments/assets/02801693-dee1-470e-9157-4fa6c69d66db" />
- `show running-config | include encapsulation`
  - Invalid input

### S1
- `show interfaces trunk`
  - <img width="1074" height="604" alt="image" src="https://github.com/user-attachments/assets/10805d18-fbd3-46a1-bb2f-e532da2fd177" />
- `show running-config | include encapsulation`
  - Invalid input

### R1
- `show running-config | include dot1q`
  - Invalid input
- `show ip interface brief`
  - <img width="1266" height="278" alt="image" src="https://github.com/user-attachments/assets/9419e9c4-fe6d-4033-9aea-78acba35ee0d" />


### R2
- `show running-config | include dot1q`
  - Invalid input
- `show ip interface brief`
  - <img width="1262" height="274" alt="image" src="https://github.com/user-attachments/assets/7ce3db4f-415a-4baa-9d36-09196ed0bb92" />


---

## Telnet vs SSH
### R1, R2, S0 & S1
`show running-config` werkt niet dus deze command kunnen niet uigevoerd worden:
- `show running-config | section line vty`
- `show running-config | include transport`


---

## HSRP (Hot Standby Router Protocol)
`show standby` werkt niet dus deze command kunnen niet uigevoerd worden:
### R1 & R2
- `show standby`
- `show standby brief`

---

## OSPF
### R1
- `show ip ospf`
  - <img width="996" height="706" alt="image" src="https://github.com/user-attachments/assets/b8bfcaf1-e3b8-4699-8546-f9ab634380ee" />
- `show ip ospf neighbor`
  - <img width="1390" height="160" alt="image" src="https://github.com/user-attachments/assets/78d5fe4e-1059-4039-8a95-bf27a7521410" />
- `show running-config | section router ospf`
  - Invalid input

### R2
- `show ip ospf`
  - <img width="981" height="697" alt="image" src="https://github.com/user-attachments/assets/35e0859f-876a-4873-a9f7-e94be9782283" />
- `show ip ospf neighbor`
  - wordt uitgevoerd maar laat niets zien
- `show running-config | section router ospf`
  - Invalid input


---

## UDLD (Unidirectional Link Detection)
### S0 & S1
- `show udld`
  - Invalid input

---

## Routing
### R1
- `show ip route`
  - <img width="1254" height="526" alt="image" src="https://github.com/user-attachments/assets/65683ae5-ad31-4943-a40a-ebd8f149480e" />
- `show running-config | include ip route`
  - Invalid input

### R2
- `show ip route`
  - <img width="1236" height="512" alt="image" src="https://github.com/user-attachments/assets/613cf001-55c9-4cd9-93fa-1656262ad242" />
- `show running-config | include ip route`
  - Invalid input


---

## HTTP
### R1, R2, S0 & S1
- `show running-config | include ip http`
  - Invalid input

---

## DHCP
### R1
- `show ip dhcp pool`
  - <img width="1271" height="765" alt="image" src="https://github.com/user-attachments/assets/4254d80a-3080-4421-b26e-4f6c420e9c00" />
- `show ip dhcp binding`
  - DHCPD: No such pool: binding
- `show running-config | section dhcp`
  - Invalid input

### R2
- `show ip dhcp pool`
  - <img width="1251" height="755" alt="image" src="https://github.com/user-attachments/assets/4b22621f-0bf4-487c-83db-4114cd0b4fec" />
- `show ip dhcp binding`
  - DHCPD: No such pool: binding
- `show running-config | section dhcp`
  - Invalid input







