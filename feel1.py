from flask_restful import fields

class Feel:
    fields = {
        'name': fields.String,
        'feel': fields.Integer,
    }

    def __init__(self, name, feel):
        self.name = name
        self.feel = feel

    def json(self):
        return {'name': self.name, 'feel': self.feel}
