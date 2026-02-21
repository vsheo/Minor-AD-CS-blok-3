# Samenvatting Netwerken – Deel 3 t/m 17

## 1. Switchgebruik en Netwerklagen
- **Accesslaag:** Eindgebruikers, geen redundantie, loopdetectie belangrijk.
- **Distributielaag:** Verbindt accesslagen, redundant, routers als gateways.
- **Corelaag:** Verbindt distributielagen, “zware” switches, redundantie via EtherChannel.

---

## 2. VLAN’s
- Virtuele scheiding van netwerkverkeer per groep.

broadcast bericht nadoen, door een ping te sturen naar het laatste ip adress op het netwerk: `ping 192.168.1.255`  
alle machines binnen de lan reageren op de ping.  
dit gebeurt in de achtergrond steeds, maar dit wil je niet omdat het teveel data verkeer kost.

dit kan je voorkomen door vlans aan te maken, als een pc nu een broadcast bericht verstuurt dan gaat die niet buiten het vlan netwerk

- **Commando’s:**
  - `vlan 10` -> VLAN 10 aanmaken
  - `name Inkoop` -> naam toewijzen
  - `interface Fa0/1` -> interface selecteren
    - meerdere interfaces tegelijk op een vlan zetten
    - `interface range fa0/1-20` -> fa0/1 t/m fa0/20
  - `switchport access vlan 10` -> interface in VLAN 10 zetten

- **Access vs Trunk:**
  - Access: 1 VLAN, native VLAN standaard 1
  - Trunk: alle VLAN-verkeer, gebruikt voor switch-to-switch verbindingen
- VLAN opslaan in `vlan.dat`; verwijderen met `delete flash:vlan.dat`
- Show-commando’s: `show vlan`, `show ip interface brief`, `show interface switchport`


---

## 3. InterVLAN Routing
- VLAN’s in verschillende subnetten hebben router nodig.
- **Router-on-a-stick:**
  - Subinterfaces aanmaken:
    - `interface fa0/0.10` -> sub interface maken `.10` de naam van de vlan (zonder `.10` was het de hoofd interface)
    - `no shutdown` -> aanzetten
    - `encapsulation dot1q 10` -> truking voor vlan 10 instellen
  - IP-adres instellen:
    - `ip address 192.168.1.1 255.255.255.0`
  - op de Switch interface naar trunk:
    - `switchport mode trunk`

---

## 4. VTP (VLAN Trunking Protocol)
VLAN-gegevens centraliseren via VTP.  
VTP synchroniseert de VLAN database tussen switches binnen hetzelfde VTP-domein

**S0 (Server):** beheer de vlan database
- `vtp mode server` -> switch tot een vlan server maken
- `vtp domain` `Packettracer` -> domein waarin deze switches zitten en vlan data deelen
- `vtp password Welkom01`
- VLAN aanmaken:
  - `vlan 10`, `name Tien`
  - `vlan 20`, `name Twintig`

**S1 (Transparent):** stuurt vlan data door
- `vtp mode transparent`
- `vtp domain` `Packettracer` -> ook hier aangeven voor welke vlan domain doorgestuurd wordt
- `vtp password Welkom01` -> dezelfde pw als op de server

**S2 (Client):** gebruik de vlan data uit de vlan server
- `vtp mode client`
- `vtp domain` `Packettracer` -> moet hetzelfde VTP domain hebben om VLAN updates van de server te ontvangen
- `vtp password Welkom01` -> dezelfde pw als op de server

**Verbinding tussen deze switches moet op trunk staan**

> als je nu op een client switch een vlan probeert aan te maken dan krijg je een bericht dat dat niet kan.  
Vlan's kunnnen nu alleen op de server switch aangemaakt worden

**Debug commando:**
- `debug sw-vlan vtp events`
  - We zullen nu periodiek meldingen zien verschijnen in onze terminal. Als de gegevens op switches niet met elkaar overeenkomen
    - laat zien wat er op de achtergrond gebeurt (wat normaal niet op de cli komt)
    - eerst deze command uit voeren op de transparent switch
    - daarna een nieuwe vlan aan maken in de vlan server switch
    - daarna terug gaan naar de transparent switch. nu zie je vtp berichten door de switch gaan
> Show-commando:  
`show vlan`  
`show vtp status`

---

## 5. Netwerkberichten
- **Unicast:** 1 apparaat → 1 apparaat
  - Een bericht van het ene apparaat naar het andere. Bestemmingsadres is een uniek MAC-adres
- **Multicast:** 1 → groep apparaten
  - Een bericht naar een groep geïnteresseerde apparaten. Deze ‘delen’ een gemeenschappelijk adres
- **Broadcast:** 1 → alle apparaten
  - Een bericht naar iedereen binnen het interne netwerk. Een router is het apparaat dat dit soort berichten tegenhoudt

