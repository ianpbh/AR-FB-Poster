from selenium import webdriver
import Constantes as dados
import Funcoes
import os
import time
import json

bcolors = Funcoes.bcolors
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
        testerOpcao = False
    else:
        print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)

arrayImagens = descricaoPost['imagem'].replace(" ", "").split(",")
if len(arrayImagens) >= 1:
    for imagem in arrayImagens:
        if os.path.exists("images/" + imagem) == False:
            print(bcolors.FAIL + "Imagem '" + imagem + "' não encontrada, favor verificar" + bcolors.ENDC)
            exit()


print(bcolors.OKGREEN + "Iniciando serviço web..." + bcolors.ENDC)

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
if opcaoNavegador.upper() == "S":
    navegador = webdriver.Firefox(firefox_profile=profile)
else:
    opcoes = webdriver.FirefoxOptions()
    opcoes.add_argument('-headless')
    navegador = webdriver.Firefox(options=opcoes,firefox_profile=profile)

funcoes = Funcoes.FuncoesNavegador()
email = dados.email()
senha = dados.senha()
funcoes.realizaLogin(navegador, email, senha)
time.sleep(2)

if opcao == "1":
    funcoes.realizaPostagem(navegador, mensagemPost)
elif opcao == "2":
    funcoes.realizaPostagemGrupos(navegador, descricaoPost["titulo"], descricaoPost["descricao"], descricaoPost["preco"], arrayImagens)
else:
    print(bcolors.FAIL + "Opção inválida" + bcolors.ENDC)
    exit()