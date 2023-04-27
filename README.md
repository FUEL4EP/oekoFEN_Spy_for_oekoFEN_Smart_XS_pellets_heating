# oekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FFUEL4EP%2FoekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) <a href='https://ko-fi.com/FUEL4EP' target='_blank'><img height='20' style='border:0px;height:20px;' src='https://cdn.ko-fi.com/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

Set-up and customization of an oekoFEN-spy Raspi 3B+ server for observing an oekoFEN Smart XS pellets heating



## Required Hardware

- please carefully follow below recipies for a reduced RF disturbance of the Raspberry Pi's embedded WiFi
	+ in my case, my WiFi router is located in the attic floor, the Oekofen heating is in the cellar, 3 reinforced-concrete floor are in between, therefore the WiFi connection is very poor and each dB transmission gain is important
- Raspberry Pi 3B+
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

## software section is under construction

## coming soon
