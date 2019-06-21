from selenium import webdriver
import Constantes as dados
import Funcoes
import os
import time

opcao = input("Digite a opção: \n1) Postar no feed \n2) Postar em grupos\n")
if opcao == "1":
    mensagemPost = input('Digite a mensagem do post: ')
elif opcao == "2":
    tituloAnuncio = input('Digite o título do anuncio do post: ')
    descricaoAnuncio = input('Digite a descrição do anuncio do post: ')
    precoAnuncio = input('Digite o preço do anuncio do post: ')
    imagemAnuncio = input('Digite o nome da imagem que deseja fazer upload, vazio caso não deseje postar imagem (Precisa estar dentro da pasta images): ')
else:
    print("Opção inválida")
    exit()

print("Iniciando serviço web...")
navegador = webdriver.Firefox()
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