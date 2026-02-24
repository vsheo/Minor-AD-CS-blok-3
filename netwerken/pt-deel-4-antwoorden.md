# packet tracer deel 4 opdrachten

## Oprdacht 18a
|start| IP hop1 | IP hop2 | IP hop3 | IP hop4 | IP hop5 | IP hop6 | Eind |
|-----| ------- | ------- | ------- | ------- | ------- | --------|------|
| pc0 192.168.1.1|R1(5.0.0.1)|R3(1.0.0.3)|||PC4|
| pc0 192.168.1.1|R1(5.0.0.1)|R3(5.0.0.5)|R4(4.0.0.4)|||PC5|
| pc0 192.168.1.1|R1(5.0.0.1)|R2(2.0.0.2)|R4(3.0.0.4)|||PC5|
| pc0 192.168.1.1|R1(5.0.0.1)|R3(1.0.0.3)|R4(4.0.0.4)|||PC5|
| pc2 192.168.5.1|R4(7.0.0.4)|||||PC6|
| pc3 192.168.4.1|R3|||||PC4|
| pc4 192.168.3.1|R3|R5|R1(5.0.0.1)|R1||PC0|
| pc5 192.168.6.1|R4|R5(5.0.0.1)|R1|||PC0|
| pc5 192.168.6.1|R4|R2(2.0.0.1)|R1|||PC0|

- `sh ip route`
  - kijken naar elke ip berichten verstuurt worden
  - `192.168.3.0` verstuurt naar `1.0.0.3`
- `sh cdp neighbors detail`
  - kijken welke van de aangesloten routers de ip `1.0.0.3` heeft
  - interface -> de poort van deze router
  - outgoing port -> de poort op de router naar waar bericht verstuurt wordt
- deze lijn volgen totdat je de `PC` bereikt

|router| Maakt deze router gebruik van Static Routing? | Maakt deze router gebruik van RIP? | Maakt deze router gebruik van Default Routing? | Indien Default Routing, wat is het IP van next-hop? |
|-----| ------- | ------- | ------- | ------- |
| R1 | ja | ja | ja | 2.0.0.2 |
| R2 | ja | ja | ja | 6.0.0.5 |
| R3 | ja | ja | ja | 1.0.0.1 |
| R4 | ja | ja | ja | 4.0.0.3 |
| R5 | nee | ja | nee | 8.0.0.3 |

---

## Oprdacht 19a
Vraag 19.1. Hoeveel IP’s zijn er nodig voor het grootste netwerk?  
**8**  

Vraag 19.2. Wat is je subnet mask voor het netwerk, uitgaande van het grootste netwerk? Laat de berekening zien.  


> Aantal computers + 2 = 2^N  
8+2= 10 adressen nodig -> 2^4=16  
dat is dus 4host bits  
netwerk bits: 32-4= 28 netwerk bits -> /28  
subnet mask: `11111111.11111111.11111111.11110000`  
(4host bits dus 4 0len overlaten)  
`11110000` -> 16+32+64+128=240  
subnet mask = `255.255.255.240`


Vraag 19.3. Wat is je subnet mask in CIDR-notatie?  
`11111111.11111111.11111111.11110000`  
8+8+8+4= 28 -> /28

Vraag 19.4. Vul de volgende tabel in:  
4host bits, dus 16 per netwerk  
| netwerk | netwerk id | start IP | eind ip | broadcast |
|---| ------------ | ------------ | ------------ | ------------ |
| 1 | 192.168.1.0  | 192.168.1.1  | 192.168.1.14 | 192.168.1.15 |
| 2 | 192.168.1.16 | 192.168.1.17 | 192.168.1.30 | 192.168.1.31 |
| 3 | 192.168.1.32 | 192.168.1.33 | 192.168.1.46 | 192.168.1.47 |
| 4 | 192.168.1.48 | 192.168.1.49 | 192.168.1.62 | 192.168.1.63 |

Vraag 19.5. We willen graag drie subnets. De grootste bevat 49 computers. Vul het volgende in:  
subnet: **255.255.255.192**
| netwerk | netwerk id | start IP | eind ip | broadcast |
|---| ------------ | ------------ | ------------- | ------------- |
| 1 | 192.168.1.0  | 192.168.1.1  | 192.168.1.62  | 192.168.1.63  |
| 2 | 192.168.1.64 | 192.168.1.65 | 192.168.1.94  | 192.168.1.95  |
| 3 | 192.168.1.96 | 192.168.1.97 | 192.168.1.126 | 192.168.1.127 |

Vraag 19.6. Ons subnet is 255.255.255.252 Hoeveel computers kan ik dan in één subnet voorzien van een IP-adres? Laat zien, hoe je dit hebt berekend.  

> subnetmask = `255.255.255.252`  
256-252=4 -> dus 4 ip adressen per netwerk  
Aantal computers + 2 = 2^N  
2^N= 4  
Aantal computers + 2 = 4  
Aantal computers = 2


Vraag 19.7. We willen graag vier subnets. De grootste bevat vier computers. Vul het volgende in:  

4+2=6 -> 2^3=8 ip adressen per netwerk  
3 host bits 
CIDR: 32 - 3host bits = /29  
`11111111.11111111.11111111.11111000`  
`11111000` -> 8+16+32+64+128=248  

subnet: **255.255.255.248**  
CIDR: **/29**
| netwerk | netwerk id | start IP | eind ip | broadcast |
|---| ------------ | ------------ | ------------ | ------------ |
| 1 | 192.168.1.0  | 192.168.1.1  | 192.168.1.6  | 192.168.1.7  |
| 2 | 192.168.1.8  | 192.168.1.9  | 192.168.1.14 | 192.168.1.15 |
| 3 | 192.168.1.16 | 192.168.1.17 | 192.168.1.22 | 192.168.1.23 |
| 4 | 192.168.1.24 | 192.168.1.25 | 192.168.1.30 | 192.168.1.31 |

---
