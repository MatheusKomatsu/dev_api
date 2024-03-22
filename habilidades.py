from flask_restful import Resource
lista_Habilidades = ['Python', 'Java', 'Flask','PHP']
class Habilidades(Resource):
    def get(self):
        return lista_Habilidades