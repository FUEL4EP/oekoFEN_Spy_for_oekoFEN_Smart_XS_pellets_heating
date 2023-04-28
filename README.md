# oekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FFUEL4EP%2FoekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) <a href='https://ko-fi.com/FUEL4EP' target='_blank'><img height='20' style='border:0px;height:20px;' src='https://cdn.ko-fi.com/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>



## Objectives of a [oekofen_spy](https://nc-x.com/oekofen-spy), InfluxDB, and Grafana proxy server
- analysis of a Oekofen Smart XS pellets heating by visualizing graphically the data of the Smart XS' Pelletronic Touch JSON interface

- set-up a Raspberrry Pi 3B+ based proxy server with wifi connection to your LAN's router
	+ that is running the [oekofen_spy](https://nc-x.com/oekofen-spy) application
	+ that is running an [InfluxDB](https://www.influxdata.com/) data base server
	+ that is running a [Grafana](https://grafana.com/) server for visualizing captured data
	+ the **oekofen_spy software** can be dowloaded from [GitLab](https://gitlab.com/p3605/oekofen-spy)
	+ in my case I do not have a wired Ethernet LAN cabeling to my cellar
	+ wired connection to a Oekofen Smart XS pellets heating by a Ethernet patch cable
	+ wifi connection to your LAN's router
	+ support a firewall to isolate and protect the Oekofen Smart XS pellets heating
	+ the proxy server can be put into a DMZ if your router is supporting a DMZ with a wifi access point
	+ support a SSD drive with sufficient storage capacity in order to store measurement data of a longer time frame
	+ independend stand-alone operation and data collection of the [oekofen_spy](https://nc-x.com/oekofen-spy) proxy server even if the WLAN is switched off, e.g. during night time
	+ automatic unattended updates of the Raspberry Pi OS
	+ ssh maintenance connection to a dedicated client of your LAN, e.g your laptop

## Required Hardware

- please carefully follow below **recipies** for a reduced RF disturbance of the Raspberry Pi's embedded WiFi
	+ in my case, my WiFi router is located in the attic floor, the Oekofen heating is in the cellar, 3 reinforced-concrete floor are in between, therefore the WiFi connection is very poor and each dB transmission gain is important
	+ if your router's antenna is turnable, please adjust it for best wifi transmission to such an angle that a plane perpenticular to the antenna stick is going through the oekofen_spy Raspberry Pi's location in the cellar
	+ if you are still experiencing too low wifi signal levels in your cellar, you may experiment with a [directional YAGI WLAN Antenna EXTENSION for 2.4 GHz](https://www.thingiverse.com/thing:19548)
	+ **note:** any directional antenna results in worse RF radiation characteristics in non-preferred directions
	+ despite following these recipies, I am experiencing temporary RF disturbances and connection problems to the oekofen_spy Raspberry Pi in the ceellar in the following situations
	+ my neighbour is using a baby phone which is heavily disturbing the wifi transmission
	+ the Oekofen Smart XS is igniting, obviously the fan of the Smart XS heating does a lot of RF disturbances
	+ the Oekofen Smart XS is filling the pellets buffer store. A cleaning with a running fan is part of that process
	+ in case of such RF disturbances, please just wait until the source of the distubances is switched off. Then a connnection should be possible again without any further action.
- Raspberry Pi 3B+.
	+ if you can buy or [prepare](https://geeks-r-us.de/2019/02/03/raspberry-pi-3b-mit-externer-wlan-antenne/) a Raspberry Pi 3B+ board with an U.FL external antenna connector, go for it and enjoy a better WiFi transmission
- [Geekworm X850 V3.1 USB 3.0 mSATA SSD Storage Expansion Board for Raspberry Pi 3B+/3B](https://geekworm.com/products/raspberry-pi-3-x850-v3-0-usb-3-0-msata-ssd-storage-expansion-board), available e.g at Amazon
	+ please ensure that you purchase the 3.1 version
	+ please do not use older versions with higher RF emissions and disturbances
	+ wiki is [here](https://wiki.geekworm.com/X850)
	+ [installation guide](https://wiki.geekworm.com/Installation_Guide_For_X850_V3.0_New_Version) V3.0 version
- mSATA SSD 64 GB 3D NAND MLC SATA III mSATA (30 x 50,9 mm) [e.g. from here](https://www.amazon.de/Integrierte-Solid-State-Festplatte-Hochleistungs-Festplatte-Desktop-Laptop-Einschlie%C3%9Flich/dp/B07NJHX5JL)
- [Raspberry Pi USB 2.0 /USB 3.0 Connector Bridge / USB 3.0 Cable for Raspberry Pi 4B / 3B+(Plus)&X180/150 Board](https://de.aliexpress.com/item/4000807147152.html)
	+ please do not the connector bridge shipped together with the X850 board since it is not shielded and is causing RF disturbances
	+ please ensure a USB3.1 version with less disturbance of the Raspberry Pi's WiFi
- if you are experiencing stability problems, then connect [decoupling capacitors](./decoupling_capacitors.png) to the GND and +5.0V GPIO pins of the Raspberry Pi 3B+
	+ 2x 470 uF electrolytic capacitor, 10V, take care of the polarity!
	+ 1x 0.15 uF ceramic capacitor
-  M2.5 12 mm nylon hexagonal spacers, nuts, and screws, e.g. from [here](https://www.amazon.de/Male-Female-Motherboard-Sortiment-Montieren-Kunststoffbox/dp/B07NK3S7C1?language=en_GB)
	+ please do not use the metal spacers shipped with the X850 board; they would disturb the Raspberry Pi's WiFi
	+ please use nylon spacers for not disturbing the Raspberry Pi's embedded WiFi
- a plastic case
	+ please do not use a metal case; it would worsen the Raspberry Pi's WiFi transmission
	+ I've [3D printed](./oekoFEN_Spy_Raspi_3B+_X850_mSata_SSD_case.png) this [PI case (room available for X850 Msata and Pi hat)](https://www.thingiverse.com/thing:3530981/remixes)
		* however, it did not fit perfectly to the X850 V3.1 board, some tweaking of the case and x850 board was necessesary
		* I've been to lazy to construct a fitting case
		* please be encouraged to share your fitting case
- System-S USB Type C Input to 2X Micro USB Output Y Cable Splitter Adapter Cable from e.g. [here](https://www.amazon.de/-/en/System-S-Input-Output-Splitter-Adapter/dp/B07FPBZTQN)
- original Raspberry Pi 4 power supply (yes Raspberry Pi 4 is correct) from e.g. [here](https://www.amazon.de/-/en/Raspberry-Pi-official-power-supply/dp/B07TMPC9FG/)
	+ it can supply a higher 3A current than a standard Raspi3 power supply (2.5A) for additionally supplying the SSD
	+ use in conjunction with above Y splitter cable
- a CAT6 1.5 m Ethernet patch cable

## Software

### Advisory
- since I don't want to break my production system and I do not have a separate test system, I unfortunately can not test the below software installation guidelines
- I had to do a lot of trial and error experiments to get my system up an running
- I am writing below instructions from my memory and may some parts in my description
- in case you are experiencing trouble with my instructions, please raise an issue at github [here](https://github.com/FUEL4EP/oekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating/issues) and ask for help

### Install Raspberry Pi OS (64-bit)

- dowload the latest version of Raspberry Pi OS (64Bit) from [here](Raspberry Pi OS (64-bit)
- when writing this README.md, the latest version was [version 2023-02-21-raspios-bullseye-arm64.img.xz](https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2023-02-22/2023-02-21-raspios-bullseye-arm64.img.xz)
- unpack and install this OS on an appropriate SD card and boot the Raspberry Pi 3B+
- for Linux OS, unpack with xz -d -v \<filename\>
### Prepare the Raspberry Pi 3B+ for an USB drive
- please follow these [instructions](https://www.instructables.com/Booting-Raspberry-Pi-3-B-With-a-USB-Drive/)
- **note:** The Raspberry Pi 3 B+ can be USB booted out-of-the-box.
### Harden your Raspberry Pi
- apply appropriately [this hardening guide](https://chrisapproved.com/blog/raspberry-pi-hardening.html)
	+ do not disable the Raspberry Pi's wifi since it is needed for this application

## To be continued ..
- please wait a bit, I am working on it


## Some recommendations for settings of the Oekofen Smart XS pellets heating
- to be done
