# Inrichten van Pentestlab met behulp van Docker en Labshock evenals het installeren van diverse pentesting tools

## Opdracht 1: OT labomgeving
### stappen
- git clone https://github.com/zakharb/labshock.gi
- https://github.com/zakharb/labshock/wiki/Configuration-Guide
  - onfigureer alleen de networks, router, scada, plc en volumes
- Ip voor plc & scada
  - `nano ~/labshock-2.1.5/oilsprings/plc/entrypoint.sh` -> `192.168.2.254`
    - `ip route add 192.168.3.0/24 via 192.168.2.254`
  - `nano ~/labshock-2.1.5/oilsprings/scada/entrypoint.sh` -> `192.168.3.25`
    - `ip route add 192.168.2.0/24 via 192.168.3.254`
- sudo apt install docker-compose
- `docker-compose build`
- `docker-compose up -d`

### docker-compose.yml
```yml
name: labshock

services:
  portal:
    image: zakharbz/labshock-portal:latest
    ports:
      - '443:443'
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./docker-compose.yml:/app/docker/docker-compose.yml
      - portal-data:/app/config/
    networks:
      - portal_network

  plc:
    build: ./oilsprings/plc/
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    networks:
      l2_network:
        ipv4_address: 192.168.2.10
    ports:
      - "8080:8080"
    volumes:
      - plc-data:/workdir/webserver

  router:
    build: ./oilsprings/router/
    privileged: true
    restart: unless-stopped
    networks:
      l2_network:
        ipv4_address: 192.168.2.254
      l3_network:
        ipv4_address: 192.168.3.254
#    command: /bin/bash -c "echo 1 > /proc/sys/net/ipv4/ip_forward && /entrypoint.sh"

  scada:
    build: ./oilsprings/scada/
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    networks:
      l3_network:
        ipv4_address: 192.168.3.20
    ports:
      - '1881:1881'
    volumes:
      - scada-data:/usr/src/app/FUXA/server/_appdata

networks:
  portal_network:
    driver: bridge
  l2_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.2.0/24
  l3_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.3.0/24

volumes:
  scada-data:
  plc-data:
  ews-data:
  portal-data:

```

### test
terminal:
- `ping 192.168.2.10`
- `ping 192.168.3.20`
- `docker exec -it labshock-scada-1 bash`
  - `ping 192.168.2.10`
 
localhost
- `http://localhost:8080/`
  - username & password: openplc
- `http://localhost:1881/`

## Opdracht 2: Clone PLCSCAN
```
sudo git clone https://github.com/meeas/plcscan.git
```

## Opdracht 3: Clone ICSSecurityscripts
```
git clone https://github.com/tijldeneut/ICSSecurityScripts.git
```

## Opdracht 4: Clone REDPOINT
```
git clone https://github.com/digitalbond/Redpoint.git
```
verplaats de files naar nmap:
```
sudo cp Redpoint/*.nse /usr/share/nmap/scripts/
sudo nmap --script-updatedb
```
> copy alle `.nse`files naar nmap/scripts
> 2de command om nmap te laten weten dat je iets heb toegeveogd

## Opdracht 5: Installeer Modbus-cli
```
sudo gem install modbus-cli
```
