from cliente import Cliente
import json
from telass import TelaInicio, TelaCadastro, TelaProjetos

class Sistema:
    def __init__(self, dicclientes,telas):
        self.dicclientes = dicclientes
        self.telas = telas
    
    
    def iniciarsistema(self):
        import json
        j = open('clientes.json', 'r')
        clientes = json.load(j)
        j.close()
        for usuario, dados in clientes.items():
            nome, email, username, telefone, senha, dicprojetos = dados
            self.dicclientes[username] = Cliente(nome, email, username, telefone,senha, {})
        return self.dicclientes

    def iniciarTelas(self):
        self.telas.append(TelaInicio)
        self.telas.append(TelaCadastro)
        return self.telas
    
    def cadastroCliente(self, nome, email, username, telefone, senha):
        catual = Cliente(nome, email, username, telefone, senha)
        import json
        # Verificar se o arquivo JSON existe
        try:
            with open('clientes.json', 'r') as arquivo_json:
                # Ler o conteúdo atual do arquivo
                clientes = json.load(arquivo_json)
        except FileNotFoundError:
            # Se o arquivo não existir, criar um dicionário vazio
            clientes = {}

        # Adicionar o novo cliente ao dicionário
        clientes[username] = [nome, email, username, telefone, senha, {}]

        # Escrever o dicionário atualizado de volta no arquivo JSON
        with open('clientes.json', 'w') as arquivo_json:
            json.dump(clientes, arquivo_json)
        print("Usuario cadastrado")
        return catual
    
    def getUsuario(self, username, senha):
        import json
        # Usar 'with' para garantir que o arquivo seja fechado corretamente
        with open('clientes.json', 'r') as arquivo_json:
            clientes = json.load(arquivo_json)

        # Consulta por username 
        if username in clientes:
            if senha == clientes[username][4]:
                nome = clientes[username][0]
                email = clientes[username][1]
                username = clientes[username][2]
                telefone = clientes[username][3]
                senha = clientes[username][4]
                dicprojetos = clientes[username][5]
                cliente_atual = Cliente(nome, email, senha, username, telefone, dicprojetos)
                return cliente_atual
            else:
                return False
        else:
            return False
    
    def verificaNewUser(self,dic_novouser):
        import re
        nome = dic_novouser['nome']
        email = dic_novouser['email']
        username = dic_novouser['username']
        telefone = dic_novouser['telefone']
        telefone = re.sub(r'\s+|-|\(|\)', '', telefone)
        senha = dic_novouser['senha']
        confirmar_senha = dic_novouser['confirmar_senha']
        numeros = []
        if len(nome) < 4 or len(nome) > 20:
            return 'Nome deve ter entre 4 e 20 caracteres'
        elif len(email) < 4 or len(email) > 20:
            return 'Email deve ter entre 4 e 20 caracteres'
        elif telefone.isnumeric() == False:
            return 'Telefone deve conter apenas números'
        elif len(telefone) < 10 or len(telefone) > 11:
            return 'Telefone deve ter entre 10 e 11 caracteres'
        elif senha != confirmar_senha:
            return 'Senhas não coincidem'
        elif len(senha) < 4 or len(senha) > 20 or senha.isalpha() or not any(char.isdigit() for char in senha):
            return 'A senha deve ter entre 4 e 20 caracteres, possuir letras e pelo menos um número'
        #verificar se existe user no json
        import json
        # Usar 'with' para garantir que o arquivo seja fechado corretamente
        with open('clientes.json', 'r') as arquivo_json:
            clientes = json.load(arquivo_json)

        # Consulta por username 
        if username in clientes:
            return 'Username já cadastrado'
        else:
            return True
                

    def consultaClientes(self):
        import json
        j = open('clientes.json', 'r')
        clientes = json.load(j)
        j.close()
        for usuario, dados in clientes.items():
            nome, email, username, telefone, senha, dicprojetos = dados
            print(nome, email, username, telefone, senha, dicprojetos)

    def criarProjeto(self):
        pass

