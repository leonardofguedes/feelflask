from flask import Flask
from flask_restful import Resource, Api
from resources.feel import Feels, Feel


app = Flask(__name__)
api = Api(app) #ele vai fazer o gerencimento de como tudo funciona


api.add_resource(Feels, '/feels') #colocamos o nome da classe e de onde queremos que seja chamado
api.add_resource(Feel, '/feels/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)

