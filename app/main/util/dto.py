from flask_restplus import Namespace

class Wifilocator:
    api = Namespace('Wifilocator', description='WIFI gelocation')
    wifilocator = api.model('wifilocator', {
        
    })

