import time
import os
class FuncoesNavegador:

    def realizaLogin(self, navegador, email, senha):
        navegador.get('http://facebook.com.br')
        elementEmail = navegador.find_element_by_id('email')
        elementEmail.clear()
        elementEmail.send_keys(email)

        password = navegador.find_element_by_id('pass')
        password.clear()
        password.send_keys(senha)

        navegador.find_element_by_id('loginbutton').click()

    def realizaPostagem(self, navegador, mensagem):
        navegador.find_element_by_name('xhpc_message').click()
        navegador.find_element_by_tag_name('body').send_keys(mensagem);
        navegador.find_element_by_class_name('_6c0o').click()

    def realizaPostagemGrupos(self, navegador, titulo, descricao, preco, imagem, tipoGrupo):

        if int(tipoGrupo) == 2:
            arrayGrupos = ["http://facebook.com.br/groups/2124656980892699"] 

        elif int(tipoGrupo) == 1:
            if os.path.exists("grupos.txt"):
                arquivoGrupos = open("grupos.txt", "r")
                arrayGrupos = arquivoGrupos.read().split("\n")
            else:
                print("Arquivo de grupos não encontrado, ele deve se chamar grupos.txt e estar na pasta raíz do programa")
                exit()
            
        for link in arrayGrupos:
            navegador.get(link)
            time.sleep(2)
            for x in range(3):
                navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').click()
            time.sleep(4)
            navegador.find_element_by_xpath('//input[@placeholder="O que você está vendendo?"]').send_keys(titulo)
            navegador.find_element_by_xpath('//input[@placeholder="Preço"]').send_keys(preco)
            navegador.find_element_by_xpath('//input[@placeholder="Adicionar localização (opcional)"]').clear()
            navegador.find_element_by_class_name('_1mwp').click()
            navegador.find_element_by_tag_name('body').send_keys(descricao.replace("/","\n"))
            if imagem != "":
                navegador.find_element_by_xpath('//input[@title="Escolha um arquivo para carregar"]').send_keys(os.path.abspath('images/'+imagem))
                time.sleep(8)
            navegador.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]').click()
            time.sleep(3)
            if int(tipoGrupo) == 2:
                checkboxes = navegador.find_elements_by_xpath('//div[@role="checkbox"]')
                for checkbox in checkboxes:
                    checkbox.click()
            navegador.find_element_by_xpath('//button[@data-testid="react-composer-post-button"]').click()
            time.sleep(8)
            print("Realizada a postagem no grupo: " + link)