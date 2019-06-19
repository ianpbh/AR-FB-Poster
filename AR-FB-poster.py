from selenium import webdriver
import Constantes as dados

def realizaLogin(email, senha):
    navegador.get('http://facebook.com.br')
    elementEmail = navegador.find_element_by_id('email')
    elementEmail.clear()
    elementEmail.send_keys(email)

    password = navegador.find_element_by_id('pass')
    password.clear()
    password.send_keys(senha)

    navegador.find_element_by_id('loginbutton').click()

def realizaPostagem(mensagem):
    navegador.find_element_by_name('xhpc_message').click()
    navegador.find_element_by_tag_name('body').send_keys(mensagem);
    navegador.find_element_by_class_name('_6c0o').click()

def realizaPostagemGrupos(titulo, descricao, preco):
    navegador.get('http://facebook.com.br/groups/2124656980892699')
    for x in range(3):
        navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').click()
    
    navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').send_keys(titulo)
    navegador.find_element_by_xpath('//input[@placeholder="Preço"]').send_keys(preco)
    navegador.find_element_by_xpath('//input[@placeholder="Adicionar localização (opcional)"]').clear()
    navegador.find_element_by_class_name('_1mwp').click()
    navegador.find_element_by_tag_name('body').send_keys(descricao);


opcao = input("Digite a opção: \n1) Postar no feed \n2) Postar em grupos\n")

if opcao == "1":
    mensagemPost = input('Digite a mensagem do post: ')
elif opcao == "2":
    tituloAnuncio = input('Digite o título do anuncio do post: ')
    descricaoAnuncio = input('Digite a descrição do anuncio do post: ')
    precoAnuncio = input('Digite o preço do anuncio do post: ')
else:
    print("Opção inválida")
    exit()

print("Iniciando serviço web...")
navegador = webdriver.Firefox()

email = dados.email()
senha = dados.senha()
realizaLogin(email, senha)

if opcao == "1":
    realizaPostagem(mensagemPost)
elif opcao == "2":
    realizaPostagemGrupos(tituloAnuncio, descricaoAnuncio, precoAnuncio)
else:
    print("Opção inválida")
    exit()