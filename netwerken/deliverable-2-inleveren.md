# Deliverable 2 — IDS/IPS vs Firewall

### pfSense / OPNsense + Snort vs Kali + UFW

---

> Wanneer je dit formulier indient, ziet de eigenaar je naam en e-mailadres.

---

## Vraag 1 — Klas

In welke klas zitten jullie?  
101

---

## Vraag 2 — Duoleden

**Wat zijn de volledige namen van de duoleden?**

```
Naam 1: Viresh
Naam 2: Muazma
```

---

## Vraag 3 — Opstelling

**Beschrijf jullie testopstelling:**

- Welke VM's gebruik je (Kali / pfSense / OPNsense)?
  - Viresh: pfSense VM en kali host only VM
  - Muazma: Kali VM Aanvaller en Kali VM Client
- Netwerkmodus per VM (NAT, Host-Only, Internal Network)?
  - Viresh:
    - pfsense -> NAT en host only
    - kali -> host only
  - Muazma:
    - kali aanvaller -> NAT en host only
    - kali client -> host only
- Wat zijn de IP-adressen — DHCP of statisch?
  - Viresh
    - pfSense: `192.168.1.1`, Statisch in kali host only op de web pagina aangegeve
    - Kali host only: `192.168.216.130` DHCP omdat hier dynamisch staat op de regel van de IP:
      - <img width="1489" height="488" alt="Schermafbeelding 2026-03-11 180835" src="https://github.com/user-attachments/assets/81b1781c-c16a-42a4-aee9-6fa7360818d8" />
  - Muazma
    - Kali aanvaller: `172.20.10.8`
    - client VM: 
- Is er end-to-end connectiviteit?
  - Kali aanvaller van Muazma kan pfSense met nmap vinden: `nmap -sS -Pn 192.168.1.1`
  - Maar in de webpagina van Viresh kali host only zien we niks bij alerts
- Waar staat het target (telefoon/hotspot, VM achter pfSense, etc.)?
  - pfSense zelf `192.168.1.1` is het target -> voorheen
  - We hebben nu door dat de target de Ip van mijn telefoon moet zijn dat is: ``


---

## Vraag 4 — UFW Baseline-config

**Welke UFW-instellingen hebben jullie gezet?**

- `default incoming` / `outgoing` policy
  - Default policies:
  - Incoming: deny incomming
  - Outgoing: allow outgoing
  - Routed: disabled
- `logging` aan of uit
  - logging: on (low)
- Voeg 1 regel output toe uit `sudo ufw status verbose` (beschrijf in tekst)
  - <img width="537" height="126" alt="image" src="https://github.com/user-attachments/assets/6f05274a-1923-4a7b-b519-bb0a124f7448" />
  - Dit is de output van `sudo ufw status verbose` op Muazma's Kali aanvaller VM. Je ziet dat UFW actief is, logging staat aan op 'low', inkomend verkeer wordt standaard geblokkeerd (deny) en uitgaand verkeer is toegestaan (allow).

---

## Vraag 5 — Snort Baseline-config

**Op welke interface draait Snort en in welke modus?**

- IDS of IPS/Block?
  - wij hebben voor IDS gekozen
- Welke (globale) rules/categorieën staan aan?
  - <img width="1910" height="714" alt="image" src="https://github.com/user-attachments/assets/b244949f-e9fa-481e-8031-b41ce6dee2fc" />
  - 

---

## Vraag 6 — Routing Check ⚠️

**Hoe hebben jullie gecontroleerd dat het verkeer langs Snort loopt?**
~nmap -sS -Pn 172.20.10.10 en 10.1

Bijv. Snort alerts verschijnen / interface counters / pfSense logs.

```
Antwoord: ___________________________
```

---

## Vraag 7 — Test 1: Ping (ICMP)

> Voer de test uit op **beide clients/laptops**!

Beantwoord:

