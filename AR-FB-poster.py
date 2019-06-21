from selenium import webdriver
import Constantes as dados
import Funcoes
import os
import time

testerNavegador = True
while testerNavegador == True:
    opcaoNavegador = input("Deseja visualizar o navegador? (S/N) ")
    if opcaoNavegador.upper() == "S" or opcaoNavegador.upper() == "N":
        testerNavegador = False
    else:
        print("Opção inválida")


testerOpcao = True
while testerOpcao == True:
    opcao = input("Digite a opção: \n1) Postar no feed \n2) Postar em grupos\n")
    if opcao == "1":
        mensagemPost = input('Digite a mensagem do post: ')
        testerOpcao = False
    elif opcao == "2":
        tituloAnuncio = input('Digite o título do anuncio do post: ')
        descricaoAnuncio = input('Digite a descrição do anuncio do post: ')
        precoAnuncio = input('Digite o preço do anuncio do post: ')
        imagemAnuncio = input('Digite o nome da imagem que deseja fazer upload, vazio caso não deseje postar imagem (Precisa estar dentro da pasta images): ')
        testerOpcao = False
    else:
        print("Opção inválida")


print("Iniciando serviço web...")

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
    funcoes.realizaPostagemGrupos(navegador, tituloAnuncio, descricaoAnuncio, precoAnuncio, imagemAnuncio)
else:
    print("Opção inválida")
    exit()