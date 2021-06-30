from flask_restplus import Api
from flask import Blueprint



from .main.controller.wifilocation_controller import api as wifi_ns



blueprint = Blueprint('wifi',__name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )


api.add_namespace(wifi_ns, path='/wifi')
