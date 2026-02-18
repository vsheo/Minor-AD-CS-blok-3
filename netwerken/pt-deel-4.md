# Packet Tracer Routing & Geavanceerde Router Configuratie - Samenvatting

---

## 1. Routing Overzicht
Routing is complex en heeft impact op grote delen van de infrastructuur. Dit deel gaat over:

- Configureren van routing-protocollen
- Verbinden van verschillende netwerken
- Beveiliging en internetconnectiviteit komen later

### Routingproces
1. PC0 (192.168.1.2) wil een bericht sturen naar PC1 (192.168.3.2). Omdat het buiten zijn netwerk valt, stuurt hij het naar zijn gateway (192.168.1.1).
2. R1 ontvangt het pakket en kijkt in de routing-table. Stuurt het door naar next-hop (192.168.2.2, R2).
3. R2 ontvangt het pakket en stuurt het direct naar PC1 via zijn FastEthernet-poort.
4. PC1 ontvangt het pakket.

**Tracert** laat zien hoeveel hops een bericht aflegt. Alternatieve paden kunnen worden ingesteld door routing-tables anders te vullen.

---

## 2. Manieren van Routing Table vullen
### 2.1 Static Routing
- Handmatig routes instellen: `ip route <network-id> <subnet-mask> <next-hop-ip>`
- Geschikt voor kleine netwerken, tijdrovend bij veel routers

### 2.2 Dynamische Routing protocollen
**Categorieën:**

| Type | Voorbeelden | Werking |
|------|------------|---------|
| Distance Vector | RIP, RIP v2 | Beste pad op basis van aantal hops |
| Link-State | OSPF | Berekening op basis van kosten (cost), selecteert pad met laagste cost |
| Hybrid | EIGRP | Combinatie van beide; snel detecteren netwerkveranderingen, minder CPU-intensief |

---

## 3. IP-adressering & Subnetting
### Classfull vs Classless
- Classfull: inefficiënt, grote broadcastomgevingen
- Classless (CIDR/VLSM): flexibel, efficiënter gebruik van IP-adressen

**Voorbeeld subnetting:**
- Nodig: 4 bruikbare IP's per subnet, 6 subnets
- Formule: `Aantal hosts + 2 = 2^N` → 4 + 2 = 6 → 2^3 = 8
- Subnetmask: 255.255.255.248 (/29)
- Magic number: 256 - 248 = 8 → netwerk-ID's: 0, 8, 16, 24, 32, 40, 48

**Subnettabel:**

| Netwerk | Netwerk-ID | Start IP | Eind IP | Broadcast |
|---------|------------|----------|---------|-----------|
| 1       | 192.168.1.0 | 192.168.1.1 | 192.168.1.6 | 192.168.1.7 |
| 2       | 192.168.1.8 | 192.168.1.9 | 192.168.1.14 | 192.168.1.15 |
| 3       | 192.168.1.16 | 192.168.1.17 | 192.168.1.22 | 192.168.1.23 |
| 4       | 192.168.1.24 | 192.168.1.25 | 192.168.1.30 | 192.168.1.31 |
| 5       | 192.168.1.32 | 192.168.1.33 | 192.168.1.38 | 192.168.1.39 |
| 6       | 192.168.1.40 | 192.168.1.41 | 192.168.1.46 | 192.168.1.47 |
| 7       | 192.168.1.48 | 192.168.1.49 | 192.168.1.54 | 192.168.1.55 |

---

## 4. Routing Protocollen

### 4.1 RIP / RIP v2
- RIP v1: classful, broadcast updates
- RIP v2: ondersteunt subnetten, multicast updates
- RIPNG: IPv6
- Configuratie voorbeeld R0:
Router Rip
Network 192.168.1.0
Network 192.168.2.0
Version 2

- Show: `show ip route`
- Administrative Distance (AD): belangrijk bij meerdere protocollen

| Protocol | AD |
|----------|----|
| Direct verbonden | 0 |
| Static Route | 1 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| RIP | 120 |

**Belangrijke RIP-commando’s:**

- `passive-interface s0/1/0` → interface ontvangt RIP, zendt zelf niets uit
- `distance 1` → AD aanpassen voor voorkeur
- `default-information originate` → default route in updates opnemen

---

### 4.2 OSPF
- Werkt met **areas**, DR/BDR kiezen op basis van router-ID
- Backbone: Area 0
- Configuratie voorbeeld:
Router OSPF 1
Network 192.168.1.0 0.0.0.3 Area 0

- Stub-area's: beperken inter-area updates, default route vanuit ABR
- Belangrijk: `clear ip ospf process` bij wijzigingen in router-ID of area

---

### 4.3 EIGRP
- Hybride protocol, Cisco-specifiek
- Werkt met Autonomous Systems (AS)
- Snelle failover, variance voor load-balancing
- Configuratie voorbeeld:
Router EIGRP 1
Network 192.168.1.0 0.0.0.3

- Belangrijke commando’s:
  - `show ip eigrp neighbors`
  - `show ip eigrp interfaces`
  - `passive-interface`
  - `variance <waarde>` → load-balancing

- Redistribute commando: routes tussen AS’en uitwisselen

---

## 5. IPv6 Routing

### 5.1 Verschillen IPv4 vs IPv6

| Kenmerk | IPv4 | IPv6 |
|---------|------|------|
| Bits | 32 | 128 |
| Adressering | Statisch / DHCP | Statisch / DHCPv6 / SLAAC |
| IP→MAC | ARP broadcasts | Neighbor Solicitation multicast |
| Notatie | Decimaal | Hexadecimaal |
| Voorbeeld | 8.8.8.8 | 2001:4860:4860::8888 |

### 5.2 IPv6 Configuratie
- PC: auto-config of handmatig
- Router: `ipv6 address <adres>/<prefix>`
- IPv6 routing: `ipv6 unicast-routing`

**Static IPv6 route:**
Router0(config)# ipv6 route 2003::/64 2002::2

---

### 5.3 IPv6 Dynamische protocollen

#### RIPNG (IPv6)
- Configuratie per interface, niet op routerniveau
Router0(config)# interface fa0/0
Router0(config)# ipv6 rip <NAAM> enable

#### OSPFv3 (IPv6)
Router0(config)# ipv6 router ospf 1
Router0(config-rtr)# router-id 1.1.1.1
Router0(config-if)# ipv6 ospf 1 area 0

- Zelfde principes als IPv4 OSPF: DR/BDR, areas, backbone area 0

#### EIGRP for IPv6
- Vergelijkbaar met OSPF configuratie
- Activeer `ipv6 unicast-routing` en configureer per interface met `ipv6 eigrp <AS>`

---

## 6. Praktische Tips
- Controleer altijd routing tables: `show ip route` / `show ipv6 route`
- Test connectiviteit: `ping`, `tracert`
- Pas default routes en stub areas toe om routing efficiënt te maken
- Gebruik AD om voorkeuren van protocollen te bepalen
- IPv6: gebruik SLAAC of DHCPv6 voor automatische adressering

---

**Conclusie:**  
Routing vereist goed begrip van protocollen, subnetting, en netwerktopologie. Dynamische protocollen zoals RIP, OSPF en EIGRP automatiseren het proces en verbeteren schaalbaarheid en betrouwbaarheid. IPv6 introduceert nieuwe adressering en protocollen, maar de concepten blijven vergelijkbaar met IPv4.
