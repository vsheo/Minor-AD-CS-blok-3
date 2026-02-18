# Packet Tracer (PT) - Volledige Beginner Samenvatting

## 1. Wat is Packet Tracer?
- Simulatieprogramma van Cisco om netwerken te bouwen en testen.  
- Apparaten plaatsen, verbinden en netwerkverkeer simuleren zonder echte hardware.  
- Doel: leren hoe netwerken werken, configureren en fouten oplossen.

## 2. Werkvelden & Interface
- **Logical view:** Alleen netwerkapparatuur zichtbaar, handig voor ontwerp.  
- **Physical view:** Apparatuur op geografische locaties plaatsen, visueel realistischer.  
- **Werkveld:** Apparaten slepen, verbinden, configureren.  
- **Acties:** Verplaatsen, verwijderen, labels toevoegen.  
- **Inspect tool:** Bekijk eigenschappen van apparaten of verbindingen zonder commando’s.  
- **Berichten testen:** Verzend “pakketjes” tussen apparaten om connectiviteit te controleren.  
- **Realtime vs Simulation:**  
  - Realtime = netwerk draait live.  
  - Simulation = volg pakketten stap voor stap; zie waar ze vastlopen.  
- **Scenario’s:** Testresultaten opslaan en meerdere scenario’s vergelijken.  

## 3. Apparaten & Functies
| Apparaat | Laag | Functie | Extra |
|----------|------|---------|-------|
| PC / Laptop | 1-3 | Eindapparaat, verstuurt/vervangt data | Kan DHCP of static IP gebruiken |
| Switch | 2 | Verbindt apparaten in hetzelfde netwerk | Gebruikt MAC-adressen, Full Duplex mogelijk, VLAN instelbaar |
| Router | 3 | Verbindt netwerken, routeert pakketjes | Vereist IP + subnet, serial → clock rate, Static routing mogelijk |
| Access Point | 2/3 | Draadloze verbinding | SSID uitzenden, WPA/WPA2 beveiliging |
| Server | 3 | Web, mail, DHCP, DNS, FTP, AAA | Kan IP-adres uitdelen en services leveren |
| Randapparatuur | 2-3 | Printer, tablet, TV | IP-adres kan worden toegewezen, beperkt gebruik |

## 4. Verbindingen & Kabels
- **Straight-through:** Ongelijke apparaten (PC ↔ Switch).  
- **Cross-over:** Gelijke apparaten (PC ↔ PC, Switch ↔ Switch).  
- **Serial:** Router ↔ Router.  
- **Kleur in PT:**  
  - Groen = werkt  
  - Rood = niet geconfigureerd of fout

### Kabeltypes
| Kabel | Gebruik |
|-------|---------|
| Straight-through | PC ↔ Switch, Server ↔ Switch |
| Cross-over | PC ↔ PC, Switch ↔ Switch |
| Serial | Router ↔ Router |


## 5. IP-adressen & Subnetten
- **IP-adres:** Uniek nummer voor apparaat, zodat apparaten elkaar vinden. Formaat: 192.168.1.1  
- **Subnet mask:** Scheidt network-ID van host-ID. 255 = netwerk, 0 = host  
- **Adresklassen:**  
  - **A:** 1–127 → groot netwerk, subnet 255.0.0.0  
  - **B:** 128–191 → middelgroot, subnet 255.255.0.0  
  - **C:** 192–223 → klein (LAN), subnet 255.255.255.0  
- **Private IP ranges:** Alleen lokaal: 10.x.x.x, 172.16.x.x–172.31.x.x, 192.168.x.x  
- **Static IP:** Handmatig IP + subnet + default gateway instellen  

## 6. Switch-configuratie
- **MAC-adressen:** Unieke fysieke ID van apparaat, gebruikt door switch voor forwarding.  
- **MAC-table:** Lijst met MAC-adressen en poorten, automatisch opgebouwd.  
- **VLAN:** Logische segmentatie van netwerkpoorten.  
- **Speed / Duplex:**  
  - Speed = snelheid van poort (Mbit)  
  - Duplex = Half (1 kant tegelijk) of Full (beide kanten tegelijk)  
- **Full Duplex:** Geen botsingen, beide kanten kunnen tegelijk communiceren.  
- **Auto:** Switch detecteert automatisch instellingen van verbonden apparaat.

## 7. Router-configuratie
- **IP-adres en subnet:** Nodig om netwerk te herkennen en te communiceren.  
- **Serial interfaces:** Vereisen **clock rate** om verbinding te laten werken.  
- **Routing:**  
  - Direct verbonden netwerken = standaard bekend  
  - **Static routing:** Handmatig routes toevoegen naar onbekende netwerken (Next Hop)  
- **Inspect tool:** Bekijk routing-table en status van interfaces.

## 8. DHCP & DNS
- **DHCP-server:** Verdeelt automatisch IP-adressen aan clients, stelt default gateway en DNS in.  
- **DNS-server:** Zet IP-adressen om in hostnamen (bv. 192.168.1.1 → web)  
- **Dynamic IP:** Client krijgt automatisch een adres uit DHCP-pool  
- **Static IP:** Handmatig ingesteld adres

## 9. Servers en Services
- **Webserver:** HTTP/HTTPS, kan eigen HTML hosten  
- **Mailserver:** POP3/SMTP, maakt mailaccounts aan  
- **FTP-server:** Voor bestandsoverdracht  
- **AAA-server:** Beveiliging, authenticatie, autorisatie, accounting  
- **Randapparatuur:** Printer, tablet, TV kan IP gebruiken

| Server | Functie |
|--------|---------|
| DHCP | Verdeel IP-adressen automatisch |
| DNS | Vertaal IP naar naam (bv. web → 192.168.1.1) |
| Web | HTTP/HTTPS, host websites |
| Mail | POP3/SMTP, accounts aanmaken |
| FTP | Bestanden uitwisselen |
| AAA | Beveiliging, authenticatie en autorisatie |

## 10. Wi-Fi
- **Access Point:** Verbindt apparaten draadloos, zendt SSID uit  
- **Pre-shared keys:** Beveiliging via wachtwoord  
- **WEP/WPA:** Zwak, makkelijk te kraken  
- **WPA2:** Sterker, veiliger  
- Apparaten verbinden automatisch bij onveilige SSID

