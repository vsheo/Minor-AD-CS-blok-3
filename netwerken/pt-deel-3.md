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
  - Subinterfaces aanmaken: `interface fa0/0.10`, `encapsulation dot1q 10`
  - IP-adres instellen: `ip address 192.168.1.1 255.255.255.0`
  - Switchinterface naar trunk: `switchport mode trunk`

## 4. VTP (VLAN Trunking Protocol)
- VLAN-gegevens centraliseren via VTP.
- **S0 (Server):**
  - `vtp mode server`
  - `vtp domain Packettracer.nl`
  - `vtp password Welkom01`
  - VLAN aanmaken: `vlan 10`, `name Tien`, `vlan 20`, `name Twintig`
- **S1 (Transparent):** alleen doorgeven, geen lokale database
- **S2 (Client):** ontvangt VLAN-data van Server
- **Debug commando:** `debug sw-vlan vtp events`
- Show-commando: `show vlan`

## 5. Netwerkberichten
- **Unicast:** 1 apparaat → 1 apparaat
- **Multicast:** 1 → groep apparaten
- **Broadcast:** 1 → alle apparaten
- Loops voorkomen met **STP** (Spanning-Tree Protocol)
  - Verkiezing root: laagste `priority + MAC-address`
  - Poortmodi: Root, Alternative, Designated, Disabled
  - Show: `show spanning-tree`, `show spanning-tree summary`
  - Cost per link: 10Mbit=100, 100Mbit=19, 1Gbit=4
  - Root aanpassen: `spanning-tree vlan 1 root primary/secondary`

## 6. Netwerksnelheden
- Standaard: 10Mbit, 100Mbit, 1Gbit, 10Gbit
- Bottlenecks door te weinig capaciteit tussen switches
- **Oplossing:** EtherChannel

## 7. EtherChannel
- Combineert meerdere lijnen tot één logische verbinding
- Drie typen:
  - **LACP:** `channel-protocol lacp`, `mode active/passive`
  - **PAgP:** `channel-protocol pagp`, `mode desirable/auto`
  - **On:** geen overleg, direct bundelen
- Commando’s:
  - `interface port-channel 1`
  - `interface range Fa0/1-5`
  - `channel-group 1 mode <type>`
- Show: `show etherchannel summary`, `show etherchannel load-balance`
- Load balancing: `port-channel load-balance <optie>`

## 8. Multilayer Switch (MLS)
- Combineert router en switch functionaliteit
- Poort als switchpoort of routingpoort
- Geen seriële verbinding
- IP-adres instellen: `no switchport` + `ip address <ip> <mask>`
- Routing inschakelen: `ip routing`

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

