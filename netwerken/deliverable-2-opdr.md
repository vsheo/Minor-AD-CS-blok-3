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
beide vms op dezelfde "netwerk"  
<img width="758" height="599" alt="image" src="https://github.com/user-attachments/assets/df3d0b93-14d3-4bab-9cd5-002626b1cf54" />
> restart netwerk om ip te vinden
> sudo ip link set eth0 down
> sudo ip link set eth0 up
> sudo dhcpcd eth0

- via netgate pfsense iso gedownload en geinstaleerd in vmware  
- vms op hetzelfde netwerk gezet
- op de host only naar `https://192.168.1.1`
- de wizard gevolgd alles next gedaan, default was goed
- daarna boven bij system -> package manager, snort gedownload


daarna
- boven bijn services -> snort
- lan toevoegen (save)
- bij block settings -> block offenders aan zetten -> save
- terug naar services -> snort en de play button klikken (dit is voor ips)
- voor ids moet block settings uit zijn


Noteer alvast:
- Op welke interface draait Snort?
  - <img width="1942" height="201" alt="image" src="https://github.com/user-attachments/assets/776d4a54-bd83-40fd-95a3-7ddfb97a88d3" />
  - op LAn (em1)
- IDS of IPS modus?
  - IDS
- Welke categorieën/rulesets staan aan?
  - <img width="1926" height="685" alt="image" src="https://github.com/user-attachments/assets/5ba89e80-0fb3-414b-8d17-fc2d7d7383ed" />
  - Snort GPLv2 Community Rules (Talos certified)

---

## Stap 3 — Target kiezen & testroute bepalen

Je hebt een doel-IP nodig om op te testen.

**Eigen telefoon/hotspot als target:**
1. Zet hotspot aan op je telefoon
2. Verbind je laptop/VM's met die hotspot (volgens topologie)
3. Test richting het IP van je telefoon/hotspot

> **Hint:** Mogelijk moet je routing handmatig instellen op Kali/pfSense.

de Ip richting getest met `nmap -sS -Pn 192.168.1.1`,  
op Muazma's kali aanvaller VM kon ze wel de target vinden:  
<img width="664" height="292" alt="image" src="https://github.com/user-attachments/assets/3ea9a052-d695-4650-a9c4-a33791d84cb0" />  

Maar op de pfsense webpagina kregen we geen alerts:  
<img width="1778" height="862" alt="Schermafbeelding 2026-03-11 173442" src="https://github.com/user-attachments/assets/9f6dcf8e-aae0-4430-a1fd-d7ede8fa6c40" />


---

## Stap 4 — Tests uitvoeren

Per test vergelijk je:
- **UFW:** block of allow? Log ja of nee?
  - op Muazma's laptop
  - Outgoing ping: allow
  - Logging is on(low)
  - <img width="537" height="126" alt="image" src="https://github.com/user-attachments/assets/6b7a1b46-b7e7-4358-9c6a-518edf9ec1ad" />

- **Snort:** alert of log? Wordt er geblokkeerd?
  - geen alerts
    - <img width="1778" height="862" alt="Schermafbeelding 2026-03-11 173442" src="https://github.com/user-attachments/assets/94914751-f057-4092-8ee8-0333dc321a06" />
  - snort settings
    - <img width="1807" height="457" alt="Schermafbeelding 2026-03-11 173605" src="https://github.com/user-attachments/assets/c0b5d4ab-ed8d-42d1-a30a-b428857bf4e8" />
    - <img width="1770" height="843" alt="Schermafbeelding 2026-03-11 183125" src="https://github.com/user-attachments/assets/e84873ce-7069-4553-a55f-f1a704cf8d76" />
    - <img width="1900" height="527" alt="Schermafbeelding 2026-03-11 183919" src="https://github.com/user-attachments/assets/b79bad52-e894-4108-a0f2-2d87c7dfa77b" />


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
