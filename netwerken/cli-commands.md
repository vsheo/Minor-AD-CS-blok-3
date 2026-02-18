# Command Line Inferface - commands

- eerst zit je in de `user mode`
  - met `?` command zie je een lijst van alle commands die je kan uitvoeren
- `enable` of `en`: privilaged mode aan zetten
  - nu geeft `?` command zie je veel meer opties
- bij een verkeerde command kan je vast zitten, om eruit te gaan: `ctrl shift 6`

modes die er zijn en hoe je naar de volgende kan gaan:
- user mode -> `Switch>` + `enable`
  - privileged mode -> `Switch#` + `configure terminal` of `conf t`
    - configure mode -> `Switch(config)#` + `interface ... ..`
      - configure mode -> `Switch(config-if)#`

---

## fastEthernet (fa0/1)
hiervoor heb je privilage mode maar ook configure terminal nodig  
- `enable`
- `configure terminal` of `conf t`

om fa0/1 uit te zetten moet je naar de interface configuratie mode gaan
- `interface fastEthernet 0/1`
- `shutdown`, om fa0/1 uit te zetten
- `no shutdown`, om fa0/1 weer aan te zetten
> ook hier kan je de `?` command gebruiken om te zien welke command je kan gebruiken

---

## Als je een fout hebt gemaakt
dit geld voor alle commands:  
- schrijf je command die je weg wilt halen (pijltje naar boven)
- schrijf `no` ervoor  

bijvoorbeeld: `no` `ip route 192.168.5.0 255.255.255.0 192.168.2.2`

---

## Ip-addressering
Een IP address aangeven op een poort doe je binnen de interface-configuratie:
- `interface fa0/0`
- `no shutdown`, zodat de poort aan gaat
- `ip address`, ook op dit moment kan je `?` doen om te kijken hoe je het verder invult
  - `ip address` + `Ip address` + `subnet mask`

bijvoorbeeld:
- `interface fa0/0`
- `ip address 192.168.1.1 255.255.255.0`
> nu is de ip 192.168.1.1 verbonden aan de poort fastEthernet0/0

---

## Ip route
wordt gedaan in de config mode (`(config)#`)  
met de gui was dit:
- naar static
- eerst ip van waar je naartoe wilt gaan
- de subnet mask
- hoe je daar naar toe gaat, de next hop (waar de de request naartoe stuurt)

in de cli:
- `ip route`
  - `ip route` `Ip adress` `subnet mask` `next hop`
  - bijvoorbeeld `ip route` `192.168.5.0` `255.255.255.0` `192.168.2.2`



nu dat je static routes hebt gemaakt kan je met `ping` testen als ze goed verbonden zijn.  
Bijvoorbeeld:  
op een `PC` -> `Desktop` -> `Command prompt`, daarin de ping command:  
`ping` + `Ip address`: `ping 192.168.3.2`


### show
met `show running-config` kan je zien wat er op de router is ingesteld  
> enter is per regel, spatie is per pagina

met `show ip route` kan je zien welke ip adreress aan welke poort verbonden is (de routing table)


---