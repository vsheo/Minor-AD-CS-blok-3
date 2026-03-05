# Risicoanalyse Vanguard
Hier houd ik de volgorde bij van wat ik heb gedaan.
de CLI commando om te controleren welke kwetsbaarheden er zijn

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
> - op beide stitcher staan alle beveiligings opties (die te zijn zijn met `show spannin-tree`) staan uit

---

## DTP (Dynamic Trunking Protocol)
### S0
- `show interfaces switchport` (check per poort of mode "dynamic auto/desirable" is)
  - werkt
- `show interfaces trunk`
  - <img width="1047" height="497" alt="image" src="https://github.com/user-attachments/assets/0ef79185-d452-4bcb-a7b7-ab36473108f5" />

> gevonden
> - poort Po1 en fa0/1 hebben trunking op default vlan
> - Actieve VLANs: default, 0010 en 0020

### S1
- `show interfaces switchport`
  - werkt
- `show interfaces trunk`
  - <img width="1063" height="605" alt="image" src="https://github.com/user-attachments/assets/9946aa95-c694-4012-9be0-1845ff56980e" />

> gevonden
> - poort Po1, fa0/1 en fa0/6 hebben trunking op default vlan
> - Actieve VLANs: default, 0010 en 0020

> gevonden
> - S1 Fa0/6: staat op auto. dit betekent dat deze poort automatisch een trunk vormt als de andere kant DTP-berichten stuurt
> - fa0/5, fa0/9 - 24, gig0/1 en gig0/2 staan ook op auto

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

> gevonden
> - overzicht van welke poorten op welke vlan zit
> - vlan 10 -> 1 poort -> fa0/2
> - vlan 20 -> 2 poorten -> fa0/3 en fa0/4
> - vlan 1 -> heeft alle andere poorten -> waarschijnlijk ongebruikt


---

## VTP (VLAN Trunking Protocol)
### S0
- `show vtp status`
  - <img width="1419" height="539" alt="image" src="https://github.com/user-attachments/assets/9149c0c9-2c33-4ca4-9169-2bc20eed9591" />
- `show vtp password`
  - Invalid input
  - <img width="567" height="81" alt="image" src="https://github.com/user-attachments/assets/1c78d599-c04b-4a27-aa4b-725b5f56d584" />


### S1
- `show vtp status`
  - <img width="1191" height="512" alt="image" src="https://github.com/user-attachments/assets/96f8f853-256c-4c8e-9afe-1f19a046e1af" />
- `show vtp password`
  - Invalid input
  - <img width="582" height="90" alt="image" src="https://github.com/user-attachments/assets/304a17bb-a26a-4e4a-bcb2-8838e1001041" />


> gevonden
> - S0 -> VTP Server, S1 -> VTP Client
> - VTP Pruning: Disabled — alle VLANs worden over alle trunks gestuurd
> - geen vtp password -> aanvaller kan een eigen switch aansluiten

---

## BPDU Guard
### S0 & S1
SNMP had ik al gezien dat de `show running-config` commands niet werken, dus deze zijn niet mogelijk:
- `show running-config | include bpduguard`
- `show running-config | include guard`

`show running-config | include guard`
<img width="792" height="65" alt="image" src="https://github.com/user-attachments/assets/4f993906-2d75-4052-ad43-931c4fa462d8" />  

nadat password had gevonden:  
<img width="806" height="90" alt="image" src="https://github.com/user-attachments/assets/f703f056-4dfb-449a-a07b-acd0bda12143" />  
<img width="805" height="89" alt="image" src="https://github.com/user-attachments/assets/afae3288-22c6-4a60-82c4-d22992b250ed" />

<img width="690" height="71" alt="image" src="https://github.com/user-attachments/assets/450aa1e2-feee-4766-8823-a85fd816eb73" />  
<img width="657" height="59" alt="image" src="https://github.com/user-attachments/assets/9b040c72-72f0-4a62-8cce-021243fbb415" />


> gevonden
> - `show running-config | include bpduguard` toont niets op S0 en S1 → geen BPDU Guard
> - `show running-config | include guard` toont op beide switches: `username Vanguard privilege 1 password 0 Vanguard`
>   - gebruikersaccount: username "Vanguard", password "Vanguard" in plain text

---

## EtherChannel
### S0
- `show etherchannel summary`
  - <img width="903" height="547" alt="image" src="https://github.com/user-attachments/assets/99917747-3c85-4f50-b44d-92a77cbfad99" />
- `show etherchannel load-balance`
  - Invalid input
  - <img width="888" height="164" alt="image" src="https://github.com/user-attachments/assets/e2e42a82-8858-4adc-b5f3-98d56d8f9fcd" />

### S1
- `show etherchannel summary`
  - <img width="900" height="550" alt="image" src="https://github.com/user-attachments/assets/5f1488f3-272d-4136-bf9e-c9e0fcc510f3" />
- `show etherchannel load-balance`
  - Invalid input
  - <img width="891" height="166" alt="image" src="https://github.com/user-attachments/assets/b792128b-24fb-4ff3-952c-996387931880" />

