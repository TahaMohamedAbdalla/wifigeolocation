
from flask_restplus import Resource 
from flask import request


from app.main.util.dto import Wifilocator
from app.main.service.wifilocation_file import fetchwifilocationfile
from app.main.service.wifilocation_json import fetchwifilocationjson



api = Wifilocator.api
_wifilocator = Wifilocator.wifilocator



@api.route('/wifilocationjson')
class Wifilocation(Resource):
    @api.doc(' get AP conrdinates from JSON object')
    def post(self):  
        data = request.json
        return  fetchwifilocationjson(data)       
         
 


@api.route('/wifilocationfromfile')
class WifiLocationFile(Resource):
    @api.doc(' get AP conrdinates')
    def post(self):  
        if 'file' not in request.files:
            return {'message' : 'No file uploaded'}
             
        file = request.files['file'] 
        return fetchwifilocationfile(file)          
         
