
## Set-up of a Raspberry Pi 3B+ based WiFi proxy server for Oekofen_Spy

- based on  [oekofen-spy](https://nc-x.com/oekofen-spy) (C) Peter Fürle
- and sources from https://gitlab.com/p3605/oekofen-spy/-/tree/main (C) Peter Fürle
- Picture of proxy server:
![pic](./untar_dir/oekofen-spy/my_oekofen_spy_extension/oekoFEN_Spy_Raspi_3B+_X850_mSata_SSD_case.png)
- sketch of the used network topology:
![png](./untar_dir/oekofen-spy/my_oekofen_spy_extension/oekoFEN_Spy_network_diagram.png)

- used Grafana dashboard:

  ![png](./untar_dir/oekofen-spy/my_oekofen_spy_extension/Grafana_dashboard_example.png)

- adjustable Grafana variables:

  ![png](./untar_dir/oekofen-spy/my_oekofen_spy_extension/variables.png)



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
	+ bridge functionality between the Raspberry Pi's eth0 and wlan0 interfaces
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
	+ if you are still experiencing too low wifi signal levels in your cellar, you may experiment with a [directional YAGI WLAN Antenna EXTENSION for 2.4 GHz](https://www.thingiverse.com/thing:19548) or a [directional panel antenna](https://www.amazon.de/-/en/Network-APA-M25-directional-connector-WL-ANT-157/dp/B00R1PA9EO) (please note that this panel antenna is radiating only into one direction)
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
- if you are experiencing stability problems, then connect [decoupling capacitors](./untar_dir/oekofen-spy/my_oekofen_spy_extension/decoupling_capacitors.png) to the GND and +5.0V GPIO pins of the Raspberry Pi 3B+ 
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
- I had to do a lot of trial and error experiments to get my system up and running
- I am writing below instructions from my memory and may miss some parts in my description
- in case you are experiencing trouble with my instructions, please raise an issue at github [here](https://github.com/FUEL4EP/oekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating/issues) and ask for help

### Install Raspberry Pi OS (64-bit)

- dowload the latest version of Raspberry Pi OS (64Bit) from [here](https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-64-bit)
	+ choose 'Raspberry Pi OS with desktop 64-Bit'
- when writing this README.md, the latest version was [version 2023-05-03-raspios-bullseye-armhf-full.img.xz](https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2023-05-03/2023-05-03-raspios-bullseye-armhf-full.img.xz)
- unpack and install this OS on an appropriate SD card and boot the Raspberry Pi 3B+
- for flashing the SD card [balenaEtcher](https://www.balena.io/etcher#download-etcher) is recommended
- for Linux OS, unpack with xz -d -v \<filename\>
- a getting-started documentation is available [here](https://www.raspberrypi.com/documentation/computers/getting-started.html):
	+ set location, language, keyboard, and time zone
	- as user name, please enter 'smartxslogin'
	- choose a safe password with at least 8 characters, write it down
	- set-up your wifi connection
	- update the Raspberry Pi OS software
	- restart
	
### Check login and your WiFi connection
- login again after the restart
- check that you can access the internet via your WiFi connection

### Prepare the Raspberry Pi 3B+ for an USB drive
- please follow these [instructions](https://www.instructables.com/Booting-Raspberry-Pi-3-B-With-a-USB-Drive/)
- **note:** The Raspberry Pi 3 B+ can be USB booted out-of-the-box.
### Harden your Raspberry Pi
- apply appropriately [this hardening guide](https://chrisapproved.com/blog/raspberry-pi-hardening.html)
	+ do not disable the Raspberry Pi's wifi since it is needed for this application

### Disable auto-login

- please follow these [instructions](https://www.raspberrypi-spy.co.uk/2022/02/disable-auto-login-in-raspberry-pi-os/)
- reboot and check a login
- shutdown

### Copy SD card to your mSata SSD
- plug your maSata SSD card  into the X850 board
- use [balenaEtcher](https://www.balena.io/etcher#download-etcher) for cloning the SD card#s content to the SSD mSata card
- connect the X850 board with your Raspberry Pi 3B+, ensure that your power supply is strong enough, see aboove hardware guidelines
- power-up the Raspberry Pi 3B+
- login in

### Reduce write cycles and extend SSD life expectancy

- some guidelines for reducing the write cycles to tthe mSata SSD canb be found [here](https://community.home-assistant.io/t/steps-to-reduce-write-cycles-and-extend-sd-ssd-life-expectancy/291718) or [here](https://www.laub-home.de/wiki/Raspberry_Pi_Schreiboperationen_minimieren) (in German language)
- add at the end of '/etc/fstab' the following line
> tmpfs /tmp tmpfs defaults,noatime,nosuid,nodev,noexec,mode=1777,size=128M 0 0
- this is mounting /tmp as a ramdrive tmpfs
- disable swapping by entering the following commands in a terminal window
> sudo systemctl disable dphys-swapfile  
sudo systemctl stop dphys-swapfile
- reboot and login again

### Install git and clone the repository from Github

-	execute the following commands in a LXterminal window:  

> cd ${HOME}  
> sudo apt install git  
git clone https://github.com/FUEL4EP/oekoFEN_Spy_for_oekoFEN_Smart_XS_pellets_heating.git

- This command sequence will download the repository 'FUEL4EP/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating' from Github into the directory '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating'
- These commands are also stored in the script 'git_clone.bsh'. Please note that this script needs to be executed as normal user!

### Customize the installation to your network and system

- Please open in a text editor the bash script '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/customize_installation.bsh'
- At the top you will find a customization section:
 ![png](./untar_dir/oekofen-spy/my_oekofen_spy_extension/customization_section.png)
 	+ d:= digit
 	+ h:= hexadecimal character	
- Please change the entries after the equal sign to fit to your network and system set-up
- An example of a customization is here:
 ![png](./untar_dir/oekofen-spy/my_oekofen_spy_extension/customization_section_example.png)
 
- now run the customization script as sudo:
> sudo ./customize_installation.bsh
- The script is patching the subdirectory '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/${MY\_UNTAR\_DIR\_MOD}'
- Please check the patched set-up files in this directory

### Do a first set of software installations and configuration

- ensure that the customization sections in '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/install_software_packages\_1.bsh' and '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/customize\_installation.bsh' are consistent

- then execute this script as normal user

> bash ${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/install\_software_packages_1.bsh

### Patch the installation
- ensure that the customization sections in '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/patch\_installation.bsh' and '${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/customize\_installation.bsh' are consistent

- then execute the script that will patch the root directory '/':

> sudo ${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/patch_installation.bsh

### Reboot

- reboot as normal user without sudo:

> reboot

- after the reboot you can check part of the new configuration e.g. by the commands

> ifconfig  
> hostname

- please note that sudo is now requiring to enter a password

### Final installation of influxdb and grafana

- execute the script

> sudo ${HOME}/oekoFEN\_Spy\_for\_oekoFEN\_Smart\_XS\_pellets\_heating/my\_install\_2.bsh

- this script will execute a reboot at the end

### Final checks of the installation

- to be done

## Some recommendations for settings of the Oekofen Smart XS pellets heating
- to be done
