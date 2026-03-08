# Week 5 : OSINT
Noteer de commando’s die je hebt gebruikt.  
Leg het resultaat uit en ondersteun dit met screenshots.  


## Opdracht 1: [SHODAN](https://www.shodan.io/dashboard)-zoekopdracht
We gaan nu een zoekopdracht uitvoeren op SHODAN.  

> opgezocht hoe ik shodan kan gebruiken:
> - [Mastering Shodan Search Engine](https://infosecwriteups.com/mastering-shodan-search-engine-8c80b80dae09)

---

### Vraag 1A: Hoeveel apparaten worden blootgesteld?
Zoek op poort 502 (modbus protocol poort)
Ondersteun dit met een screenshot waar duidelijk je zoek term zichtbaar is.  

<img width="3798" height="1820" alt="image" src="https://github.com/user-attachments/assets/aea33eca-23db-4d9c-a11d-012f87ea2fef" />

> port:502

Ik zie `top results 388,162` dus er zijn 388,164 modbus devices die verbonden zijn aan het internet, waamee waarschijnlijk verbonden kan worden

---

### Vraag 1B: Hoeveel apparaten worden blootgesteld? Ondersteun dit met een
Zoek op poort 502 (modbus protocol poort) en op vendor: Schneider Electric
screenshot waar duidelijk je zoek term zichtbaar is. Leg verder uit wat je te zien krijgt.  

> port:502 Schneider Electric

#### crt.sh
op de website van Schneider electric heb ik bij certificate dit gevonden:  
<img width="2833" height="1506" alt="image" src="https://github.com/user-attachments/assets/e80fadd2-6ed8-4ab0-8aa5-69af3bee8231" />

Uit dit heb ik `se.com` en `Schneider Electric Industries SAS` opgezocht in [crt.sh](https://crt.sh/?Identity=se.com)  
Ik ben eerst door de lijst gegaan en zag dat sommige bad URL's hadden. Er waren ook een aantal die wel pagina's hadden met meer info.  
Ik probeerde te kijken of ik de SHA-256 terug kon vinden, maar de lijst was zo groot dat ik besloot om mijn zoekopdracht specifieker te maken met de advanced options.  
Daar zag ik dat ik kon filteren op SHA-256. Toen ik dat deed, vond ik het SSL-certificaat gelijk. 

[Schneider electric ssl](https://crt.sh/?sha256=667be4e37d2cae9363bbc57b73d3a0fb01a2f3a32c85ad18ca8bffcbf78661df&exclude=expired)  

<img width="2431" height="1825" alt="image" src="https://github.com/user-attachments/assets/2cc6d74e-b608-4dbd-83b0-6174581c9136" />

Hier zag ik dat, onder subject, de commonName en organizationName kwamen overeen. Maar de countryName was FR, en ik zag nl in de url.  
ik ben terug naar de certificate viewer gegaan en vondt daar bij details ook FR bij subject:  

<img width="2194" height="1667" alt="image" src="https://github.com/user-attachments/assets/6b64b7b1-7d53-4bc2-aaf1-f7b8c256b422" />

Dus dit is wel de juiste certificate, in shodan ga ik nu zoeken naar:
- org:"se.com"
  - <img width="3034" height="1066" alt="image" src="https://github.com/user-attachments/assets/b5eecf64-daf0-44fb-98eb-add767fdfa8e" />
- ssl:"se.com"
  - <img width="3130" height="1343" alt="image" src="https://github.com/user-attachments/assets/4a269173-7713-4dc7-9abd-896f9a29b2c3" />
  - gefilterd op NL omdat de eerste lijst te groot was, maar zag Schneider Electric niet in de orginisations lijst
  - Daarna gefilterd op FR en zag daar wel: Schneider Electric IT Corporation
  - <img width="3121" height="1819" alt="image" src="https://github.com/user-attachments/assets/55720ea8-c34e-4f6f-9463-1d0b02ff805b" />
  - <img width="3815" height="1074" alt="image" src="https://github.com/user-attachments/assets/28921093-dd0b-4af8-ac6f-0a9ec9d0310d" />
  - <img width="3800" height="1838" alt="image" src="https://github.com/user-attachments/assets/0a45228f-8605-46b0-ace4-4b61705ae758" />

---

### Vraag 1C: Hoeveel apparaten worden blootgesteld? Ondersteun dit met een
Zoek op poort 502 (modbus protocol poort), vendor: Schneider Electric en een gekozen [modelnummer]
screenshot waar duidelijk je zoek term zichtbaar is. Leg verder uit wat je te zien krijgt.

---

## Opdracht 2: GOOGLE DORKS-zoekopdracht
We gaan nu een GOOGLE DORKS zoekopdracht uitvoeren.  
In jouw ICS OSINT spreadsheet (ICS-OSINT.xlsx, zie DLO voor de file) vind je heel veel zoektermen voor alle mogelijke vendors.  
Ga naar Google en gebruik de zoekterm uit de ICS OSINT spreadsheet om te zoeken naar webservers van Schneider Electric apparaten die publiekelijk zijn blootgesteld.

---

### Vraag 2A: Welke zoekterm heb je in het document (ICS-OSINT.xlsx) gevonden?
Leg uit hoe je dit hebt gevonden. Ondersteun dit met een screenshot.

---

### Vraag 2B: Kies uit de google-resultaat een gevonden Schneider Electric
Industrial web control. Ondersteun dit met een screenshot. Omschrijf ook wat je ziet.
