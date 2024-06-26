import requests
import datetime

#VARIÁVEIS
peso_da_encomenda_input_before = str(input("Digite o peso da encomenda em KG: "))
peso_da_encomenda_input = peso_da_encomenda_input_before.replace(",", ".")
peso_da_encomenda = float(peso_da_encomenda_input)

CPF_do_cliente = input("Digite o CPF: ")
CEP_de_destino = input("Digite o CEP (8 dígitos no máximo): ") 
horario_agora = datetime.datetime.now()

#REQUISIÇÃO E DICIONÁRIO
link = f"https://viacep.com.br/ws/{CEP_de_destino}/json/"

requisicao = requests.get(link)
data = requisicao.json() 

#Verifica se o CEP existe
while 'erro' in data:
    CEP_de_destino = input("Digite o CEP (8 dígitos no máximo): ")
    link = f"https://viacep.com.br/ws/{CEP_de_destino}/json/"
    requisicao = requests.get(link)
    data = requisicao.json() 


dicionario_requisicao = requisicao.json()
uf = dicionario_requisicao['uf']

dicionario_requisicao = requisicao.json()
cep = dicionario_requisicao['cep']



#Matematica se for do pr
if uf == "PR":
    print("PARANAENSE ")
    if peso_da_encomenda > 0 and peso_da_encomenda <= 1:
        print("O valor do seu frete é R$10,00")
        valor = "R$10,00"

    elif peso_da_encomenda >= 1.1 and peso_da_encomenda <= 5:
        print("O valor do seu frete é R$15,00")
        valor = "R$15,00"

    elif peso_da_encomenda >= 5.1 and peso_da_encomenda <= 10:
        print("O valor do seu frete é R$22,50")
        valor = "R$22,50"

    elif peso_da_encomenda > 10:
        print("O valor do seu frete é R$37,50")
        valor = "R$37,50"

#Se o CEP NAO for do pr
if uf != "PR":
    print("NAO E DO PARANA ")
    if peso_da_encomenda > 0 and peso_da_encomenda <= 1:
        print("O valor do seu frete é R$12,50")
        valor = "R$12,50"

    elif peso_da_encomenda >= 1.1 and peso_da_encomenda <= 5:
        print("O valor do seu frete é R$19,90")
        valor = "R$19,90"

    elif peso_da_encomenda >= 5.1 and peso_da_encomenda <= 10:
        print("O valor do seu frete é R$29,90")
        valor = "R$29,90"

    elif peso_da_encomenda > 10:
        print("O valor do seu frete é R$49,90")
        valor = "R$49,90"


#Escrevendo no arquivo
arquivo = open("REGISTRO_DE_CLIENTES.txt", "a")
arquivo.write(f"{peso_da_encomenda}Kg | {CPF_do_cliente} | {cep} | {valor} {horario_agora.day}/{horario_agora.month}/{horario_agora.year} {horario_agora.hour}:{horario_agora.minute}:{horario_agora.second}\n")
arquivo.write("-------------------------------------------------------------------------------\n")
arquivo.close