# -*- coding: utf-8 -*-
# erstellt: Peter Fürle Python3.9
# legt Datenbank und User local auf Raspberry Pi für Ökofen-Spy an.
# zuvor muss mit "pip install influxdb" influx installiert werden.
# nur einmal starten!

from influxdb import InfluxDBClient

# Configure InfluxDB connection variables
host = "127.0.0.1" 
port = 8086 
user = "pellematic"
password = "smart"
dbname = "oekofen"  # live hier oekofen eintragen ! 

def check_dbexist():
    ok=(client.get_list_database()[i]['name']==dbname)
    return ok


# configure Influx database for oekofen-spy 
# connect to influx
client = InfluxDBClient(host, port)
#client.drop würde die Datenbank entfernen    
#client.drop_database(dbname)
print("vorhandene Datenbanken bisher:",len(client.get_list_database()))
i=0
schonda = False
while i < len(client.get_list_database()):
    print("gefunden: ",client.get_list_database()[i]['name'])
    if check_dbexist():
        print(dbname,"gibt es schon:",check_dbexist())
        schonda = True
    i=i+1

if not schonda:
    # create database
    client.create_database(dbname)
    # use this database
    client.switch_database(dbname)
    # create a user for this database
    # client.create_user(user, password, admin=False)
    # configure user rights
    client.grant_privilege('all', dbname, user)
    # create a retention policy to compress data older than 6weeks
    client.create_retention_policy('6weeks', '6w', 1, default=True)
    # use newly created user
    client.switch_user(user, password)
    print("Version Influx:",client.ping())
    print("--> Datenbank ",dbname," angelegt")
    print("--> User ",user, "mit Passwort ",password," für Oekofen-Spy eingerichtet")
    print("--> Retention policy '6weeks' angelegt")
    #client.write_points(json_body)
else :
    print("Sorry, die Datenbank ",dbname," existiert schon!")


