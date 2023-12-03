from marshmallow import Schema, fields

class WinePredictionSchema(Schema):
    """
    Define a estrutura dos dados para uma previsão de vinho.
    """
    id = fields.Integer(description="ID da previsão", dump_only=True)
    alcohol = fields.Float(required=True, description="Teor de álcool")
    malic_acid = fields.Float(required=True, description="Ácido málico")
    ash = fields.Float(required=True, description="Cinza")
    alcalinity_of_ash = fields.Float(required=True, description="Alcalinidade da cinza")
    magnesium = fields.Float(required=True, description="Magnésio")
    total_phenols = fields.Float(required=True, description="Fenóis totais")
    flavanoids = fields.Float(required=True, description="Flavonoides")
    nonflavanoid_phenols = fields.Float(required=True, description="Fenóis não flavonoides")
    proanthocyanins = fields.Float(required=True, description="Proantocianidinas")
    color_intensity = fields.Float(required=True, description="Intensidade da cor")
    hue = fields.Float(required=True, description="Matiz")
    proline = fields.Float(required=True, description="Prolina")
    predicted_class = fields.String(description="Classe prevista para o vinho", dump_only=True)

    class Meta:
        description = "Define a estrutura de dados para uma previsão de vinho."
