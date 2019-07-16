from selenium import webdriver
import Constantes as dados
import Funcoes
import os
import time
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

jsonPost = open("post.json", "r")
descricaoPost = json.loads(jsonPost.read())

testerNavegador = True
while testerNavegador == True:
    opcaoNavegador = input("Deseja visualizar o navegador? (S/N) ")
    if opcaoNavegador.upper() == "S" or opcaoNavegador.upper() == "N":
        testerNavegador = False
    else:
        print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)


testerOpcao = True
while testerOpcao == True:
    opcao = input("Digite a opção: \n1) Postar no feed \n2) Postar em grupos\n")
    if opcao == "1":
        mensagemPost = input('Digite a mensagem do post: ')
        testerOpcao = False
    elif opcao == "2":
        testerImagem = True
        while testerImagem == True:
            imagemAnuncio = input('Digite o nome da imagem que deseja fazer upload, vazio caso não deseje postar imagem (Precisa estar dentro da pasta images): ')
            if os.path.exists("images/" + imagemAnuncio):
                testerImagem = False
            else:
                print(bcolors.FAIL + "A imagem não foi encontrada, favor digitar o nome novamente" + bcolors.ENDC)
        testerOpcao = False
    else:
        print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)



print(bcolors.OKGREEN + "Iniciando serviço web..." + bcolors.ENDC)

if opcaoNavegador.upper() == "S":
    navegador = webdriver.Firefox()
else:
    opcoes = webdriver.FirefoxOptions()
    opcoes.add_argument('-headless')
    navegador = webdriver.Firefox(options=opcoes)

funcoes = Funcoes.FuncoesNavegador()
email = dados.email()
senha = dados.senha()
funcoes.realizaLogin(navegador, email, senha)
time.sleep(2)

if opcao == "1":
    funcoes.realizaPostagem(navegador, mensagemPost)
elif opcao == "2":
    funcoes.realizaPostagemGrupos(navegador, descricaoPost["titulo"], descricaoPost["descricao"], descricaoPost["preco"], imagemAnuncio)
else:
    print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)
    exit()