> gevonden
> - EtherChannel is geconfigureerd tussen S0 en S1 via PAgP
> - Load-balancing methode = src-mac -> dit is de standaard instelling en niet optimaal

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
  - <img width="714" height="122" alt="image" src="https://github.com/user-attachments/assets/10523450-bf2e-47ea-a71d-32c4eee2aa59" />
- `show ip interface brief`
  - <img width="1266" height="278" alt="image" src="https://github.com/user-attachments/assets/9419e9c4-fe6d-4033-9aea-78acba35ee0d" />

### R2
- `show running-config | include dot1q`
  - Invalid input
  - <img width="733" height="107" alt="image" src="https://github.com/user-attachments/assets/8ab30e99-f701-4dc4-ac48-09ac6ce62297" />
- `show ip interface brief`
  - <img width="1262" height="274" alt="image" src="https://github.com/user-attachments/assets/7ce3db4f-415a-4baa-9d36-09196ed0bb92" />

> gevonden
> - S0 & S1: `show running-config | include encapsulation` toont niets — switches doen automatisch 802.1q
> - R1& R2: `encapsulation dot1Q 10` en `encapsulation dot1Q 20` — router-on-a-stick bevestigd
> - native VLAN = 1 op alle trunk poorten (S0, S1) — standaard en onveilig
> - VLANs allowed on trunk: 1-1005 — veel meer dan nodig, alleen 1, 10 en 20 zijn actief


---

## Telnet vs SSH
### R1, R2, S0 & S1
`show running-config` werkt niet dus deze command kunnen niet uigevoerd worden:
- `show running-config | section line vty`
- `show running-config | include transport`

- R1
  - <img width="686" height="310" alt="image" src="https://github.com/user-attachments/assets/670571f0-6251-4c67-ac74-32525c887e2b" />
- R2
  - <img width="704" height="238" alt="image" src="https://github.com/user-attachments/assets/bc65afde-7f99-4d13-b320-e5532d4a7ea2" />
- S0
  - <img width="688" height="302" alt="image" src="https://github.com/user-attachments/assets/1fd5e444-d924-4bb6-aa98-d1dd689f21b6" />
- S1
  - <img width="695" height="303" alt="image" src="https://github.com/user-attachments/assets/21a83973-397e-403e-a03a-91fd3e75d045" />

op PC0 `telnet 192.168.20.2` -> username & password: Vanguard  
<img width="937" height="403" alt="image" src="https://github.com/user-attachments/assets/0f00309b-692e-4e43-a62d-c3064f2b4ca0" />

> gevonden
> - alle apparaten hebben SSH version 1 -> heeft bekende kwetsbaarheden en is onveilig
> - R1 en R2: line vty 0 4 met `login local` — gebruiken lokale gebruikersdatabase
> - S0: line vty 0 4 en line vty 5 15 met `login` (zonder "local")
>   - `login` zonder "local" = alleen een line password, geen username vereist. dit is minder veilig dan `login local`
> - S1: line vty 0 4 met `login local`, line vty 5 15 met `login`
>   - inconsistent: eerste 5 sessies vereisen username, de rest alleen een password
> - console poort: geen password geconfigureerd op alle apparaten
>   - iemand met fysieke toegang kan direct de CLI openen zonder wachtwoord

---

## HSRP (Hot Standby Router Protocol)
`show standby` werkt niet dus deze command kunnen niet uigevoerd worden:
### R1 & R2
- `show standby`
- `show standby brief`

- R1
  - <img width="1167" height="213" alt="image" src="https://github.com/user-attachments/assets/ad916bba-e2aa-46e6-870c-350631f8bb4b" />
- R2
  - <img width="1199" height="662" alt="image" src="https://github.com/user-attachments/assets/f8d3129d-9e44-4e5a-bdb3-0166c278fa09" />

> gevonden
> - HSRP is ALLEEN geconfigureerd op R2, voor VLAN 20 (Gig0/0.20)
> - Virtual IP: 192.168.20.1 — dit zou de default gateway voor de PC's moeten zijn
> - zonder R1 als standby is er geen failover — als R2 uitvalt, werkt 192.168.20.1 niet meer
> - HSRP is NIET geconfigureerd voor VLAN 10 (servers)
> - geen HSRP authenticatie geconfigureerd
> - Preemption is disabled -> als R2 uitvalt en later terugkomt, neemt hij niet automatisch de Active rol terug
> - PC0 en PC1 hebben default gateway 0.0.0.0 — ze gebruiken het virtual IP 192.168.20.1 niet
>   - de HSRP configuratie is er wel, maar de PC's zijn er niet op ingesteld

---

## OSPF
### R1
- `show ip ospf`
  - <img width="996" height="706" alt="image" src="https://github.com/user-attachments/assets/b8bfcaf1-e3b8-4699-8546-f9ab634380ee" />
- `show ip ospf neighbor`
  - <img width="1390" height="160" alt="image" src="https://github.com/user-attachments/assets/78d5fe4e-1059-4039-8a95-bf27a7521410" />
