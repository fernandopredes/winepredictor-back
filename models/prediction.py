from db import db

class WinePredictionModel(db.Model):
    __tablename__ = 'wine_predictions'

    id = db.Column(db.Integer, primary_key=True)
    alcohol = db.Column(db.Float, nullable=False)
    malic_acid = db.Column(db.Float, nullable=False)
    ash = db.Column(db.Float, nullable=False)
    alcalinity_of_ash = db.Column(db.Float, nullable=False)
    magnesium = db.Column(db.Float, nullable=False)
    total_phenols = db.Column(db.Float, nullable=False)
    flavanoids = db.Column(db.Float, nullable=False)
    nonflavanoid_phenols = db.Column(db.Float, nullable=False)
    proanthocyanins = db.Column(db.Float, nullable=False)
    color_intensity = db.Column(db.Float, nullable=False)
    hue = db.Column(db.Float, nullable=False)
    proline = db.Column(db.Float, nullable=False)
    predicted_class = db.Column(db.String(50))

    def __repr__(self):
        return f'<WinePrediction {self.id}>'
