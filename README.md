# 🌦️ Consulta de Clima com Python

Projeto simples em Python que consome uma **API de clima** para mostrar a temperatura atual e a condição do tempo em **Florianópolis**.

Este projeto foi criado para praticar:
- Consumo de API REST
- Uso da biblioteca `requests`
- Manipulação de dados em JSON
- Uso de variáveis de ambiente com `os.getenv`

---

## 🚀 Como funciona

O script envia uma requisição para a **WeatherAPI** e retorna:

✔ Temperatura atual em °C  
✔ Descrição do clima em português  

Exemplo de saída: A temperatura atual em Florianópolis é de 23°C e o clima está Parcialmente nublado.


---

## 🧰 Tecnologias utilizadas

- Python 3
- Biblioteca `requests`
- API externa: WeatherAPI - https://www.weatherapi.com/

---

## 🔑 Configuração da API Key

Este projeto usa variável de ambiente para proteger sua chave da API.

### 1️⃣ Crie uma conta na WeatherAPI  
https://www.weatherapi.com/

### 2️⃣ Gere sua chave de API

### 3️⃣ Configure a variável de ambiente

#### 💻 Windows (PowerShell)
```powershell
setx API_KEY "SUA_CHAVE_AQUI"
```
### 🐧 Linux / Mac
```
export API_KEY="SUA_CHAVE_AQUI"
```
---

## 📚 Objetivo do projeto

Projeto desenvolvido para fins de estudo e prática de integração com APIs externas usando Python.

