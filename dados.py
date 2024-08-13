import json


#norte
#nordeste
#sul

centro_oeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
}
sudeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
}
norte = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
}
nordeste = {
    "nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],
}
sul = {"nomes":[],
    "cidades":[],
    "telefones":[],
    "tags":[],}

with open('static/json/dados_mapas.json', "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for item in dados:
    if "Centro Oeste" in item["Região:"]:
        centro_oeste["nomes"].append(item["Nome Fantasia:"])
        centro_oeste["cidades"].append(item["Cidade:"])
        centro_oeste["telefones"].append(item["Telefone:"])
        centro_oeste["tags"].append(item["TAG:"])
    elif "Nordeste" in item["Região:"]:
        nordeste["nomes"].append(item["Nome Fantasia:"])
        nordeste["cidades"].append(item["Cidade:"])
        nordeste["telefones"].append(item["Telefone:"])
        nordeste["tags"].append(item["TAG:"])
    elif "Norte" in item["Região:"]:
        norte["nomes"].append(item["Nome Fantasia:"])
        norte["cidades"].append(item["Cidade:"])
        norte["telefones"].append(item["Telefone:"])
        norte["tags"].append(item["TAG:"])
    elif "Sul" in item["Região:"]:
        sul["nomes"].append(item["Nome Fantasia:"])
        sul["cidades"].append(item["Cidade:"])
        sul["telefones"].append(item["Telefone:"])
        sul["tags"].append(item["TAG:"])
    elif "Sudeste" in item["Região:"]:
        sudeste["nomes"].append(item["Nome Fantasia:"])
        sudeste["cidades"].append(item["Cidade:"])
        sudeste["telefones"].append(item["Telefone:"])
        sudeste["tags"].append(item["TAG:"])
    else:
        print("Mas q caralho é isso")
unido = {
    "nomes":centro_oeste["nomes"] + nordeste["nomes"] + norte["nomes"] + sul["nomes"] + sudeste["nomes"],
    "cidades":centro_oeste["cidades"] + nordeste["cidades"] + norte["cidades"] + sul["cidades"] + sudeste["cidades"],
    "telefones": centro_oeste["telefones"] + nordeste["telefones"] + norte["telefones"] + sul["telefones"] + sudeste["telefones"],
    "tags":centro_oeste["tags"] + nordeste["tags"] + norte["tags"] + sul["tags"] + sudeste["tags"],
}

for i in unido["nomes"]:
    print(i)
