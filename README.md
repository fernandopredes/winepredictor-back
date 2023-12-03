# Wine Prediction API 🍷

## Descrição
Este projeto é uma API Flask que realiza previsões sobre tipos de vinhos com base em características químicas e físicas do vinho (como teor alcoólico, acidez, teor de magnésio, etc.). A API é capaz de classificar os vinhos em diferentes classes com base nesses atributos.

## Configuração Inicial 🛠️
Para configurar o ambiente virtual Python e instalar as dependências, siga os seguintes passos:

1. **Criação do Ambiente Virtual:**
   ```bash
   python -m venv venv
   ```

2. **Ativação do Ambiente Virtual:**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix ou MacOS:
     ```bash
     source venv/bin/activate
     ```

3. **Instalação das Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso 🚀

Para iniciar o servidor Flask, execute:

```bash
flask run
```

A API estará disponível em http://127.0.0.1:5000.

### Fazendo Previsões

Para fazer uma previsão, envie uma solicitação POST para `/prediction` com os seguintes dados (substitua os valores de exemplo pelos seus dados):

```json
{
  "alcohol": 13.2,
  "malic_acid": 1.78,
  "ash": 2.14,
  "alcalinity_of_ash": 11.2,
  "magnesium": 100,
  "total_phenols": 2.65,
  "flavanoids": 2.76,
  "nonflavanoid_phenols": 0.26,
  "proanthocyanins": 1.28,
  "color_intensity": 4.38,
  "hue": 1.05,
  "proline": 1050
}
```

## Executando Testes 🔍

Para executar os testes e verificar a precisão do modelo, execute:

```bash
pytest
```

## Tecnologias Utilizadas 💻

- Python
- Flask
- Pandas
- scikit-learn

---

Ajuste este README conforme necessário para incluir informações específicas do seu projeto, como novos endpoints, detalhes adicionais de configuração ou funcionalidades adicionais.
