import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os

def train_model():
    # URL do data set
    url = "https://raw.githubusercontent.com/fernandopredes/winepredictor-back/master/data/wine_dataset.csv"

    # Carregar o dataset diretamente da URL
    dataset = pd.read_csv(url)

    # Remover a coluna 'od280/od315_of_diluted_wines'
    dataset = dataset.drop(columns=['od280/od315_of_diluted_wines'], errors='ignore')

    X = dataset.drop(columns=['target'])  # Características dos vinhos.
    y = dataset['target']  # Classes dos vinhos.


    # Dividir os dados em conjuntos de treino e teste.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

    # Definir os parâmetros para otimização do modelo KNN.
    param_grid = {
        'n_neighbors': range(1, 31),
        'metric': ['euclidean', 'manhattan', 'minkowski'],
        'weights': ['uniform', 'distance']
    }

    # Usar GridSearchCV para encontrar os melhores hiperparâmetros para o modelo KNN.
    grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    # Selecionar o modelo com os melhores hiperparâmetros.
    best_model = grid_search.best_estimator_

    # Treinar o melhor modelo com todo o conjunto de dados.
    best_model.fit(X, y)

    # Salvar o modelo treinado para uso posterior.
    model_file_path = os.path.join(os.getcwd(), 'best_wine_model.pkl')
    joblib.dump(best_model, model_file_path)

def load_model():
    # Carregar o modelo treinado do arquivo.
    model_file_path = os.path.join(os.getcwd(), 'best_wine_model.pkl')
    return joblib.load(model_file_path)

def predict_wine(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    wine = load_wine()
    predicted_class_index = int(prediction[0])
    predicted_class = wine['target_names'][predicted_class_index]
    return predicted_class

if __name__ == '__main__':
    train_model()
    test_features = pd.DataFrame([[13.2, 1.78, 2.14, 11.2, 100, 2.65, 2.76, 0.26, 1.28, 4.38, 1.05, 3.40, 1050]],
                                 columns=load_wine()['feature_names'])
