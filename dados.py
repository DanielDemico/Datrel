import json


#norte
#nordeste
#sul

centro_oeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
    "endereco":[],
    "cep":[],
    "bairro":[],
}
sudeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
    "endereco":[],
    "cep":[],
    "bairro":[],
}
norte = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
    "endereco":[],
    "cep":[],
    "bairro":[],
}
nordeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
    "endereco":[],
    "cep":[],
    "bairro":[],
}
sul = {"nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
    "endereco":[],
    "cep":[],
    "bairro":[],}

with open('static/json/dados_mapas.json', "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for item in dados:
    if "Centro Oeste" in item["Região:"]:
        centro_oeste["nomes"].append(item["Nome Fantasia:"])
        centro_oeste["cidades"].append(item["Cidade:"])
        centro_oeste["telefones"].append(item["Telefone:"])
        centro_oeste["tags"].append(item["TAG:"])
        centro_oeste["cep"].append(item["CEP:"])
        centro_oeste["bairro"].append(item["Bairro:"])
        centro_oeste["endereco"].append(item["Endereço:"])
    elif "Nordeste" in item["Região:"]:
        nordeste["nomes"].append(item["Nome Fantasia:"])
        nordeste["cidades"].append(item["Cidade:"])
        nordeste["telefones"].append(item["Telefone:"])
        nordeste["tags"].append(item["TAG:"])
        nordeste["cep"].append(item["CEP:"])
        nordeste["bairro"].append(item["Bairro:"])
        nordeste["endereco"].append(item["Endereço:"])
    elif "Norte" in item["Região:"]:
        norte["nomes"].append(item["Nome Fantasia:"])
        norte["cidades"].append(item["Cidade:"])
        norte["telefones"].append(item["Telefone:"])
        norte["tags"].append(item["TAG:"])
        norte["cep"].append(item["CEP:"])
        norte["bairro"].append(item["Bairro:"])
        norte["endereco"].append(item["Endereço:"])
    elif "Sul" in item["Região:"]:
        sul["nomes"].append(item["Nome Fantasia:"])
        sul["cidades"].append(item["Cidade:"])
        sul["telefones"].append(item["Telefone:"])
        sul["tags"].append(item["TAG:"])
        sul["cep"].append(item["CEP:"])
        sul["bairro"].append(item["Bairro:"])
        sul["endereco"].append(item["Endereço:"])
    elif "Sudeste" in item["Região:"]:
        sudeste["nomes"].append(item["Nome Fantasia:"])
        sudeste["cidades"].append(item["Cidade:"])
        sudeste["telefones"].append(item["Telefone:"])
        sudeste["tags"].append(item["TAG:"])
        sudeste["cep"].append(item["CEP:"])
        sudeste["bairro"].append(item["Bairro:"])
        sudeste["endereco"].append(item["Endereço:"])
    else:
        print("Mas q caralho é isso")
unido = {
    "nomes":centro_oeste["nomes"] + nordeste["nomes"] + norte["nomes"] + sul["nomes"] + sudeste["nomes"],
    "cidades":centro_oeste["cidades"] + nordeste["cidades"] + norte["cidades"] + sul["cidades"] + sudeste["cidades"],
    "telefones": centro_oeste["telefones"] + nordeste["telefones"] + norte["telefones"] + sul["telefones"] + sudeste["telefones"],
    "tags":centro_oeste["tags"] + nordeste["tags"] + norte["tags"] + sul["tags"] + sudeste["tags"],
    "cep":centro_oeste["cep"] + nordeste["cep"] + norte["cep"] + sul["cep"] + sudeste["cep"],
    "bairro":centro_oeste["bairro"] + nordeste["bairro"] + norte["bairro"] + sul["bairro"] + sudeste["bairro"],
    "endereco":centro_oeste["endereco"] + nordeste["endereco"] + norte["endereco"] + sul["endereco"] + sudeste["endereco"],
}
