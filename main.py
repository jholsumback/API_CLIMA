import requests
import pprint
import os

chave = os.getenv("API_KEY")

api_key = chave

url = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": api_key,
    "q": "Florianópolis",
    "lang": "pt"
}

resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]
    print(f"A temperatura atual em Florianópolis é de {temp}°C e o clima está {descricao}.")

