from flask import abort
from flask_restful import Resource, reqparse, marshal
from models.feel1 import Feel

feels = [
    Feel(name='trabalho', feel=50),
    Feel(name='flamengo', feel=55),
]


class FeelsAPI(Resource):
    """
    FeelsAPI permite acessar a coleção de objetos do tipo Feel.

    métodos:
    - GET: retorna uma lista com todos os objetos salvos
    - POST: cria/adiciona um novo objeto na coleção
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            type=str,
            required=True,
            help='No Feel name provided',
            location='json',
        )
        self.reqparse.add_argument(
            'feel',
            type=int,
            default=0,
            location='json',
        )
        super().__init__()

    def get(self):
        return {'feels': [marshal(f, Feel.fields) for f in
                          feels]}  # o flaskrestful converterá isso para json, se tudo ocorrer bem

    def post(self):
        args = self.reqparse.parse_args()
        feelin = Feel(**args)
        feels.append(feelin)
        return marshal(feelin, Feel.fields), 201  # sucesso em post (created)


class FeelAPI(Resource):
    """
    FeelAPI permite acessar um objeto especifico da coleção de Feels

    métodos:
    - GET: retorna um objeto pelo nome
    - PUT: atualiza um objeto pelo nome
    - DELETE: remove um objeto pelo nome
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            type=str,
            required=True,
            help='No Feel name provided',
            location='json',
        )
        self.reqparse.add_argument(
            'feel',
            type=int,
            default=0,
            location='json',
        )
        super().__init__()

    def get(self, name):
        feel = self._find_feel(name)
        if feel:
            return marshal(feel, Feel.fields)
        return {'message': 'Feel not found'}, 404  # statuscode http not found

    def put(self, name):
        feel = self._find_feel(name)
        if not feel:
            abort(404)

        args = self.reqparse.parse_args()
        feel.update(args['feel'])
        return marshal(feel, Feel.fields)

    def delete(self, name):
        feel = self._find_feel(name)
        if not feel:
            abort(404)

        feels.remove(feel)
        return {'message': 'Subject deleted.'}

    def _find_feel(self, name):
        for feel in feels:
            if feel.name == name:
                return feel
        return None
