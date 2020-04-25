import urllib3
from bs4 import BeautifulSoup

#Desabilitando warnings de certificado de conexao
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Criando variavel pra receber a classe PoolManager
#PoolManager eh usada para fazer requisicoes http
#para pegar conteudos de paginas
http = urllib3.PoolManager()

#Variavel pra fazer requisicoes em uma pagina
pagina = http.request('GET', 'https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o')

#Printando o status da requisicao
#200 significa que a conexao foi bem sucedida
#404 significa que a pagina nao foi encontrada
print(pagina.status) 

#Printando dados da pagina (codigo fonte)
print(pagina.data)

#Printando os primeiros 50 caracteres de dados da pagina
print(pagina.data[0:50])

#Pegando os dados da pagina formatados
sopa = BeautifulSoup(pagina.data, "html.parser")

#Printando dados da pagina (codigo fonte) agora formatados
print(sopa)

#Criando um arquivo txt
f = open("dados.txt", "w+")
#Convertendo os dados da pagina para uma string
dados = str(sopa)
#Escrevendo a string no arquivo criado
f.write(dados)
f.close()

#Printando apenas o titulo da pagina
print(sopa.title)

#Printando o titulo da pagina em formato string
print(sopa.title.string)

#Criando uma variavel pra guardar todos os links da pagina
#O 'a' representa a tag html <a>, que se refere aos links
links = sopa.find_all('a')

#Printando a quantidade de links encontrados
print(len(links))

#Printando todos os links encontrados
for link in links:
    print(link.get('href'))
    #Printando conteudo dos links
    print(link.contents)