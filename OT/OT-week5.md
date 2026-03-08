# Week 5 : OSINT
Noteer de commando’s die je hebt gebruikt.  
Leg het resultaat uit en ondersteun dit met screenshots.  


## Opdracht 1: [SHODAN](https://www.shodan.io/dashboard)-zoekopdracht
We gaan nu een zoekopdracht uitvoeren op SHODAN.  

> opgezocht hoe ik shodan kan gebruiken:
> - [Mastering Shodan Search Engine](https://infosecwriteups.com/mastering-shodan-search-engine-8c80b80dae09)
> - [Search Query Fundamentals](https://help.shodan.io/the-basics/search-query-fundamentals)

---

### Vraag 1A: Hoeveel apparaten worden blootgesteld?
Zoek op poort 502 (modbus protocol poort)
Ondersteun dit met een screenshot waar duidelijk je zoek term zichtbaar is.  

<img width="1287" height="1820" alt="image" src="https://github.com/user-attachments/assets/aea33eca-23db-4d9c-a11d-012f87ea2fef" />

> port:502

Ik zie `top results 388,162` dus er zijn 388,164 modbus devices die verbonden zijn aan het internet, waamee waarschijnlijk verbonden kan worden

---

### Vraag 1B: Hoeveel apparaten worden blootgesteld? Ondersteun dit met een
Zoek op poort 502 (modbus protocol poort) en op vendor: Schneider Electric
screenshot waar duidelijk je zoek term zichtbaar is. Leg verder uit wat je te zien krijgt.  

#### crt.sh (extra)
op de website van Schneider electric heb ik bij certificate dit gevonden:  
<img width="1287" height="1820" alt="image" src="https://github.com/user-attachments/assets/e80fadd2-6ed8-4ab0-8aa5-69af3bee8231" />

Uit dit heb ik `se.com` en `Schneider Electric Industries SAS` opgezocht in [crt.sh](https://crt.sh/?Identity=se.com)  
Ik ben eerst door de lijst gegaan en zag dat sommige bad URL's hadden. Er waren ook een aantal die wel pagina's hadden met meer info.  
Ik probeerde te kijken of ik de SHA-256 terug kon vinden, maar de lijst was zo groot dat ik besloot om mijn zoekopdracht specifieker te maken met de advanced options.  
Daar zag ik dat ik kon filteren op SHA-256. Toen ik dat deed, vond ik het SSL-certificaat gelijk. 

[Schneider electric ssl](https://crt.sh/?sha256=667be4e37d2cae9363bbc57b73d3a0fb01a2f3a32c85ad18ca8bffcbf78661df&exclude=expired)  

<img width="1287" height="1820" alt="image" src="https://github.com/user-attachments/assets/2cc6d74e-b608-4dbd-83b0-6174581c9136" />

Hier zag ik dat, onder subject, de commonName en organizationName kwamen overeen. Maar de countryName was FR, en ik zag nl in de url.  
ik ben terug naar de certificate viewer gegaan en vondt daar bij details ook FR bij subject:  

<img width="1287" height="1820" alt="image" src="https://github.com/user-attachments/assets/6b64b7b1-7d53-4bc2-aaf1-f7b8c256b422" />

Dus dit is wel de juiste certificate, in shodan ga ik nu zoeken naar:
- org:"se.com"
  - <img width="1287" height="1066" alt="image" src="https://github.com/user-attachments/assets/b5eecf64-daf0-44fb-98eb-add767fdfa8e" />
- ssl:"se.com"
  - <img width="1287" height="1343" alt="image" src="https://github.com/user-attachments/assets/4a269173-7713-4dc7-9abd-896f9a29b2c3" />
  - gefilterd op NL omdat de eerste lijst te groot was, maar zag Schneider Electric niet in de orginisations lijst
  - Daarna gefilterd op FR en zag daar wel: Schneider Electric IT Corporation
  - <img width="1287" height="1819" alt="image" src="https://github.com/user-attachments/assets/55720ea8-c34e-4f6f-9463-1d0b02ff805b" />
  - <img width="1287" height="1074" alt="image" src="https://github.com/user-attachments/assets/28921093-dd0b-4af8-ac6f-0a9ec9d0310d" />
  - <img width="1287" height="1838" alt="image" src="https://github.com/user-attachments/assets/0a45228f-8605-46b0-ace4-4b61705ae758" />

dit heeft poort 433 open,  
de opdracht was om Schneider Electric op poort 502 te zoeken

#### port:502 Schneider Electric
<img width="1287" height="434" alt="image" src="https://github.com/user-attachments/assets/aca5b1af-0026-4edc-8e34-522d5d15b8e4" />  
<img width="1287" height="416" alt="image" src="https://github.com/user-attachments/assets/0c905a42-1e98-47ba-8701-57114ceb00f0" />
<img width="1287" height="439" alt="image" src="https://github.com/user-attachments/assets/2a291a4d-0c0d-4098-9f7d-fe94d7177d6a" />

> port:"502" org:Schneider Electric, org:Schneider Electric port:"502", port:502 vendor:"Schneider Electric" -> geen results


Met `port:502 "Schneider Electric"` zie je wel alle aparaten die port 502 open hebben met Schneider Electric als Device Identification
<img width="1287" height="1812" alt="image" src="https://github.com/user-attachments/assets/afd73136-2903-4c94-816d-30be3f0ed538" />

in totaal 2.737 Schneider Electric apparaten met poort 502 open op het internet.

open ports:  
<img width="1287" height="522" alt="image" src="https://github.com/user-attachments/assets/3c544867-c3f4-42e8-bd17-0b59aa8df423" />
<img width="1287" height="526" alt="image" src="https://github.com/user-attachments/assets/7fc0cd11-d450-4937-a82a-95a761e8feb3" />
<img width="1287" height="1067" alt="image" src="https://github.com/user-attachments/assets/c463320d-10a7-4015-88ab-52b5f0a9ad3b" />

uit de lijst hebben alle devices 1 of meerdere poorten open, waarvan 1 open port 502 is

---

### Vraag 1C: Hoeveel apparaten worden blootgesteld? Ondersteun dit met een
Zoek op poort 502 (modbus protocol poort), vendor: Schneider Electric en een gekozen [modelnummer]
screenshot waar duidelijk je zoek term zichtbaar is. Leg verder uit wat je te zien krijgt.

van claude heb ik begrepen dat de moddelnummer naast de rodr Schneider electric staat:  
<img width="1287" height="814" alt="image" src="https://github.com/user-attachments/assets/2faf0018-57a5-44dc-94e8-c2d7aa3e0fcf" />

search naar:
- Device Identification: Schneider Electric TM221CE16T
  - <img width="1287" height="1824" alt="image" src="https://github.com/user-attachments/assets/4b464636-9aae-4b66-80e8-71ceaf5a74f2" />
  - 182 apparaten blootgesteld
  - port:502 erbij -> 170 apparaten blootgesteld
    - <img width="1287" height="1818" alt="image" src="https://github.com/user-attachments/assets/c4cbcc98-7b4f-41c1-a83b-35e7ed5204df" />
- Device Identification: Schneider Electric TM251MESE V05.00.08.07
  - <img width="1287" height="1770" alt="image" src="https://github.com/user-attachments/assets/9dbb1502-cfd6-4a11-86a2-a6bd7a310369" />
  - 4 apparaten blootgesteld
  - port:502 erbij -> geen verschill
    - <img width="1287" height="1774" alt="image" src="https://github.com/user-attachments/assets/430a3250-545b-4229-a5af-91a2d283768f" />


Device Identification: Schneider Electric TM221CE16T port:502
Dit leverde 170 blootgestelde apparaten op.

Device Identification: Schneider Electric TM251MESE V05.00.08.07 port:502 (met een versie nummer erbij)
Dit leverde 4 blootgestelde apparaten op, allemaal in Spanje.

Ik heb ook eerst gezocht zonder port:502, wat bij de eerste 182 resultaten gaf.  
en bioj de 2de veranderde niets.

---

## Opdracht 2: GOOGLE DORKS-zoekopdracht
We gaan nu een GOOGLE DORKS zoekopdracht uitvoeren.  
In jouw ICS OSINT spreadsheet (ICS-OSINT.xlsx, zie DLO voor de file) vind je heel veel zoektermen voor alle mogelijke vendors.  
Ga naar Google en gebruik de zoekterm uit de ICS OSINT spreadsheet om te zoeken naar webservers van Schneider Electric apparaten die publiekelijk zijn blootgesteld.


---

### Vraag 2A: Welke zoekterm heb je in het document (ICS-OSINT.xlsx) gevonden?
Leg uit hoe je dit hebt gevonden. Ondersteun dit met een screenshot.

Shneider electric in ICS-OSINT.xlsx:  

ctrl + f op: `Schneider Electric`
<img width="1287" height="670" alt="image" src="https://github.com/user-attachments/assets/50f0bf92-ac5f-4d83-b18e-232b9a35da61" />  
<img width="1287" height="434" alt="image" src="https://github.com/user-attachments/assets/a2f1f3dd-5c29-4555-b3e8-f6a8f9fd096f" />


---

### Vraag 2B: Kies uit de google-resultaat een gevonden Schneider Electric
Industrial web control. Ondersteun dit met een screenshot. Omschrijf ook wat je ziet.


#### intitle:"Schneider Electric Telecontrol
<img width="1287" height="1216" alt="image" src="https://github.com/user-attachments/assets/913bfddd-1b1e-4c41-ba42-8b14bbdedf67" />

<img width="1287" height="763" alt="image" src="https://github.com/user-attachments/assets/b20cff1d-65fd-40eb-867b-6a4ead0d2f0a" />  
<img width="1287" height="344" alt="image" src="https://github.com/user-attachments/assets/2f20f86d-869f-477e-b604-abc1e8c21b5c" />  
<img width="1287" height="1028" alt="image" src="https://github.com/user-attachments/assets/4a8bd752-6269-413f-be61-a4ad22fcb358" />

ik heb `site: OLOROn opgezocht` daar zag ik dat het een locatie was: `oloron-sainte-marie`, dus oloron is volgens mij de locatie van waar de device is.  
dus de `H-4 MAP S.A` is de locatie van de andere3  

ik heb daarna deze gevonden:  
<img width="1287" height="886" alt="image" src="https://github.com/user-attachments/assets/8fbea045-7bd9-42c4-bf5c-64e13af76d66" />  
met site `RAPALE` een locatie in italie

wat ik zie is een inlog pagina en de locatie van waar het apparaat zit.  


---

#### De rest
alles bahalve `intitle:"Schneider Electric Telecontrol` gaf resultaten over producten die schneider verkoopt en documentatie.  
deze hadden geen url naar inlog paginas
<img width="1287" height="1911" alt="image" src="https://github.com/user-attachments/assets/0edb3dce-4845-46df-a87c-b0215a374c3a" />  


#### ik ging verkeerd zoeken
ik moest nog `inurl` of `intitle` erbij zetten  
ik ben terug gegaan bijna alles van Schneider geprobeerd met `inurl` en `intitle` maar weer hetzelfde gevonden


daarna vroeg ik aan claude wat ik nog meer zou kunnen testen en: `inurl:/portal/portal.mwsl` was 1 van de opties  
<img width="1287" height="1356" alt="image" src="https://github.com/user-attachments/assets/cc1cfc88-8bc5-4bd6-9762-046960e56d58" />  
<img width="1287" height="1582" alt="image" src="https://github.com/user-attachments/assets/b0396645-11a3-4b6d-8be7-bae86ecd2a64" />  
<img width="1287" height="1598" alt="image" src="https://github.com/user-attachments/assets/354527b6-9b07-44ca-adab-17b36534fc5e" />

---

<img width="1287" height="1182" alt="image" src="https://github.com/user-attachments/assets/a8470816-5085-4515-a5cd-0ae2a6032fec" />  
<img width="1287" height="1586" alt="image" src="https://github.com/user-attachments/assets/9c732773-1de4-4e8c-9e33-f564558d573d" />  
<img width="1287" height="1295" alt="image" src="https://github.com/user-attachments/assets/7e84a990-e9c9-457f-a79e-141dd4a91e97" />

---

<img width="1287" height="1605" alt="image" src="https://github.com/user-attachments/assets/f6e61987-a6e2-4030-b7f3-9edbb4df4644" />




