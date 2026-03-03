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
- Netwerkmodus per VM (NAT, Host-Only, Internal Network)?
- Wat zijn de IP-adressen — DHCP of statisch?
- Is er end-to-end connectiviteit?
- Waar staat het target (telefoon/hotspot, VM achter pfSense, etc.)?
```
Antwoord: ___________________________
```

---

## Vraag 4 — UFW Baseline-config

**Welke UFW-instellingen hebben jullie gezet?**

- `default incoming` / `outgoing` policy
- `logging` aan of uit
- Voeg 1 regel output toe uit `sudo ufw status verbose` (beschrijf in tekst)
```
Antwoord: ___________________________
```

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

## Vraag 9 — Extra Test A *(jullie keuze)*

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

## Vraag 10 — Extra Test B *(jullie keuze)*

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

## Vraag 11 — Extra Test C *(jullie keuze)*

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