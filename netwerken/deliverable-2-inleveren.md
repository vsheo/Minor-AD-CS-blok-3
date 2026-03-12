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
    - Kali aanvaller: `172.20.10.8` MISCHIEN AANGEPAST OMDAT HET NAT IS
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
- Welke (globale) rules/categorieën staan aan?

```
Antwoord: ___________________________
```

---

## Vraag 6 — Routing Check ⚠️

**Hoe hebben jullie gecontroleerd dat het verkeer langs Snort loopt?**

Bijv. Snort alerts verschijnen / interface counters / pfSense logs.

```
Antwoord: ___________________________
```

---

## Vraag 7 — Test 1: Ping (ICMP)

> Voer de test uit op **beide clients/laptops**!

**Commando:**

```bash
ping -c 4 <target-ip>
```

Beantwoord:

- Resultaat: success of fail?
- Wat logt **UFW**?
- Wat logt **Snort**?

```
Antwoord: ___________________________
```

---

## Vraag 8 — Test 2: hping3 SYN

> Voer de test uit op **beide clients/laptops**!

**Commando:**

```bash
sudo hping3 -S -p 80 -c 20 <target-ip>
```

Beantwoord:

- Wat gebeurt er?
- Welke logs/alerts zie je in **UFW** en **Snort**?

```
Antwoord: ___________________________
```

---

## Vraag 9 — Extra Test A _(jullie keuze)_

**Voer 1 van de extra aanvalstypen uit** (bijv. nmap scan).

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

## Vraag 14 — Feedback

**Vond je deze deliverable leuk om te doen?**

- [ ] Ja
- [ ] Nee
- [ ] Min of meer

---

## Vraag 15 — Opmerkingen

**Willen jullie nog iets kwijt?**

```
Antwoord: ___________________________
```
