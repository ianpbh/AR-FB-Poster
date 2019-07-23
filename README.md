# AR-FB-Poster

Como utilizar:
  
      
  1) Faça a instalação do selenium através do pip
  2) Crie um arquivo chamado 'Constantes.py' (sem aspas) na pasta raiz do projeto e adicione o seguinte conteúdo
    
    def email():
      return 'seuEmailTeste@email.com'
    def senha():
      return 'suaSenhaTeste'
      
  3) Crie um arquivo chamado "grupos.txt", nele insira os links dos grupos para postar, links devem ser separados por quebras de     linhas. Ex.:
  
    https://www.facebook.com/groups/123/
    https://www.facebook.com/groups/1234/
    
  4) Crie um arquivo "post.json" com o seguinte conteúdo, ele possuirá as informações para realizar a postagem.
  
    {
      "titulo":"Titulo Teste", 
      "descricao":"Descrição Teste * Descrição teste", 
      "preco":"31990",
      "imagem":"imagem1,imagem2,imagem3"
      }
  OBS.: Os asteriscos(*) na descrição significam quebra de linha, caso queira quebrar a linha duas vezes, use dois asteriscos, e assim por diante. Mais de uma imagem pode ser postada junto com um anuncio, separe as imagens por vírgula
  
  3) Rode o arquivo AR-FB-poster.py
  
O script foi feito manipulando elementos da página do Facebook, podendo váriar de usuário para usuário, comprometendo a      execução do programa

Vídeo demonstrativo de postagens no feed: https://www.youtube.com/watch?v=3Jt9OdR2JT8

Vídeo demonstrativo de postagens em grupos de venda: https://www.youtube.com/watch?v=-8LF5YmzMRM
