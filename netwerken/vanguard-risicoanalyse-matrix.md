# 2. Risicoanalyse Matrix

---

## CDP (Cisco Discovery Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 1 | R1, R2, S0, S1 — CDP | CDP staat aan op alle apparaten. Lekt IP-adressen, IOS-versie (15.0(2)SE4), platform (2960/C1900) en poortinfo | Aanvaller kan volledige netwerktopologie achterhalen | 4 | 3 | 12 | `no cdp run` globaal, of `no cdp enable` per interface |

---

## LLDP (Link Layer Discovery Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 2 | R1, R2, S0, S1 — LLDP | LLDP staat actief op alle apparaten, toont neighbors met platform en poortinfo | Dubbele informatielekkage naast CDP | 4 | 3 | 12 | `no lldp run` globaal uitschakelen |

---

## SNMP (Simple Network Management Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| — | R1, R2, S0, S1 — SNMP | `show running-config \| include snmp` toont niets. SNMP is niet geconfigureerd | Geen risico gevonden | — | — | — | — |

---

## STP (Spanning Tree Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 3 | S0, S1 — STP | PortFast BPDU Guard Default = disabled, Root Guard = disabled, Loopguard = disabled op beide switches | Aanvaller kan eigen switch aansluiten en root bridge overnemen, netwerk loops veroorzaken | 3 | 5 | 15 | `spanning-tree portfast bpduguard default`, `spanning-tree guard root` op trunk poorten |

---

## DTP (Dynamic Trunking Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 4 | S1 — DTP | Fa0/6 staat op mode auto (DTP negotiation actief), vormt automatisch trunk. Ook fa0/5, fa0/9-24, gig0/1 en gig0/2 staan op auto | Aanvaller kan via DTP een trunk opzetten en alle VLAN-verkeer onderscheppen (VLAN hopping) | 4 | 5 | 20 | `switchport mode access` + `switchport nonegotiate` op alle access poorten |

---

## VLAN

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 5 | S0, S1 — VLAN | Veel ongebruikte poorten zitten in VLAN 1 (default) en staan nog aan | Geen segmentatie, onbevoegde toegang via ongebruikte poorten | 3 | 4 | 12 | Ongebruikte poorten in apart VLAN plaatsen + `shutdown` |

---

## VTP (VLAN Trunking Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 6 | S0, S1 — VTP | VTP domain "LAB" zonder password ("The VTP password is not configured"). S0=Server, S1=Client. VTP Pruning disabled | Aanvaller kan switch aansluiten met hogere revision number en volledige VLAN-database overschrijven/wissen | 3 | 5 | 15 | `vtp password <sterk_wachtwoord>` instellen, of `vtp mode transparent` gebruiken |

---

## BPDU Guard

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 7 | S0, S1 — BPDU Guard | `show running-config \| include bpduguard` toont niets. Geen BPDU Guard geconfigureerd op enige poort. `show running-config \| include guard` onthulde ook plain text account: username Vanguard password 0 Vanguard | Aanvaller kan BPDU-berichten sturen om STP-topologie te manipuleren. Wachtwoord Vanguard in plain text leesbaar | 3 | 5 | 15 | `spanning-tree portfast bpduguard default` globaal. `service password-encryption` activeren |

---

## EtherChannel

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 8 | S0-S1 — EtherChannel | PAgP EtherChannel: S0 Fa0/8 = stand-alone (I), S1 Fa0/7 = desirable (D). Mismatch in bundeling. Load-balancing = src-mac (standaard, niet optimaal) | Verminderde redundantie en bandbreedte, niet alle links actief | 2 | 3 | 6 | EtherChannel opnieuw configureren zodat alle poorten (P) status krijgen. Overweeg `port-channel load-balance src-dst-ip` |

---

## DOT1Q / Trunking

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 9 | S0, S1 — Trunking/DOT1Q | Native VLAN = 1 op alle trunk poorten (Po1, Fa0/1, Fa0/6). VLANs allowed on trunk: 1-1005 (veel meer dan nodig) | VLAN hopping via double-tagging aanval op native VLAN 1 | 3 | 5 | 15 | Native VLAN wijzigen naar ongebruikt VLAN: `switchport trunk native vlan 999`. Trunk beperken: `switchport trunk allowed vlan 10,20` |

---

## Telnet

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 10 | R1 — Telnet | Telnet actief op 192.168.20.2, plain text protocol. Geen `transport input ssh` geconfigureerd op alle apparaten. S0 vty 0-4 en 5-15 met `login` zonder "local". Console poort zonder password | Wachtwoorden en commando's kunnen worden afgeluisterd op het netwerk. Fysieke toegang = directe CLI toegang | 4 | 5 | 20 | Vervang Telnet door SSH: `transport input ssh` op VTY lines. Console password instellen |

---

## SSH

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 11 | R1, R2, S0, S1 — SSH | SSH version 1 geconfigureerd op alle apparaten (`ip ssh version 1`). SSH v1 heeft bekende kwetsbaarheden | Man-in-the-middle aanvallen op SSH-sessies, sessie kan onderschept worden | 3 | 4 | 12 | Upgrade naar `ip ssh version 2` op alle apparaten |

---

