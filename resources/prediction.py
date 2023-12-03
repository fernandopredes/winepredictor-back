import pandas as pd
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from ml_model.model import predict_wine
from sklearn.datasets import load_wine

from db import db
from models import WinePredictionModel
from schemas import WinePredictionSchema

blp = Blueprint("Predictions", __name__, description="Operações para criar e visualizar previsões de vinhos")

@blp.route('/prediction')
class PredictionList(MethodView):
    @blp.arguments(WinePredictionSchema)
    @blp.response(201, WinePredictionSchema, description="Sucesso. Retorna as informações da previsão criada.")
    def post(self, prediction_data):
        # Criar um DataFrame com os recursos dos dados de entrada
        feature_names = load_wine()['feature_names']
        input_data = pd.DataFrame([prediction_data], columns=feature_names)
        input_data = input_data.drop(columns=["od280/od315_of_diluted_wines"], errors='ignore')

        # Imprimir input_data para verificar
        print(input_data)
        print(input_data.isnull().any())

        # Alterar o nome da coluna para corresponder ao nome usado no treinamento
        input_data = input_data.rename(columns={"od280_od315_of_diluted_wines": "od280/od315_of_diluted_wines"})

        # Chama a função predict_wine do modelo para fazer a previsão com base nos recursos
        predicted_class = predict_wine(input_data)

        # Cria um novo registro de previsão com os dados de entrada e a classe prevista
        prediction_record = WinePredictionModel(**prediction_data, predicted_class=predicted_class)

        try:
            db.session.add(prediction_record)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Um erro ocorreu ao tentar criar uma previsão.")

        return prediction_record

@blp.route('/predictions')
class Predictions(MethodView):
    @blp.response(200, WinePredictionSchema(many=True), description="Sucesso. Retorna a lista de previsões.")
    def get(self):
        predictions = WinePredictionModel.query.all()
        return predictions
