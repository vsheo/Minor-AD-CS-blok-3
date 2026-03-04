## 4. Top 5 Kritieke Risico's

1. **Risico:** Wi-Fi zonder encryptie — Encryption disabled op beide access points (Medewerkers + Gasten), geen WPA/WPA2, geen wachtwoord
   - **Impact:** Iedereen binnen bereik kan verbinden met het bedrijfsnetwerk en al het draadloze verkeer afluisteren, inclusief gevoelige bedrijfsdata en inloggegevens (score: 5×5 = 25)
   - **Oplossing:** WPA2-PSK of WPA2-Enterprise configureren op beide access points met een sterk wachtwoord. Aparte SSID's en VLANs voor medewerkers en gasten

---

2. **Risico:** Geen default route / routing faalt — Gateway of last resort is not set op beide routers. Alleen connected routes zichtbaar, geen OSPF-routes (OSPF neighbor state = INIT/DROTHER). WAN-interfaces naar KPN liggen DOWN
   - **Impact:** Geen internetverbinding mogelijk. Verkeer tussen subnetten faalt. Het volledige netwerk is geïsoleerd van de buitenwereld (score: 5×5 = 25)
   - **Oplossing:** Default route instellen: `ip route 0.0.0.0 0.0.0.0 <KPN next-hop>`. OSPF adjacency troubleshooten zodat state FULL wordt. `default-information originate` in OSPF configureren

---

3. **Risico:** DTP actief op access poorten — S1 Fa0/6 staat op mode auto, en ook fa0/5, fa0/9-24, gig0/1, gig0/2 staan op dynamic auto. DTP negotiation vormt automatisch trunk verbindingen
   - **Impact:** Een aanvaller kan een apparaat aansluiten dat DTP desirable stuurt, automatisch een trunk opzetten en al het VLAN-verkeer onderscheppen inclusief het server-VLAN (VLAN hopping) (score: 4×5 = 20)
   - **Oplossing:** `switchport mode access` en `switchport nonegotiate` instellen op alle access poorten. Alleen bewust geconfigureerde trunk poorten toestaan

---

4. **Risico:** Telnet in gebruik (plain text) — Telnet actief op R1 (192.168.20.2), geen `transport input ssh` geconfigureerd op alle apparaten. SSH version 1 in gebruik. Console poort zonder password. S0 vty lines met `login` zonder "local"
   - **Impact:** Alle inloggegevens en commando's worden onversleuteld over het netwerk verstuurd en kunnen worden afgeluisterd. Fysieke toegang geeft directe CLI toegang zonder authenticatie (score: 4×5 = 20)
   - **Oplossing:** `transport input ssh` op alle VTY lines. Upgrade naar `ip ssh version 2`. Console password instellen. `login local` op alle VTY lines

---

5. **Risico:** PC's zonder default gateway — Default gateway = 0.0.0.0 op PC0 en PC1. Veroorzaakt door incomplete DHCP-configuratie op R1 (geen `default-router` ingesteld). R1 deelt wel IP-adressen uit maar zonder gateway
   - **Impact:** PC's kunnen niet communiceren buiten hun eigen subnet. Pings naar servers (192.168.10.x) falen. Gebruikers hebben geen toegang tot bedrijfsapplicaties en internet (score: 5×4 = 20)
   - **Oplossing:** R1 DHCP fixen: `default-router 192.168.20.1` toevoegen aan pool VLAN20. Of R1 DHCP uitschakelen en alleen R2 als DHCP-server gebruiken. PC's default gateway instellen op 192.168.20.1 (HSRP virtual IP)

---------

## 5. Hardening Checklist

| Nr | Maatregel | Status (✓/✗) | Opmerkingen |
|----|-----------|--------------|-------------|
| 1 | CDP uitschakelen (`no cdp run`) | ✗ | Risico 1: staat aan op R1, R2, S0, S1 |
| 2 | LLDP uitschakelen (`no lldp run`) | ✗ | Risico 2: staat actief op R1, R2, S0, S1 |
| 3 | BPDU Guard en Root Guard inschakelen | ✗ | Risico 3: alles disabled op S0 en S1 |
| 4 | DTP uitschakelen (`switchport nonegotiate`) | ✗ | Risico 4: S1 Fa0/6 en veel andere poorten op mode auto |
| 5 | Ongebruikte poorten in apart VLAN + `shutdown` | ✗ | Risico 5: veel poorten actief in VLAN 1 |
| 6 | VTP password instellen | ✗ | Risico 6: "The VTP password is not configured" |
| 7 | `service password-encryption` activeren | ✗ | Risico 7: username Vanguard password 0 Vanguard in plain text |
| 8 | EtherChannel mismatch fixen | ✗ | Risico 8: S0 Fa0/8 stand-alone, S1 Fa0/7 down |
| 9 | Native VLAN wijzigen + trunk VLANs beperken | ✗ | Risico 9: native VLAN = 1, allowed 1-1005 |
| 10 | Telnet uitschakelen (`transport input ssh`) | ✗ | Risico 10: Telnet actief, console zonder password |
| 11 | SSH upgraden naar version 2 | ✗ | Risico 11: SSH version 1 op alle apparaten |
| 12 | HSRP op R1 configureren + authenticatie + VLAN 10 | ✗ | Risico 12: alleen op R2 VLAN 20, geen auth, geen preempt |
| 13 | OSPF authenticatie configureren | ✗ | Risico 13: "Area has no authentication", state INIT |
| 14 | Default route instellen op routers | ✗ | Risico 15: "Gateway of last resort is not set" |
| 15 | DHCP snooping inschakelen + R1 DHCP fixen | ✗ | Risico 16: geen snooping, R1 geen default-router |
| 16 | WPA2 instellen op beide access points | ✗ | Risico 17: encryption disabled |
| 17 | Vervang `enable password` door `enable secret` | ✗ | Risico 18: `enable password cisco` plain text |
| 18 | Default gateway instellen op PC's | ✗ | Risico 19: gateway = 0.0.0.0 |
| 19 | `login local` op alle VTY lines | ✗ | Risico 10: S0 en S1 vty 5-15 met `login` zonder "local" |
