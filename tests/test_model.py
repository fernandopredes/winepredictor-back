import pytest
import pandas as pd
from sklearn.metrics import accuracy_score
from ml_model.model import train_model, load_model, predict_wine
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

@pytest.fixture
def wine_dataset():
    wine = load_wine()
    dataset = pd.DataFrame(data=wine['data'], columns=wine['feature_names'])
    dataset.drop('od280/od315_of_diluted_wines', axis=1, inplace=True)
    X = dataset.values
    y = wine.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    return X_train, X_test, y_train, y_test

def test_model_accuracy(wine_dataset):
    X_train, X_test, y_train, y_test = wine_dataset

    # Treinar e salvar o modelo
    train_model()  # Chamada atualizada sem argumentos

    # Carregar o modelo treinado
    model = load_model()

    # Obter os nomes das colunas diretamente do dataset do sklearn
    feature_names = [f for f in load_wine()['feature_names'] if f != 'od280/od315_of_diluted_wines']

    # Converter os dados de teste para DataFrame antes de fazer previsões
    X_test_df = pd.DataFrame(X_test, columns=feature_names)

    # Fazer previsões no conjunto de teste usando DataFrame
    predictions = model.predict(X_test_df)

    # Calcular a precisão
    accuracy = accuracy_score(y_test, predictions)

    # Verificar se a precisão atende ao threshold definido
    assert accuracy > 0.75
