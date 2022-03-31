from flask import Flask
from flask_restful import Resource, Api
from resources.feel import Feels, Feel


app = Flask(__name__)
api = Api(app) 


api.add_resource(Feels, '/feels') 
api.add_resource(Feel, '/feels/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)

