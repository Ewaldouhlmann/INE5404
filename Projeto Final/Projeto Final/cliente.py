from projetos import Projetos
import json
class Cliente:
    def __init__(self, nome, email, username, telefone,senha, dicprojetos = {}):
        self.nome = nome
        self.email = email
        self.username = username
        self.telefone = telefone
        self.senha = senha
        self.dicprojetos = dicprojetos

    def getnome(self):
        return self.nome
    
    def getemail(self):
        return self.email
    
    def getusername(self):
        return self.username
    
    def gettelefone(self):
        return self.telefone
    
    def getprojetos(self):
        return self.dicprojetos

    def getsenha(self):
        return self.senha
    
    def setnome(self, nome):
        self.nome = nome
    
    def setemail(self, email):
        self.email = email
    
    def setusername(self, username):
        self.username = username
    
    def settelefone(self, telefone):
        self.telefone = telefone
    
    def addProjeto(self, projeto):
        self.dicprojetos[projeto.titulo] = projeto
        # Lê o conteúdo atual do arquivo JSON
        with open('clientes.json', 'r') as arquivo_json:
            clientes = json.load(arquivo_json)
        
        # Verifica se o cliente existe no JSON
        if self.username in clientes:
            # Adiciona o novo projeto ao dicionário de projetos do cliente
            clientes[self.username][5][projeto.titulo] = {
                'titulo': projeto.titulo,
                'descricao': projeto.descricao,
                'background': projeto.background,
                'tarefas': []  # Supondo que 'tarefas' seja um dicionário vazio inicialmente
            }
        else:
            print(f"Cliente '{self.username}' não encontrado no JSON.")

        # Escrever o dicionário atualizado de volta no arquivo JSON
        with open('clientes.json', 'w') as arquivo_json:
            json.dump(clientes, arquivo_json)

    def removeProjeto(self, projetorecebido):
        for proj in self.dicprojetos.keys():
            if proj == projetorecebido:
                self.dicprojetos.pop(projetorecebido)
                print("Removido")
                break  # Para o loop após a remoção
        else:
            print("Projeto não encontrado")

    def getProjeto(self, projeto):
        for proj in self.dicprojetos.keys():
            if proj == projeto:
                return self.dicprojetos[projeto]
        else:
            print("Projeto não encontrado")