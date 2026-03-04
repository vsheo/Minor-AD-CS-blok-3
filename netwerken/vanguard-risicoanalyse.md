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

---

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

> gevonden:
> - R2 heeft is verbonden met S0 en S1
> - poort S1 poort gig0/1 gaat naar fa0/2
> - poort S1 poort gig0/0 gaat naar fa0/2
> - S1 ip: `192.168.10.253`
> - S0 ip: `192.168.10.254`
>   - telnet geprobeer naar deze 2 ip's via server en pc's -> connection timed out; host not respponding
> - IOS versie 15.0(2)SE4

### S0
- `show cdp`
  - <img width="694" height="148" alt="image" src="https://github.com/user-attachments/assets/19410522-fb48-475e-a393-09d1d7fd1309" />
- `show cdp neighbors`
  - <img width="1216" height="394" alt="image" src="https://github.com/user-attachments/assets/716675b0-5f01-44ae-b757-39427ab02a25" />
- `show cdp neighbors detail`
  - werkt

> gevonden:
> - ik zie hier terug dat S0 verbonden is met R2 via fa0/2
> - ik zie ook dat R1 en R2 subinterfaces hebben (gig0/0.10, gig0/0.20)
> - R2 is router on a stick (dot1q encapsulation)

### S1
- `show cdp`
  - <img width="707" height="137" alt="image" src="https://github.com/user-attachments/assets/a093b640-8b93-431d-906d-890152173717" />
- `show cdp neighbors`
  - <img width="1170" height="276" alt="image" src="https://github.com/user-attachments/assets/087f3f24-6dc5-4746-b4c2-f41c95f0161b" />
- `show cdp neighbors detail`
  - werkt

> gevonden:
> - beide switches laten info van de neighbors zien

---

