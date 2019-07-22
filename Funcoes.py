import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class FuncoesNavegador:

    def realizaLogin(self, navegador, email, senha):
        print(bcolors.OKGREEN + "Realizando login..." + bcolors.ENDC)
        navegador.get('http://facebook.com.br')
        elementEmail = navegador.find_element_by_id('email')
        elementEmail.clear()
        elementEmail.send_keys(email)

        password = navegador.find_element_by_id('pass')
        password.clear()
        password.send_keys(senha)

        navegador.find_element_by_id('loginbutton').click()

    def realizaPostagem(self, navegador, mensagem):
        print(bcolors.OKGREEN + "Realizando postagem..." + bcolors.ENDC)
        time.sleep(2)
        navegador.find_element_by_name('xhpc_message').click()
        time.sleep(2)
        navegador.find_element_by_tag_name('body').send_keys(mensagem)
        time.sleep(2)
        navegador.find_element_by_class_name('_6c0o').click()

    def realizaPostagemGrupos(self, navegador, titulo, descricao, preco, arrayImagens):

        if os.path.exists("grupos.txt"):
            arquivoGrupos = open("grupos.txt", "r")
            arrayGrupos = arquivoGrupos.read().split("\n")
        else:
            print("Arquivo de grupos não encontrado, ele deve se chamar grupos.txt e estar na pasta raíz do programa")
            exit()
        print(bcolors.OKGREEN + "Iniciando as postagens" + bcolors.ENDC)
        for link in arrayGrupos:
            navegador.get(link)
            time.sleep(2)
            try:
                for x in range(3):
                    navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').click()
                time.sleep(4)
                navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').send_keys(titulo)
                navegador.find_element_by_xpath('//input[@placeholder="Preço"]').send_keys(preco)
                navegador.find_element_by_xpath('//input[@placeholder="Adicionar localização (opcional)"]').clear()
                navegador.find_element_by_class_name('_1mwp').click()
                navegador.find_element_by_tag_name('body').send_keys(descricao.replace("*","\n"))
                if len(arrayImagens) > 1:
                    for imagem in arrayImagens:
                        navegador.find_element_by_xpath('//input[@title="Escolha um arquivo para carregar"]').send_keys(os.path.abspath('images/'+imagem))
                        time.sleep(2)
                    time.sleep(10)
                else:
                    time.sleep(2)
                navegador.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]').click()
                time.sleep(6)
                navegador.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]').click()
                time.sleep(6)
                print(bcolors.OKGREEN + "Realizada a postagem no grupo: " + link + bcolors.ENDC)
            except:
                print(bcolors.FAIL + "Erro ao postar no grupo " + link + bcolors.ENDC)