from flask_restful import Resource, reqparse
from models.feel import FeelModel


subjects = [
    {'name' : 'trabalho', 'feel': 50},
    {'name' : 'flamengo', 'feel': 55}
]


class Feels(Resource): #recurso da api,todo recurso tem funç. get, post, delete
    def get(self):
        return {'assunto': subjects} #o flaskrestful converterá isso para json, se tudo ocorrer bem


class Feel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('feel')


    def find_feel(name):
        for feel_n in subjects:
            if feel_n['name'] == name:
                return feel_n
        return None


    def get(self, name):
        feel = Feel.find_feel(name)
        if feel:
            return feel
        return {'message': 'Feel not found'}, 404 #statuscode http not found


    def post(self,name):
        dados = Feel.atributos.parse_args() #os dados serão a chave e valor do argumento passado
        feelin = FeelModel(name, **dados)
        novo_feel = feelin.json()
        subjects.append(novo_feel)
        return novo_feel, 200 #codigo de sucesso


    def put(self,name):
        dados = Feel.atributos.parse_args()  # os dados serão a chave e valor do argumento passado
        feelin = FeelModel(name, **dados)
        novo_feel = feelin.json()
        feel = Feel.find_feel(name)
        if feel:
            feel.update(novo_feel) #quando existe, devolve dados
            return novo_feel, 200 #ok
        subjects.append(novo_feel)
        return novo_feel, 201 #criado


    def delete(self,name):
        global subjects
        subjects = [ feel for feel in subjects if feel['name'] != name]
        return { 'message': 'Subject deleted.'}