## LLDP (Link Layer Discovery Protocol)
[lldp commands](https://www.cisco.com/c/en/us/td/docs/routers/nfvis/switch_command/b-nfvis-switch-command-reference/b-nfvis-switch-command-reference_chapter_010000.html)

### R1
- `show lldp`
  - <img width="1091" height="490" alt="image" src="https://github.com/user-attachments/assets/7fec850b-c6a3-453d-af30-3b7272762daa" />

> gevonden:
> - LLDP status: active
> - neighbor is S0 via poort fa0/1

### R2
- `show lldp`
  - <img width="1084" height="513" alt="image" src="https://github.com/user-attachments/assets/6160e3a9-32d9-4815-a35a-78317da980f6" />

> gevonden:
> - LLDP status: active
> - neighbor is S0 via poort fa0/2 (vanuit Gig0/0 op R2)
> - neighbor is ook S1 via poort fa0/2 (vanuit Gig0/1 op R2)

### S0
- `show lldp`
  - <img width="1093" height="573" alt="image" src="https://github.com/user-attachments/assets/8d44fe24-495e-46d8-a4a1-6847180140c2" />

> gevonden:
> - LLDP status: active
> - S1 Fa0/8 -> S0 Fa0/6
> - S1 Po1 -> S0 Fa0/8
> - R2 Fa0/2 -> S0 Gig
> - R1 Fa0/1 -> S0 Gig

### S1
- `show lldp`
  - <img width="1092" height="567" alt="image" src="https://github.com/user-attachments/assets/4c25232f-90db-4b23-b41b-521ef03aed93" />

> gevonden:
> - LLDP status: active
> - R2 Fa0/2 -> S1 Gig0/1
> - R1 Fa0/1 -> S1 Gig0/1
> - S0 pO1 -> S1 Fa0/7
> - S0 Fa0/6 -> S1 Fa0/8


> - LLDP is active op R!, R2, S0 & S1
> - met `sh lldp neighbors` kunnen we zien via welke poort de routers en switcher verbonden zijn
> - een aanvaller kan hiermee het heel nbetwerk structuur achterhalen
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

### met password cisco
nu dat ik de password heb gevonden kan ik `show running-config` wel uit voeren maar als ik `| include snmp` erbij zet zie ik niets.  

<img width="658" height="605" alt="image" src="https://github.com/user-attachments/assets/79d5b2f6-7bee-4631-bde7-e1de4c2776c3" />

> gevonden
> - `show running-config | include snmp` laat niks zien, waarschijnlijk is die niet geconfigureerd


---

## STP (Spanning Tree Protocol)
### S0
- `show spanning-tree`
  - werkt
- `show spanning-tree summary`
  - <img width="1137" height="648" alt="image" src="https://github.com/user-attachments/assets/ffb61988-e4fb-4b04-90fb-afffd7ebc0af" />

> gevonden
> - heeft toegang tot de vlan default, vlan0010 en vlan 0020
> - vlan default heeft 6 ips om het subnet
> - vlan0010 heeft 5 ips om het subnet
> - vlan 0020 heeft 6 ips om het subnet

### S1
- `show spanning-tree`
  - werkt
- `show spanning-tree summary`
  - <img width="1150" height="640" alt="image" src="https://github.com/user-attachments/assets/3af099d3-faa3-43f1-9676-14e85c829d12" />

> gevonden
> - heeft toegang tot de vlan default, vlan0010 en vlan 0020
> - vlan default heeft 4 ip's om het subnet maar 2 worden geblokeert
> - vlan0010 heeft 5 ip's om het subnet maar 2 worden geblokeert
> - vlan 0020 heeft 6 ip's om het subnet maar 2 worden geblokeert


> gevonden
> - op beide stitcher staan alle beveiligings opties (die te zijn zijn met `show spannin-tree`) uit



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
 

---

## ik heb toevalig dit gezien in DLO
<img width="1122" height="389" alt="image" src="https://github.com/user-attachments/assets/b5eca17b-7084-4f05-bb7a-757a23955c84" />
... ...
<img width="214" height="122" alt="image" src="https://github.com/user-attachments/assets/596b4908-9510-4970-948e-9c15d6d07054" />
...

---


# Samenvatting Bevindingen Risicoanalyse Vanguard

## Netwerk overzicht
- 2 subnetten: `192.168.10.0/24` (VLAN10 - servers) en `192.168.20.0/24` (VLAN20 - PC's)
- R1: Gig0/0.10 = `192.168.10.2`, Gig0/0.20 = `192.168.20.2`, Gig0/1/0 = `10.1.1.2` (down)
- R2: Gig0/0.10 = `192.168.10.3`, Gig0/0.20 = `192.168.20.3`, Gig0/0/0 = `10.1.2.2` (down)
- Beide routers gebruiken router-on-a-stick (subinterfaces)
- S0 = VTP Server, S1 = VTP Client, domain "LAB"

---

## Gevonden risico's per protocol

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 1 | R1, R2, S0, S1 — CDP | CDP staat aan op alle apparaten. Lekt IP-adressen, IOS-versie (15.0(2)SE4), platform (2960/C1900) en poortinfo | Aanvaller kan volledige netwerktopologie achterhalen | 4 | 3 | 12 | `no cdp run` globaal, of `no cdp enable` per interface |
| 2 | R1, R2, S0, S1 — LLDP | LLDP staat actief op alle apparaten, toont neighbors met platform en poortinfo | Dubbele informatielekkage naast CDP | 4 | 3 | 12 | `no lldp run` globaal uitschakelen |
| 3 | S0, S1 — STP/BPDU Guard | PortFast BPDU Guard Default = disabled, Root Guard = disabled, Loopguard = disabled op beide switches | Aanvaller kan eigen switch aansluiten en root bridge overnemen, netwerk loops veroorzaken | 3 | 5 | 15 | `spanning-tree portfast bpduguard default`, `spanning-tree guard root` op trunk poorten |
| 4 | S1 — DTP | Fa0/6 staat op mode **auto** (DTP negotiation actief), vormt automatisch trunk | Aanvaller kan via DTP een trunk opzetten en alle VLAN-verkeer onderscheppen (VLAN hopping) | 4 | 5 | 20 | `switchport mode access` + `switchport nonegotiate` op alle access poorten |
| 5 | S0, S1 — VLAN | Veel ongebruikte poorten zitten in VLAN 1 (default) en staan nog aan | Geen segmentatie, onbevoegde toegang via ongebruikte poorten | 3 | 4 | 12 | Ongebruikte poorten in apart VLAN plaatsen + `shutdown` |
| 6 | S0, S1 — VTP | VTP domain "LAB" zonder password (show vtp password = invalid). S0=Server, S1=Client | Aanvaller kan switch aansluiten met hogere revision number en volledige VLAN-database overschrijven/wissen | 3 | 5 | 15 | `vtp password <sterk_wachtwoord>` instellen, of `vtp mode transparent` gebruiken |
| 7 | S0, S1 — Trunking/DOT1Q | Native VLAN = 1 op alle trunk poorten (Po1, Fa0/1, Fa0/6) | VLAN hopping via double-tagging aanval op native VLAN 1 | 3 | 5 | 15 | Native VLAN wijzigen naar ongebruikt VLAN (bv. VLAN 999) |
| 8 | S0-S1 — EtherChannel | PAgP EtherChannel: S0 Fa0/8 = stand-alone (I), S1 Fa0/7 = desirable (D). Mismatch in bundeling | Verminderde redundantie en bandbreedte, niet alle links actief | 2 | 3 | 6 | EtherChannel opnieuw configureren zodat alle poorten (P) status krijgen |
| 9 | R1 — Telnet | Telnet actief op 192.168.20.2, plain text protocol | Wachtwoorden en commando's kunnen worden afgeluisterd op het netwerk | 4 | 5 | 20 | Vervang Telnet door SSH: `transport input ssh` op VTY lines |
| 10 | R1, R2 — OSPF | OSPF actief in Area 0, **geen authenticatie** ("Area has no authentication"). Neighbor state = INIT/DROTHER (niet FULL) | Aanvaller kan valse routes injecteren. OSPF adjacency niet volledig = routing werkt niet correct | 3 | 5 | 15 | OSPF authenticatie instellen: `ip ospf authentication message-digest` |
| 11 | R1, R2 — Routing | Geen default route ingesteld ("Gateway of last resort is not set"), alleen connected routes zichtbaar | Geen internetverbinding, verkeer tussen subnetten faalt | 5 | 5 | 25 | Default route instellen: `ip route 0.0.0.0 0.0.0.0 <next-hop>` |
| 12 | R1, R2 — HSRP | HSRP niet geconfigureerd (show standby niet beschikbaar) | Geen gateway redundantie: als één router uitvalt, verliezen alle clients op dat subnet connectiviteit (single point of failure) | 3 | 4 | 12 | HSRP configureren met authenticatie op beide routers |
| 13 | R1, R2 — DHCP | DHCP pools actief (VLAN10 + VLAN20), geen excluded addresses op R1, geen DHCP snooping | DHCP spoofing: aanvaller kan valse DHCP-server opzetten en verkeer omleiden (man-in-the-middle) | 3 | 5 | 15 | `ip dhcp snooping` inschakelen, trusted ports instellen |
| 14 | AP Medewerkers + Gasten — Wi-Fi | Encryption type = **disabled** op beide access points. Geen WEP/WPA/WPA2, geen wachtwoord | Iedereen kan verbinden met het netwerk en al het draadloze verkeer afluisteren | 5 | 5 | 25 | WPA2-PSK of WPA2-Enterprise instellen met sterk wachtwoord |
| 15 | R1, R2 — Wachtwoorden | `enable password` gebruikt i.p.v. `enable secret`. Onbekend of `service password-encryption` actief is | Wachtwoord mogelijk in plain text zichtbaar in configuratie | 4 | 4 | 16 | Vervang door `enable secret`, activeer `service password-encryption` |
| 16 | PC0, PC1 — Default Gateway | Default gateway = `0.0.0.0` op beide PC's | PC's kunnen niet communiceren buiten hun subnet (verklaart waarom pings naar servers falen) | 5 | 4 | 20 | Default gateway instellen op `192.168.20.2` of `192.168.20.3`, of DHCP gebruiken |
| 17 | S0, S1 — UDLD | UDLD niet beschikbaar/niet geconfigureerd | Unidirectionele links kunnen onopgemerkt blijven en loops of black holes veroorzaken | 2 | 3 | 6 | `udld enable` of `udld aggressive` op relevante interfaces |

---

## Top 5 Kritieke Risico's

1. **Wi-Fi zonder encryptie** (Risicoscore: 25)
   - **Impact:** Iedereen kan verbinden en verkeer afluisteren, inclusief gevoelige bedrijfsdata
   - **Oplossing:** WPA2-PSK of WPA2-Enterprise configureren op beide access points

2. **Geen default route / routing faalt** (Risicoscore: 25)
   - **Impact:** Geen internetverbinding, subnetten kunnen niet met elkaar communiceren
   - **Oplossing:** Default route instellen en OSPF adjacency fixen (INIT → FULL)

3. **Telnet in gebruik (plain text)** (Risicoscore: 20)
   - **Impact:** Inloggegevens en commando's afluisterbaar op het netwerk
   - **Oplossing:** SSH configureren, Telnet uitschakelen met `transport input ssh`

4. **DTP actief op access poorten** (Risicoscore: 20)
   - **Impact:** Aanvaller kan trunk opzetten en alle VLAN-verkeer zien
   - **Oplossing:** `switchport mode access` + `switchport nonegotiate` op alle access poorten

5. **PC's zonder default gateway** (Risicoscore: 20)
   - **Impact:** PC's zijn geïsoleerd van de rest van het netwerk
   - **Oplossing:** Gateway instellen of DHCP correct configureren

---

## Hardening Checklist

| Nr | Maatregel | Status (✓/✗) | Opmerkingen |
|----|-----------|--------------|-------------|
| 1 | Vervang `enable password` door `enable secret` | ✗ | Beide routers + switches |
| 2 | `service password-encryption` activeren | ✗ | Niet te verifiëren zonder privileged access |
| 3 | CDP uitschakelen (`no cdp run`) | ✗ | Staat aan op alle 4 apparaten |
| 4 | LLDP uitschakelen (`no lldp run`) | ✗ | Staat aan op alle 4 apparaten |
| 5 | SSH i.p.v. Telnet (`transport input ssh`) | ✗ | Telnet actief op R1 |
| 6 | BPDU Guard inschakelen op access poorten | ✗ | Disabled op S0 en S1 |
| 7 | DTP uitschakelen (`switchport nonegotiate`) | ✗ | S1 Fa0/6 op auto |
| 8 | Native VLAN wijzigen naar ongebruikt VLAN | ✗ | Native VLAN = 1 overal |
| 9 | Ongebruikte poorten uitschakelen (`shutdown`) | ✗ | Veel poorten actief in VLAN 1 |
| 10 | VTP password instellen | ✗ | Geen password geconfigureerd |
| 11 | OSPF authenticatie configureren | ✗ | "Area has no authentication" |
| 12 | DHCP snooping inschakelen | ✗ | Niet geconfigureerd |
| 13 | WPA2 instellen op beide access points | ✗ | Encryption disabled |
| 14 | Default gateway instellen op PC's | ✗ | Gateway = 0.0.0.0 |