## HSRP (Hot Standby Router Protocol)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 12 | R1, R2 — HSRP | HSRP alleen geconfigureerd op R2 voor VLAN 20 (virtual IP 192.168.20.1). R1 heeft geen HSRP. Geen HSRP voor VLAN 10. Geen authenticatie. Preemption disabled. Standby router = unknown | Geen failover: als R2 uitvalt werkt gateway 192.168.20.1 niet meer. Aanvaller kan HSRP spoofing doen zonder authenticatie. Servers (VLAN 10) hebben geen gateway redundantie | 3 | 4 | 12 | HSRP ook op R1 configureren. HSRP voor VLAN 10 toevoegen. `standby 20 authentication md5 key-string <ww>`. `standby 20 preempt` inschakelen |

---

## OSPF

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 13 | R1, R2 — OSPF | OSPF actief in Area 0, geen authenticatie ("Area has no authentication"). Neighbor state = INIT/DROTHER (niet FULL). WAN-links (10.1.1.0, 10.1.2.0) DOWN | Aanvaller kan valse routes injecteren. OSPF adjacency niet volledig = routing werkt niet correct | 3 | 5 | 15 | OSPF authenticatie instellen: `area 0 authentication message-digest`. Per interface: `ip ospf message-digest-key 1 md5 <ww>` |

---

## UDLD (Unidirectional Link Detection)

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 14 | S0, S1 — UDLD | UDLD niet ondersteund in deze Packet Tracer versie (`show udld` = Invalid input) | Unidirectionele links kunnen onopgemerkt blijven en loops of black holes veroorzaken | 2 | 3 | 6 | In productieomgeving: `udld enable` of `udld aggressive` |

---

## Routing

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 15 | R1, R2 — Routing | Geen default route ingesteld ("Gateway of last resort is not set"), alleen connected routes zichtbaar. Geen static routes. WAN-interfaces DOWN | Geen internetverbinding, verkeer tussen subnetten faalt | 5 | 5 | 25 | Default route instellen: `ip route 0.0.0.0 0.0.0.0 <next-hop>`. `default-information originate` in OSPF |

---

## HTTP

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| — | R1, R2, S0, S1 — HTTP | `show running-config \| include ip http` toont niets. HTTP-server niet actief | Geen risico gevonden | — | — | — | — |

---

## DHCP

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 16 | R1, R2 — DHCP | Beide routers zijn DHCP-server voor dezelfde netwerken (conflict). R1 DHCP incompleet: geen `default-router`, geen `excluded-address`. R1 heeft IP's uitgedeeld zonder gateway (verklaart PC gateway 0.0.0.0). Geen DHCP snooping op switches | DHCP spoofing: aanvaller kan valse DHCP-server opzetten. PC's krijgen geen gateway van R1. IP-conflicten mogelijk | 3 | 5 | 15 | R1 DHCP fixen of uitschakelen. `ip dhcp snooping` inschakelen op switches. Trusted ports instellen |

---

## Overige bevindingen

### Wi-Fi / Access Points

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 17 | AP Medewerkers + Gasten — Wi-Fi | Encryption type = disabled op beide access points. Geen WEP/WPA/WPA2, geen wachtwoord | Iedereen kan verbinden met het netwerk en al het draadloze verkeer afluisteren | 5 | 5 | 25 | WPA2-PSK of WPA2-Enterprise instellen met sterk wachtwoord |

### Wachtwoorden / Algemene beveiliging

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 18 | R1, R2, S0, S1 — Wachtwoorden | `enable password cisco` (zwak standaard wachtwoord, plain text). `no service password-encryption` bevestigd. Username Vanguard met password 0 Vanguard (plain text). `enable password` i.p.v. `enable secret` | Wachtwoorden leesbaar in configuratie. Zwak wachtwoord makkelijk te raden | 4 | 4 | 16 | Vervang door `enable secret`. `service password-encryption` activeren. Sterke wachtwoorden gebruiken |

### Default Gateway PC's

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 19 | PC0, PC1 — Default Gateway | Default gateway = 0.0.0.0 op beide PC's. DHCP van R1 geeft geen gateway mee | PC's kunnen niet communiceren buiten hun subnet | 5 | 4 | 20 | Default gateway instellen op 192.168.20.1 (HSRP virtual IP), of DHCP op R1 fixen |

### Algemene beveiliging — Configure Terminal

| Nr | Component/Service | Kwetsbaarheid / Foutconfiguratie | Mogelijke Impact | Waarschijnlijkheid | Impactniveau | Risicoscore | Mitigatie / Advies |
|----|-------------------|----------------------------------|------------------|---------------------|--------------|-------------|---------------------|
| 20 | R1, R2, S0, S1 — Configure Terminal | Vanuit enable mode (password "cisco") kan direct `conf t` worden uitgevoerd. Geen extra authenticatie of autorisatie vereist voor configuratiewijzigingen | Aanvaller met enable toegang kan volledige configuratie wijzigen: VLANs verwijderen, routes aanpassen, wachtwoorden wijzigen, interfaces uitschakelen, backdoor accounts aanmaken | 4 | 5 | 20 | Sterk enable secret instellen. AAA autorisatie configureren met privilege levels. `login local` met sterke wachtwoorden. Logging van configuratiewijzigingen inschakelen |
