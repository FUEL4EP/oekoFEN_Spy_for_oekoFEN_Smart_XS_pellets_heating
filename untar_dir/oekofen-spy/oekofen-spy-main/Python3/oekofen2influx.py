# -*- coding: utf-8 -*-
# erstellt: Peter Fürle für Python3
# holt Leistungswerte aus den JSON-Daten der Ökofen Pelletheizung
# ein Cronjob startet Skript jede 4 Minuten
# unter der MIT-Lizenz auf https://gitlab.com/p3605/oekofen-spy verfügbar

import io
import sys
import json
import urllib.request #python3
import requests
from influxdb import InfluxDBClient
from datetime import datetime
import time

#Wohnhaus Ökofen
json_quelle = "http://<MY_OEKOFEN_PELLETRONIC_IP_ADDRESS>:<MY_OEKOFEN_PELLETRONIC_JSON_PORT>/<MY_OEKOFEN_PELLETRONIC_JSON_PASSWORD>/all"

# Configure InfluxDB connection variables
host = "127.0.0.1"
port = 8086 
user = "pellematic"
password = "smart"
dbname = "oekofen" 

now = datetime.now()
print(now.strftime("%Y-%m-%d, %H:%M:%S"))

# Influx Datenbank verbinden
client = InfluxDBClient(host, port, user, password, dbname)


#line und json zusammenbauen
def eintragen(measurement,name,wert):
    if wert == "":
        wert = " "
    #statt text lieber int ausgeben für stat in grafana
    if wert == "true": 
        wert = 1
        name = name + "_mod"
    elif wert == "false":
        wert = 0
        name = name + "_mod"
    info=[{"measurement": "oekofen","tags": {"bereich": measurement},"fields": {measurement+"_"+name : wert}}]
    #print(info)
    client.write_points(info, time_precision='m')
    return

# prüfen ob Wert numerisch sein könnte, sonst String
def num(s):
    try:
        return float(s)
    except ValueError:
        return s


# durch alle Elemente des JSON-Outputs durchgehen, nachbereiten und diese an
# die Funktion zum Eintragen in die Datenbank weitergeben.
def iter_dict(data):
    for key in data:
        if isinstance(data[key], dict):
            #print("Anzahl Paare: "+str(len(d[key])))
            bereich = key
            iter_dict(data[key])
            print(str(bereich))
            for attribute, value in data[key].items():
                w = num(value)
                if "mode" in str(attribute):
                    w = int(w)
                elif "_prg" in str(attribute):
                    w = int(w)
                elif str(attribute)=="L_state":
                    w = int(w)
                elif "temp_" in str(attribute):
                    w = float(w)/10
                    #print(str(attribute)+"  temp_  "+str(w))
                elif "_temp" in str(attribute):
                    w = float(w)/10
                    #print(str(attribute)+"  _temp  "+str(w))
                elif "ambient" in str(attribute):
                    w = float(w)/10
                elif "L_tp" in str(attribute):
                    w = float(w)/10
                elif "L_day" in str(attribute):
                    w = float(w)/10
                elif "L_yesterday" in str(attribute):
                    w = float(w)/10
                elif "L_sp" in str(attribute):
                    w = float(w)/10
                elif str(attribute)=="L_flow":
                    w = float(w)/100
                elif str(attribute)=="L_pwr":
                    w = float(w)/10
                if "?" in str(w): #codierung nachbessern
                    w = str(w).replace("u?e","usse")
                    w = str(w).replace("?ber","ueber")
                    w = str(w).replace("t?t","taet")
                eintragen(str(key),str(attribute),w)


#print(len(sys.argv))

if len(sys.argv) == 2:
    # alternativ aus einem File einlesen
    # Testdaten für erste Anpassung Datensatz
    testfile = io.open(sys.argv[1], encoding='cp1252').read()
    print(sys.argv[1])
    d = json.loads(testfile)
else:
    # Leistungsdaten holen über die API
    response = urllib.request.urlopen(json_quelle)
    mydata = response.read()
    #print mydata
    d = json.loads(mydata.decode('cp1252'))


# durch alle Elemente gehen
iter_dict(d)

print("Alle Ökofen-Daten geholt und in InfluxDB -"+dbname+"- abgelegt")
#---------------- alle Werte abgefragt

