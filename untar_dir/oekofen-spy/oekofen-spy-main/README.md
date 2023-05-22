## Name
Oekofen-Spy .

## Description
**Attention:**
Due to extensive size of ready prepared raspberrypi image i had to remove it.

python script fetches JSON from pellet heating system Oekofen.
Data is sent to influx and dashboards are made with grafana.
Oekofen pellet stove heating systems are available in different equipment variants. Options can be the number of heating circuits, circulation pumps, solar systems with/without yield measurement, fresh water stations and more. They even may be connected to your Fronius solar inverter.

The Pelletronic-Touch heating control supports various energy saving options such as various eco modes and a weather forecast. There are also many parameters that can be set by the installer or the customer.

Often users changes do not result in what user had in mind. An assessment is difficult and usually takes place through time-consuming subjective observation.

With the help of Oekofen-Spy, graphic evaluations can support this. Goals would be:

- fewer ignitions per day,
- longer runtimes of the burner at 100% load,
- available hot water uring desired time,
- a maximum yield from solar thermal energy.

Just as a hint, solar thermal likes cold water! In other words, if the sun hits the solar panels at 10:00 a.m., the buffer should have cooled down as much as possible. Then solar energy can be transferred into the buffer as heat.

Using the graphic representation of storage tank temperatures bottom, middle and top helps a lot in understanding the affect of your changes. It is also easy to see when and why the target temperatures are set high and a burner request is made.

Ökofen-Spy accesses the live data from the heating system and shows the status of the system components.


## Visuals
![gauges](/media/oekofen-spy_Gauges_Schnellanzeige.png "fast information by gauges")
![states](/media/oekofen-spy_Zustaende_Tabelle.png "actual states")
![solar energy](/media/oekofen-spy_Temperaturverläufe_Kollektor.png "boiler bottom and panel temp")
![solar yield](/media/oekofen-spy_Solarertrag_AzimutKurve.png "azimut and solar yield")
![solar history](/media/oekofen-spy_14Tage_Solarhistorie.png "solar yield history")
![modulation](/media/oekofen-spy_oekofen_Laufzeit_summe.png "modulation level and runtime")
![stirling info](/media/oekofen-spy_Stirling_Zusatzinfo.png "additional info if stirling in action")
![runtime and starts](/media/Oekofen-Spy_Laufzeit_Start_Diff.png "starts in period").

with added csv support:

![feeding time](/media/Oekofen-Spy_Einschubzeit_csv.png "add values from daily .csv file")


## Installation using `install.sh` script
Using a RaspberryPi 3B+ is more powerful as needed.
run `install.sh`
- it updates your RaspberryPi
- it installs and starts your InfluxDB
- it's setting up database oekofen with user and password as needed
- it downloads, installs and starts Grafana 
- it installs python3-influxdb
- it restarts your RaspberryPi

**ATTENTION:**
 Touch V3.10c and V3.10d only works if language at your boiler control is set to english. This avoids german Umlaut ÄÖÜß in JSON-File. 

## only needed if you install manually without `setup.sh`

- **Install influxdb** with `sudo apt install influxdb`. 
- `sudo apt install influxdb-client` for terminal support
- configure influxdb with user = "pellematic",password = "smart" and dbname = "oekofen"

**enter `influx` in terminal**
```
create database oekofen
use oekofen
create user pellematic with password 'smart' with all privileges
grant all privileges on oekofen to pellematic
```

- **Install Grafana for Pi** 
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install -y grafana
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server

HINT: sudo apt-get install -y grafana=9.0.8 (if using 32bit operating system)

```
- and setup data source influxdb.
- Import Grafana-Plugin 'sun and moon' as data source before importing dashboard
- Import the Oekofen-spyxxx.json dashboard.
- enhance your python3.x installation with 

-- `sudo apt-get install python3-influxdb`
## end of your manual installation without `setup.sh`

### configure Grafana

To access data source settings, hover your mouse over the Configuration (gear) icon, then click Data sources, and then click the data source InfluxDB (InfluxQL)

- Name is the data source name. This is how you refer to the data source in panels and queries. We recommend something like InfluxDB.
- Default data source means that it will be pre-selected for new panels.
- URL	The HTTP protocol, IP address and port of your InfluxDB API. 
- InfluxDB API port is by default 8086. So please retype http://localhost:8086
- Database	same as above, name it oekofen
- User	The username you use to sign into InfluxDB, as above, user is 'pellematic'.
- Password	The password as above, it is 'smart'.
- HTTP mode, default is GET.

## Usage
please use the python script oekofen2influx.py from folder python3!

**edit your /etc/crontab to poll data every 4 minutes:**

`*/4 *  * * * pi   /usr/bin/python /home/pi/oekofen2influx.py`

modify the python script to access your Heater-IP and JSON password:

`json_quelle = "http://192.168.xx.xxx:4321/xxxx/all"`

## Backup
**to back up your influx database using usb-stick and crontab:**

`0 3   * * *  pi    /usr/bin/influxd backup -portable /media/tosh32/oekofenspy_influxdb_'date +\%Y-\%m-\%d'/`

please replace ' with back tics `

