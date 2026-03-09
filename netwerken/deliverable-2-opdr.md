# Deliverable 2 — IDS/IPS vs Firewall (pfSense + Snort vs Kali + UFW)
[workshop](https://dlo.mijnhva.nl/d2l/le/lessons/691484/topics/2855833)

## Benodigdheden (per duo)

| | **Laptop 1 (mijn laptop)** | **Laptop 2 (Muazma's laptop)** | **Target** |
|---|---|---|---|
| VM 1 | Kali (aanvaller) | pfSense/OPNsense + Snort | Telefoon/hotspot |
| VM 2 | Client VM (kloon van Kali) | Client VM (mag Kali zijn) | — |

---

## Stap 1 — UFW controleren
> *Mijn laptop*
> gewisseld Muazma doet deze nu

opzet:  
```bash
# Stap 1 – Kali VM opzetten + UFW
# Adapter 1: NAT (WAN) – verbonden met hotspot
# Adapter 2: Host-Only of Internal Network (LAN)

sudo apt update
sudo apt install ufw -y
sudo ufw status verbose
sudo ufw logging on
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
sudo apt install hping3 -y
sudo apt install nmap -y
```

Noteer alvast:
- Welke UFW default policies staan aan?
- Waar zie je UFW logs terug (en hoe)?

---

## Stap 2 — Snort controleren
> *Muazma's laptop*
> ik doe deze nu

opzet:  
```bash
# Stap 2 – Snort configureren in pfSense
# (via GUI: geen CLI-commando's)

1. Start pfSense VM → Adapter 1: NAT, Adapter 2: Host-Only
2. Stel interfaces en IP's in via pfSense setup wizard
3. System → Package Manager → installeer Snort
4. Services → Snort → Interface: LAN
5. Kies modus: IDS (alleen log) of IPS (log + block) -> noteer wat gebeurt
```
> via netgate pfsense iso gedownload en geinstaleerd in vmware
> 

Noteer alvast:
- Op welke interface draait Snort?
- IDS of IPS modus?
- Welke categorieën/rulesets staan aan?

---

## Stap 3 — Target kiezen & testroute bepalen

Je hebt een doel-IP nodig om op te testen.

**Eigen telefoon/hotspot als target:**
1. Zet hotspot aan op je telefoon
2. Verbind je laptop/VM's met die hotspot (volgens topologie)
3. Test richting het IP van je telefoon/hotspot

> **Hint:** Mogelijk moet je routing handmatig instellen op Kali/pfSense.

---

## Stap 4 — Tests uitvoeren

Per test vergelijk je:
- **UFW:** block of allow? Log ja of nee?
- **Snort:** alert of log? Wordt er geblokkeerd?

**[Open de Forms](https://forms.office.com/e/TE8dYk2LME)** — vul meteen in, daar staat ook meer instructie.

---

### Test 1 — Normale ping (ICMP)

```bash
ping -c 4 <target-ip>
```

Controleer:
- UFW logs / status
- Snort alerts / logs

> ICMP wordt niet altijd zoals verwacht gelogd via UFW — noteer wat je wél ziet. Geen Snort-alerts? Controleer of traffic over de juiste Snort-interface gaat.

---

### Test 2 — hping3 (SYN / scan-achtig verkeer)

```bash
sudo hping3 -S -p 80 -c 20 <target-ip>
```

Controleer:
- UFW logs
- Snort alerts
- Snort in IPS-modus: wordt er geblokkeerd? Hoe merk je dat?

---

### Tests 3, 4, 5 — Kies minimaal 3 extra aanvalstypen

#### A - Nmap port scan
```bash
sudo nmap -sS -T3 <target-ip>
sudo nmap -sS -T4 -p- <target-ip>
```

#### B - UDP scan
```bash
sudo nmap -sU --top-ports 50 <target-ip>
```

#### C - ICMP flood
```bash
sudo hping3 --icmp -c 50 <target-ip>
sudo hping3 --icmp --flood <target-ip>
```

#### D - HTTP hammer test *(alleen als target een webserver heeft)*
```bash
for i in {1..30}; do curl -s http://<target-ip>/ >/dev/null; done
```

> Als een test extra configuratie vraagt, beschrijf dit dan in je Forms-antwoorden.

---

## Afronding

- Zet Snort in **IPS/Block modus** en herhaal minimaal 1 test (bijv. nmap of hping SYN) om het verschil **IDS vs. IPS** te laten zien
- Vul de **[Forms](https://forms.office.com/e/TE8dYk2LME)** volledig in — per duo, kort maar concreet