- `show running-config | section router ospf`
  - Invalid input
  - <img width="702" height="189" alt="image" src="https://github.com/user-attachments/assets/1e7bef0b-da51-45c0-9e9c-d1961d80969c" />

### R2
- `show ip ospf`
  - <img width="981" height="697" alt="image" src="https://github.com/user-attachments/assets/35e0859f-876a-4873-a9f7-e94be9782283" />
- `show ip ospf neighbor`
  - wordt uitgevoerd maar laat niets zien
- `show running-config | section router ospf`
  - Invalid input
  - <img width="718" height="194" alt="image" src="https://github.com/user-attachments/assets/e89a70c4-5968-44d4-87e6-ef71f7c61d33" />

> gevonden
> - OSPF process 1 actief op beide routers -> in Area 0
> - R1 netwerken: 10.1.1.0/30, 192.168.10.0/24, 192.168.20.0/24
> - R2 netwerken: 10.1.2.0/30, 192.168.10.0/24, 192.168.20.0/24
> - R1 WAN-link: 10.1.1.0/30 (Gig0/1/0 = 10.1.1.2, maar interface is DOWN)
> - R2 WAN-link: 10.1.2.0/30 (Gig0/0/0 = 10.1.2.2, maar interface is DOWN)
> - Area has no authentication op beide routers
> - wildcard masks:
>   - 10.1.1.0 met 0.0.0.3 = /30 subnet (correct voor point-to-point WAN)
>   - 192.168.10.0 en 192.168.20.0 met 0.0.0.255 = /24 subnet (de berekening van in het begin was goed)

---

## UDLD (Unidirectional Link Detection)
### S0 & S1
- `show udld`
  - Invalid input

> gevonden
> - UDLD wordt niet ondersteund in deze Packet Tracer versie

---

## Routing
### R1
- `show ip route`
  - <img width="1254" height="526" alt="image" src="https://github.com/user-attachments/assets/65683ae5-ad31-4943-a40a-ebd8f149480e" />
- `show running-config | include ip route`
  - leeg

### R2
- `show ip route`
  - <img width="1236" height="512" alt="image" src="https://github.com/user-attachments/assets/613cf001-55c9-4cd9-93fa-1656262ad242" />
- `show running-config | include ip route`
  - leeg

> gevonden
> - er is geen default route geconfigureerd

---

## HTTP
### R1, R2, S0 & S1
- `show running-config | include ip http`
  - alles leeg

> gevonden
> - er is geen HTTP-server actief op de routers en switches

---

## DHCP
### R1
- `show ip dhcp pool`
  - <img width="1271" height="765" alt="image" src="https://github.com/user-attachments/assets/4254d80a-3080-4421-b26e-4f6c420e9c00" />
- `show ip dhcp binding`
  - DHCPD: No such pool: binding
  - <img width="1180" height="345" alt="image" src="https://github.com/user-attachments/assets/ff8018fc-1d2e-49c8-a6aa-a796b400ded4" />
- `show running-config | section dhcp`
  - Invalid input
  - <img width="616" height="162" alt="image" src="https://github.com/user-attachments/assets/3db114c5-739d-4a17-8dce-961fb2f9e19e" />

### R2
- `show ip dhcp pool`
  - <img width="1251" height="755" alt="image" src="https://github.com/user-attachments/assets/4b22621f-0bf4-487c-83db-4114cd0b4fec" />
- `show ip dhcp binding`
  - DHCPD: No such pool: binding
  - <img width="1110" height="90" alt="image" src="https://github.com/user-attachments/assets/f3abc094-7bbb-4b90-9448-8bcfd2c3bfde" />
- `show running-config | section dhcp`
  - Invalid input
  - <img width="867" height="303" alt="image" src="https://github.com/user-attachments/assets/30e7b9f2-1b13-4f1c-9127-9bba80072d4b" />

> gevonden
> - beide routers zijn DHCP-servers voor dezelfde netwerken -> kan conflicten veroorzaken
> - R1 DHCP configuratie is INCOMPLEET -> geen `default-router` en geen `excluded-address`
> - R2 DHCP configuratie is WEL compleet
>   - default-router 192.168.10.1 voor VLAN10, default-router 192.168.20.1 voor VLAN20
>   - excluded-addresses: 192.168.10.1-11, 192.168.10.253-254, 192.168.20.1-3
> - R1 heeft 2 adressen uitgedeeld: 192.168.20.1 en 192.168.20.3 -> PC1 en PC1
> - R2 heeft 0 adressen uitgedeeld
> - geen DHCP snooping geconfigureerd op de switches
>   - een aanvaller kan een eigen DHCP-server opzetten

---

## ik heb toevalig dit gezien in DLO
<img width="1122" height="389" alt="image" src="https://github.com/user-attachments/assets/b5eca17b-7084-4f05-bb7a-757a23955c84" />

... ...  

<img width="214" height="122" alt="image" src="https://github.com/user-attachments/assets/596b4908-9510-4970-948e-9c15d6d07054" />

...

---


