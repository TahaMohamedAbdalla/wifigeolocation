from app.main import db
from app.main.config import  GOOGLE_KEY

import requests

url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_KEY}'
def fetchwifilocationjson(data):
    try:

        """ format scan data to mach google geolcation """
        for record in data['apscan_data']:
            record['macAddress'] = record.pop('bssid')
            record['age'] = float(record.pop('timestamp'))
            record['signalStrength'] = int(record.pop('rssi'))
        data['wifiAccessPoints'] = data.pop('apscan_data')

        """ query the database """
        aps = db.db.wifiscan.find_one(data)
        """ if found return location and accuracy"""
        if  aps:
            return {  'location': aps['location'], 'accuracy': aps['accuracy'] }    
        else:
            """ if not found ask google"""
            search = {'wifiAccessPoints': [ {
                            'macAddress': data['wifiAccessPoints'][i]['macAddress'],
                            'age':  data['wifiAccessPoints'][i]['age'],
                            'channel': int(data['wifiAccessPoints'][i]['channel']),
                            'signalStrength': data['wifiAccessPoints'][i]['signalStrength'],
                             } for i in range(len(data['wifiAccessPoints']))]}
          
            result = requests.post(url, json=search).json()
            """ if found update the database and return location & accuracy """
            if 'location' in result:
                db.db.wifiscan.insert_one({'wifiAccessPoints': data['wifiAccessPoints'], 
                                            'location': result['location'],
                                            'accuracy': result['accuracy']  })
                return { 'location': result['location'], 'accuracy': result['accuracy'] }, 200
            else:
                """ if not found update the not found database and retrun not found"""
                db.db.not_found.insert_one(data)
                return {"error":  "not found" } , 404
    except Exception as e:
        return {'error': "error" }, 400

