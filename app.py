from flask import Flask
from flask_restful import Api
from resources.feel import FeelsAPI, FeelAPI

app = Flask(__name__)
api = Api(app) #ele vai fazer o gerencimento de como tudo funciona

api.add_resource(FeelsAPI, '/feels', endpoint='feels') #colocamos o nome da classe e de onde queremos que seja chamado
api.add_resource(FeelAPI, '/feels/<name>', endpoint='feel')

if __name__ == '__main__':
    app.run(debug=True)



