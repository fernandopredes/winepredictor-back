import pytest
import pandas as pd
from sklearn.metrics import accuracy_score
from ml_model.model import load_model
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/fernandopredes/winepredictor-back/master/data/wine_dataset.csv"

@pytest.fixture
def wine_dataset():
    # Carregar o dataset diretamente da URL
    dataset = pd.read_csv(url)
    dataset = dataset.drop(columns=['od280/od315_of_diluted_wines'], errors='ignore')
    X = dataset.drop(columns=['target']).values
    y = dataset['target'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    return X_train, X_test, y_train, y_test

def test_model_accuracy(wine_dataset):
    X_train, X_test, y_train, y_test = wine_dataset

    # Carregar o modelo treinado
    model = load_model()

    # Obter os nomes das colunas diretamente do CSV
    feature_names = pd.read_csv(url, nrows=0).columns.drop(['target', 'od280/od315_of_diluted_wines']).tolist()

    # Converter os dados de teste para DataFrame antes de fazer previsões
    X_test_df = pd.DataFrame(X_test, columns=feature_names)

    # Fazer previsões no conjunto de teste usando DataFrame
    predictions = model.predict(X_test_df)

    # Calcular a precisão
    accuracy = accuracy_score(y_test, predictions)

    # Verificar se a precisão atende ao threshold definido
    assert accuracy > 0.80
