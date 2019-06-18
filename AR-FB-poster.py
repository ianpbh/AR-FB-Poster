from selenium import webdriver
import Constantes as dados

mensagemPost = input('Digite a mensagem do post: ')
print("Iniciando serviço web...")
navegador = webdriver.Firefox()

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

email = dados.email()
senha = dados.senha()
realizaLogin(email, senha)
realizaPostagem(mensagemPost)
navegador.quit()