# Packet Tracer CLI & Geavanceerde Router/Switch Configuratie - Samenvatting

---

## 1. CLI (Command Line Interface)
- GUI is makkelijk om te leren, CLI is realistischer en krachtiger.
- Toegang tot CLI:
  - Verbind via consolekabel (admin-pc → switch/router)
  - Open terminal op PC → instellingen laten zoals ze zijn → OK
- Modusniveaus:
  | Modus | Prompt | Mogelijkheden |
  |-------|--------|---------------|
  | User | Switch> | Enkel basis show commando’s |
  | Privileged | Switch# | Alle show commando’s + configuratie starten |
  | Configuration | Switch(config)# | Apparaten en interfaces configureren |
  | Interface | Switch(config-if)# | Poorten configureren (speed, duplex, shutdown) |

- Handige commando’s:
  - enable: ga van user naar privileged modus
  - configure terminal / conf t: ga naar configuratiemodus
  - interface FastEthernet 0/x: selecteer een poort om te configureren
  - shutdown / no shutdown: poort uit / aan
  - speed 10 / speed 100: poortsnelheid instellen
  - duplex half / duplex full: half / full duplex instellen
  - show running-config: toon huidige configuratie
  - hostname <naam>: pas de hostnaam aan
  - show ip interface brief: overzicht van poorten en IP-status
  - reload: herstart apparaat
  - copy running-config startup-config: sla configuratie op
  - write erase: reset configuratie

---

## 2. Router Configuratie (Basis)
- IP-adressen instellen op interfaces:
  - R0> enable
  - R0# configure terminal
  - R0(config)# interface FastEthernet0/0
  - R0(config-if)# ip address 192.168.1.1 255.255.255.0
  - R0(config-if)# no shutdown
- Serial interface extra: clock-rate nodig voor router-naar-router verbinding:
  - R0(config)# interface Serial0/1/0
  - R0(config-if)# ip address 192.168.2.1 255.255.255.0
  - R0(config-if)# clock rate 64000
  - R0(config-if)# no shutdown
- Hostnaam instellen: hostname R0

---

## 3. Static Routing
- Nodig om routers te leren onbekende netwerken te bereiken
- Commando: ip route <network-ID> <subnet-mask> <next-hop-IP>
- Voorbeeld:
  - R0(config)# ip route 192.168.3.0 255.255.255.0 192.168.2.2
  - R1(config)# ip route 192.168.1.0 255.255.255.0 192.168.2.1
- Controle: show ip route toont welke netwerken bekend zijn

---

## 4. Beveiliging van apparaten
1. Console-wachtwoord:
   - line console 0
   - login
   - password Welkom01
2. Telnet-wachtwoord / remote login:
   - line vty 0 4
   - login local
   - username Adnan password Welkom01
3. Enable-password (privileged mode):
   - enable password Welkom01
- Test: console / telnet vraagt eerst login, daarna enable password

---

## 5. Show Commando’s (Monitoren)
| Commando | Functie |
|----------|---------|
| show version | IOS-versie en apparaatinfo |
| show mac address-table | Verbonden MAC-adressen |
| show arp | IP ↔ MAC koppeling |
| show ip interface brief | Overzicht interfaces en status |
| show history | Voorgaande commando’s |
| show tech-support | Alles in 1 overzicht (versie, config, interfaces) |
| show users | Ingelogde gebruikers |
| show ip route | Routing table |

- In configuratiemodus gebruik: do <show-commando>

---

## 6. Back-up configuratie via FTP
- Back-up running-config naar FTP-server:
  - Router> enable
  - Router# configure terminal
  - Router(config)# ip ftp username cisco
  - Router(config)# ip ftp password cisco
  - Router(config)# do copy running-config ftp:
- Herstel: copy ftp: running-config

---

## 7. Router als DHCP-server
- DHCP geeft automatisch IP-adressen uit:
  - Router> enable
  - Router# configure terminal
  - Router(config)# ip dhcp pool Adressen
  - Router(dhcp-config)# network 192.168.1.0 255.255.255.0
  - Router(dhcp-config)# default-router 192.168.1.1
- Controle: show ip dhcp binding toont toegewezen IP’s
- Remote DHCP via router (ip helper-address):
  - R2(config)# interface fa0/0
  - R2(config-if)# ip helper-address 192.168.1.1
- Hiermee worden broadcast DHCP-verzoeken omgezet naar unicast naar de DHCP-server

---

## 8. Praktische tips CLI
- Leer modusniveaus goed: User → Privileged → Config → Interface
- Gebruik ? om beschikbare commando’s te zien
- Save configuratie: copy running-config startup-config
- Test connectiviteit:
  - ping <IP>: check of apparaat bereikbaar is
  - tracert <IP>: volg pakketpad door netwerk
- DHCP dynamisch, statisch IP handmatig instellen
- Beveiliging: Console, Telnet en Enable passwords altijd instellen