- Resultaat: success of fail?
- viresh kali host only ping naar pfsense
  - <img width="1008" height="550" alt="image" src="https://github.com/user-attachments/assets/1920a6f0-a7b6-4b09-8a60-b205201ad593" />
- Muazma client VM
  - zei moets haar ping versturen naar `192.168.56.100` omdat op haar client vm dat de hotspot ip is
    - <img width="582" height="213" alt="image" src="https://github.com/user-attachments/assets/8bdffff9-235c-4a6d-a344-11f55f322828" />
- Wat logt **UFW**?
  -  omdat log op low staat, wordt uitgaand verkeer niet gelogd wordt. Alleen geblokkeerd inkomend verkeer wordt gelogd door UFW.
- Wat logt **Snort**?
  - <img width="1905" height="730" alt="image" src="https://github.com/user-attachments/assets/9ac11eb8-6e78-4a42-aa20-d4f93bdaca30" />
  - Logt niets voor ping. Ping wordt geblokkeerd door de pfSense firewall voordat Snort het analyseert. De Community Rules bevatten geen ICMP regels die deze ping detecteren.
  - Logt wel TCP alerts

---

## Vraag 8 — Test 2: hping3 SYN

> Voer de test uit op **beide clients/laptops**!

**Commando:**

```bash
sudo hping3 -S -p 80 -c 20 <target-ip>
```

Beantwoord:

- Wat gebeurt er?
  - ik heb op mijn client VM(kali host only) hpin3 geinstalleerd
    - ik heb pfsense VM gepinged via LAN en WAN 0 received
    - <img width="1159" height="490" alt="image" src="https://github.com/user-attachments/assets/bff353d7-8a4c-44e6-90d9-5dd9e55c9f9e" />
    - in alerts zie ik geen nieuwe alerts komen
    - daarna hping gedaan op `192.168.1.100`, toen zag ik wel alerts komen
  - Muazma gepinged op `192.168.56.100`
    - <img width="624" height="351" alt="image" src="https://github.com/user-attachments/assets/76faa7a8-fe61-45ac-9b11-1eb7f3301628" />
    - eerste keer wel alerts ontvangen, daarna clear en op nieuw gedaan maar kreeg niet opnieuw een alerts ( mischien waren die alerts van ergens anders)

- Welke logs/alerts zie je in **UFW** en **Snort**?

---

## Vraag 9 — Extra Test A _(jullie keuze)_

**Voer 1 van de extra aanvalstypen uit** (bijv. nmap scan).

Beantwoord:

- Welke test precies (commando)?
  - 
- Observatie **UFW**
- Observatie **Snort**

```
Commando: ___________________________
UFW:      ___________________________
Snort:    ___________________________
```

---

---

## Vraag 12 — Snort IDS → IPS Verschil

**Zet Snort (indien mogelijk) in IPS/Block-modus en herhaal 1 test** (bijv. nmap of hping).

Beantwoord:

- Wat veranderde er?
- Hoe merk je dat het echt blokkeert — symptoom + log?

```
Antwoord: ___________________________
```

---

## Vraag 13 — Conclusie & Advies

**Als jij een klein bedrijf moest adviseren:**

- Wanneer kies je alleen voor een firewall?
- Wanneer voeg je IDS/IPS toe?

```
Antwoord: ___________________________
```

---











---
## extra opdrachten


## Vraag 10 — Extra Test B _(jullie keuze)_

**Voer 1 van de extra aanvalstypen uit.**

Beantwoord:

- Welke test precies (commando)?
- Observatie **UFW**
- Observatie **Snort**

```
Commando: ___________________________
UFW:      ___________________________
Snort:    ___________________________
```

---

## Vraag 11 — Extra Test C _(jullie keuze)_

**Voer 1 van de extra aanvalstypen uit.**

Beantwoord:

- Welke test precies (commando)?
- Observatie **UFW**
- Observatie **Snort**

```
Commando: ___________________________
UFW:      ___________________________
Snort:    ___________________________
```

