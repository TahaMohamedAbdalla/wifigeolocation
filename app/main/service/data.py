from posixpath import join
from requests.models import Response
from app.main import db
from app.main.config import  GOOGLE_KEY

import os
import zipfile
import json
import requests

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_KEY}'
def fetchwifilocationfile(file):
    try:
        found = []
        not_found = []
        path = os.getcwd()
        zip_folder = "scan.zip"
        scandatapath = os.path.join(path,zip_folder)
        file.save(scandatapath)  
        # format the data to mtach wifi object in google gelocation API
        scandata = formatScanData(zip_folder) 
        i = 0 
        for i in range(5):# range(len(scandata)):
            apscan_data = scandata[i]['wifiAccessPoints']
            aps = db.db.wifiscan.find_one({'wifiAccessPoints': apscan_data})
            # check is the object stored in the database
            if aps:
                aps = { 'apscan_data': aps['wifiAccessPoints'], 'location': aps['location'], 'accuracy': aps['accuracy'] }
                found.append(aps)
            else:
                # send request if the object not found in the database
                result = requests.post(url, json={'wifiAccessPoints': apscan_data}).json()
                if 'location' in result:
                    db.db.wifiscan.insert_one({'wifiAccessPoints': apscan_data, 
                                                'location': result['location'],
                                                'accuracy': result['accuracy']  })
                    found.append( {'wifiAccessPoints': apscan_data, 
                                                'location': result['location'],
                                                'accuracy': result['accuracy']  })
                else:
                    not_found.append( {'wifiAccessPoints': apscan_data  } )
                    db.db.not_found.insert_one({'wifiAccessPoints': apscan_data })
        return {"found": found, "not_found" : not_found} , 404
    except Exception as e:
        return {'error': "error" }, 400

def formatScanData(zip_folder):
    formateddata = []
    i = 0
    j = 0  
    with zipfile.ZipFile(zip_folder) as apdata:
            with apdata.open('scan.json') as file: 
                rawdata = json.load(file)
   
    return  [{  'wifiAccessPoints': [
                        { 'macAddress': rawdata[i]['apscan_data'][j]['bssid'], 
                           'channel': rawdata[i]['apscan_data'][j]['channel'], 
                           'age':   rawdata[i]['apscan_data'][j]['timestamp'] , 
                           'signalStrength': rawdata[i]['apscan_data'][j]['rssi'] 
                        }  for j in range(len(rawdata[i]['apscan_data'])) ]} for i in range(len(rawdata)) ]

     
