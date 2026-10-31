import requests

cep = input ("digite seu CEP")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)

resposta = dados.json()

print = (f"voce mora em {resposta["localidade"]}, no bairro {resposta["bairro"]}")