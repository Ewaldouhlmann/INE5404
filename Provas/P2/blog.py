import requests
from noticias import Noticias
import json
import datetime
from clientes import Cliente, Jornalista, User
class Blog:
    def __init__(self, noticias, clientes, jornalistas):
        self.noticias = noticias
        self.clientes = clientes
        self.jornalistas = jornalistas

    def verificaLogin(self, user,senha):
        for cliente in self.clientes:
            if cliente.user == user and cliente.senha == senha:
                print("Cliente")
                return cliente
        for jornalista in self.jornalistas:
            if jornalista.user == user and jornalista.senha == senha:
                print("Jornalista")
                return jornalista
        print("Nenhuma")
        return None

    def iniciarApi(self):
        noticias = {}
        sports = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=9764e51ae1f2460b87cc0f3760d3b4b9').json()
        for art in sports['articles']:
            noticias[art['title']] = ['Esportes',art['description'], art['publishedAt'], art['url']]
            
        economy = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=9764e51ae1f2460b87cc0f3760d3b4b9').json()
        for art in economy['articles']:
            noticias[art['title']] = ['Economia',art['description'], art['publishedAt'], art['url']]
            
        politics = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey=9764e51ae1f2460b87cc0f3760d3b4b9').json()
        for art in politics['articles']:
            noticias[art['title']] = ['Política',art['description'], art['publishedAt'], art['url']]
            
        with open('noticias.json', 'w') as f:
            json.dump(noticias, f)
    
    def addNoticias(self):
        with open('noticias.json', 'r') as f:
            noticias = json.load(f)
        for key, valor in noticias.items():
            try:
                titulo = key
                tipo = valor[0]
                descricao = valor[1]
                data = valor[2]
                url = valor[3]
                n = Noticias(tipo, titulo, descricao, data, url)
                self.noticias.append(n)
            except:
                print()
        return noticias
    
    def consultarNoticias(self, tipo, datainicio, datafim):
        noticias_list = []
        for noticia in self.noticias:
            if noticia.getArea() == tipo:
                data = noticia.getData()
                try:
                    if data <= datafim and data >= datainicio:
                        noticias_list.append(noticia)
                except:
                    pass
        return noticias_list

    def cadastroClient(self,nome,senha):
        self.clientes.append(Cliente(nome,senha))
        print("Cliente cadastrado com sucesso!")

    def novaNoticia(self, titulo, descricao, link, area):
        from datetime import datetime
        dia_atual = datetime.now()  # pega a data atual
        data = dia_atual.strftime('%d/%m/%Y')

        self.noticias.append(Noticias(area, titulo, descricao,data, link))
        print("Notícia cadastrada com sucesso!")

    