This saves your influx databases in a folder including the date in its name.

**You may create an image of your installation and send it to your NAS like this:**

```
sudo mkdir /media/qnap
sudo mount 192.168.xx.xxx:/Public /media/qnap
sudo dd if=/dev/mmcblk0 of=/media/qnap/oekofenspy.img bs=4M status=progress
```


## Calculations
newer stoves do have json parameter for pellets consumption and pellets storage. Mine are several years old, so i'm doing calculations based on runtime and power/kWh.
The crontab starts the python script every 4 minutes. So i get 1 value representing a duration of 4 minutes. For me its fine, if you want to have more detailled info, just fire it up everey 2 minutes. If done so, replace 4 with 2 in your dashboard formulas.
My stoves are 7.8kW and exactly whats calculated for the buildings. So, if it runs, it always runs with 100% modulation. 

![consumption emission](/media/oekofen-spy_calculations.png "how to calculate emission and consumption")

![consumption V3](/media/oekofen-spy_pellets_Verbrauch_V3.png "calculated consumption and .csv data").
![consumption V4](/media/oekofen-spy_pellets_Verbrauch_V3.png "calculated consumption collection V4").

#### To calculate the runtime use this formula:

`SELECT non_negative_derivative(count("pe1_L_modulation"), 1m) *4 FROM "4Weeks"."heizung" WHERE "pe1_L_modulation" >10 AND  $timeFilter GROUP BY time(1m)`

This collects each measure having a value higher than 10 from modulation. It is multiplicated by 4 due to a value every 4 minutes.

#### To calculate the pellets consumption:

`SELECT non_negative_derivative(count("pe1_L_modulation"), 1m) *4/60*7.8/4.9 FROM "4Weeks"."heizung" WHERE "pe1_L_modulation" >10 AND  $timeFilter GROUP BY time(1m)`

Same base as above. The runtime is given in minutes, so it's divided by 60 to get runtime in hours. This runtime in h is multiplicated by power 7.8kW and Pellets with 4.9kWh/kg. As an example, your stove with 8kW running 3h by 100% equals 24kWh. This divided by 4.9kWh/kg equals ~5kg pellets consumption.

#### To calculate emmissions CO2

`SELECT non_negative_derivative(count("pe1_L_modulation"), 1m) *4/60 * 7.8 * 9  FROM "4Weeks"."heizung" WHERE "pe1_L_modulation" >10 AND  $timeFilter GROUP BY time(1m)`

Same base as above, runtime in hours ist multiplicated by Power 7.8kW and 9g/kWh as mentioned by SIR 2007.

#### To calculate dust / particular matter 

`SELECT non_negative_derivative(count("pe1_L_modulation"), 1m) *4/60*7.8*0.05 FROM "4Weeks"."heizung" WHERE "pe1_L_modulation" >10 AND  $timeFilter GROUP BY time(1m)`

My stove is a condensing version coupled to floor heating system. So i'm calculating with 0.05g/kWh particular matter. 

#### to calculate the amount spent for pellets used 

just multiply your pellets consumption by price you paid for.

`SELECT non_negative_derivative(count("pe1_L_modulation"), 1m) *4/60 * 7.8 / 4.9 * 0.213 FROM "4Weeks"."heizung" WHERE "pe1_L_modulation" >10 AND  $timeFilter GROUP BY time(1m)`

### analyzing critical situations
![powerusage](/media/Oekofen-Spy_Leistungsabfluss_HK2.png "modulation level and runtime").

see here a 7.8kW stove fighting against the power ordered by HK2 and how long it takes to satisfy TPO.

## .scv support (only for JSON < V4.0)
as your oekofen generates a daily '.csv' file with additional values and values other than available in JSON interface, you may pick up these values as well.

Regarding to 'http://ip.of.your.boiler/logfiles/pelletronic/' daily files are named as 'touch_20220120.csv' or sometimes with capital T.

Every day you will get 1440 lines with approx. 60 colums. Start counting with 0. So column0 will be the date and column1 is the time these lines has been generated. 
Number of colums and sequence depends on installed options like circular pump, solar pump, # of heating circuits,..

The python script 'oekofen_fetch_csv.py' fetches the csv probably every 2 minutes, depending on your crontab entry, and picks a colum from last / actual line. This data is sent to influx database with measurement "csv". Please call 'oekofen_fetch_csv.py feedingtime 25'
if you want to have sensorname feedingtime and value from column 25.

If you want to have more values from .csv file please add another line with suitable parameter for sensorname and column to your crontab.

As JSON Versions since V4.x are not offering a local webserver anymore, there is no way to collect the .csv file anymore.

## Support
pf@nc-x.com

## Roadmap
clean up existing versions for python2/pyhton3 and old JSON from Oekofen and newer JSON from Touch V4x

## Contributing
open for contributions.

## License
MIT licence

## Project status
working fine for me monitoring 2 same heating stoves having different sofware levels and located in different buildings.
