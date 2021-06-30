from posixpath import join
from requests.models import Response
from app.main import db
from app.main.config import  GOOGLE_KEY

import os
import zipfile
import json
import requests

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_KEY}'
def fetchwifilocationjson(data):
    try:
        found = []
        not_found = []
        apscan_data = data['apscan_data']
        i = 0
        data = {  'wifiAccessPoints': [{ 'macAddress': apscan_data[i]['bssid'], 
                  'channel':  apscan_data[i]['channel'], 
                  'age':  apscan_data[i]['timestamp'] ,
                  'signalStrength': apscan_data[i]['rssi'] }
                    for i in range(len(apscan_data))] } 
        aps = db.db.wifiscan.find_one(data)
        if aps:
            return {  'location': aps['location'], 'accuracy': aps['accuracy'] }    
        else:
            result = requests.post(url, json=data).json()
            print(result)
            if 'location' in result:
                db.db.wifiscan.insert_one({'wifiAccessPoints': apscan_data, 
                                            'location': result['location'],
                                            'accuracy': result['accuracy']  })
                return { 'location': result['location'], 'accuracy': result['accuracy'] }, 200
            else:
                not_found.append( {'wifiAccessPoints': apscan_data  } )
                db.db.not_found.insert_one({'wifiAccessPoints': apscan_data })
                return {"error":  "not_found" } , 404
    except Exception as e:
        return {'error': "error" }, 400