Loops voorkomen met **STP** (Spanning-Tree Protocol)
- Verkiezing root: als een switch opstart/ aan en uit gaat, dan start een verkiezing voor welke de switch de `root bridge` wordt
  - bepaald door: `priority + MAC-address`
    - de priority is standaard `32769`
    - de laagste MAC address
    - dit wordt tot 1 getal gemaakt, de priority staat vooraan
  - dit kan je beinvloeden door de priority aan te passen
    - `spanning-tree` `vlan 1` `root primary`
      - `root primary` zorgt ervoor dat de priority verlaagd wordt
      - met `show spanning-tree` zie je dat de priority verlaagd is

- Poortmodi: Root, Alternative, Designated, Disabled
- Show: `show spanning-tree`, `show spanning-tree summary`
- Cost per link: 10Mbit=100, 100Mbit=19, 1Gbit=4
- Root aanpassen: `spanning-tree vlan 1 root primary/secondary`

---

## 6. Netwerksnelheden
- Standaard: 10Mbit, 100Mbit, 1Gbit, 10Gbit
- Bottlenecks door te weinig capaciteit tussen switches
- **Oplossing:** EtherChannel

---

## 7. EtherChannel
- Combineert meerdere lijnen tot één logische verbinding
- Drie typen:
  - **LACP:** Link aggregation Control Protocol
    - `channel-protocol lacp`, `mode active/passive`
  - **PAgP:** Port Aggregation Protocol
    - `channel-protocol pagp`, `mode desirable/auto`
  - **On:** geen overleg, direct bundelen

LACP Commands:
- `interface port-channel 1` -> nieuwe EtherChannel groep maken
- `channel-protocol lacp` -> maak gebruik van LACP
- `interface range Fa0/1-5`
- `channel-group 1 mode active`
  - Deze poorten gaan nu actief LACP-berichten versturen om met de overkant een LACP-verbinding op te stellen. Als we aan de andere kant Channel-group 1 mode passive instellen, dan wordt een EtherChannel gevormd.

PAgP Commands:
- `interface port-channel 1`
- `channel-protocol PAgP`
- `interface range Fa0/1-5`
- `channel-group 1 mode desirable`
  - Deze poorten gaan nu actief PAgP-berichten versturen om met de overkant een PAgP-verbinding op te stellen. Als we aan de andere kant Channel-group 1 mode auto instellen, dan wordt een EtherChannel gevormd

On Commands:
- `interface port-channel 1`
- `interface range Fa0/1-5`
- `channel-group 1 mode on`
  - Deze poorten zijn nu gebundeld. Als we aan de andere kant Channel-group 1 mode ON instellen, dan wordt een EtherChannel gevormd

Show: `show etherchannel summary`, `show etherchannel load-balance`
Load balancing: `port-channel load-balance <optie>`

---

## 8. Multilayer Switch (MLS)
- Combineert router en switch functionaliteit
- Poort als switchpoort of routingpoort
- Geen seriële verbinding
- IP-adres instellen: `no switchport` + `ip address <ip> <mask>`
- Routing inschakelen: `ip routing`

---

## 9. Beveiliging Accesslaag
- Risico’s: eigen switch aansluiten, loops, root switch worden, VLAN-database lek, sniffing
- **VTP beveiliging:** `vtp password Welkom01`, `vtp mode server`
- **STP beveiliging:**
  - `spanning-tree bpduguard enable` → BPDU-berichten uitschakelen
  - `spanning-tree guard root` → poort mag geen root worden
- **Port-security:**
  - `switchport mode access`
  - `switchport port-security`
  - `switchport port-security maximum <aantal>`
  - `switchport port-security mac-address <adres>` of `sticky`

---

## 10. Show-commando’s Belangrijk
- `show version` → IOS-versie
- `show mac address-table` → verbonden apparaten
- `show arp` → IP ↔ MAC
- `show ip interface brief` → status interfaces
- `show history` → eerdere commando’s
- `show tech-support` → combo van versie/config/interfaces
- `show users` → ingelogde gebruikers
- `show ip route` → routing table
- Show commando in config-mode: `do <show commando>`

---

## 11. Samengevat
- VLAN’s scheiden netwerkverkeer per afdeling/subnet
- InterVLAN routing nodig voor communicatie tussen VLAN’s
- VTP centraliseert VLAN-configuratie
- STP voorkomt loops in redundante netwerken
- EtherChannel verhoogt capaciteit en redundantie
- MLS kan routeren + switchen op één apparaat
- Port-security, VTP-passwords en STP-opties beveiligen netwerk tegen onbevoegde wijzigingen

## Vragen Voorbeeld
- Show IP Interface Brief → status per interface
- Show Interface Switchport → access/trunk, VLAN
- Show VLAN → VLAN-lijst
- Root switch verkiezing → laagste priority + MAC
- DHCP/Static IP → lease toewijzing
- VTP-mode testen → server, client, transparent
- STP-prioriteit wijzigen → `root primary/secondary`
- EtherChannel status → `show etherchannel summary`

