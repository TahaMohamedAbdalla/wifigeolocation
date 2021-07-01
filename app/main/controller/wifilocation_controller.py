
from flask_restplus import Resource 
from flask import request
from marshmallow import ValidationError
from app.main.util.validator import ScanDataValidator 


from app.main.util.dto import Wifilocator
from app.main.service.wifilocation_json import fetchwifilocationjson


api = Wifilocator.api
_wifilocator = Wifilocator.wifilocator

@api.route('/wifilocationjson')
class Wifilocation(Resource):
    @api.doc(' get AP conrdinates from JSON object')
    def post(self):            
        try:
            data  = ScanDataValidator().load(request.json)
            return  fetchwifilocationjson(data)
        except  ValidationError as e:
            return { "error": str(e)}
         
           
              
         
 
