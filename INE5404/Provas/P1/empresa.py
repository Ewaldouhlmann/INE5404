from classes import Produto, Compra, Carrinho, Pessoa, Cliente, Funcionario, Gerente
from listas import lista_clientes, lista_funcionarios, produtos
class Empresa():
    def __init__(self, estoque, lista_clientes, lista_func):
        self.estoque = estoque
        self.lista_clientes = lista_clientes
        self.lista_func = lista_func
    
    #CRUD PRODUTOS
    def criar_produto(self):
        codigo = input("Informe o codigo do produto: ")
        quantidade = int(input("Informe a quantidade: "))   
        nome = input("Informe o nome: ")
        preco = float(input("Informe o preco: "))
        novo_produt = Produto(codigo,quantidade,nome,preco)
        self.estoque.append(novo_produt)
        return 'Produto adicionado com sucesso!'

    def get_produtos(self):
        print('Estoque: ')
        try:
            for prod in self.estoque:
                nome = prod.get_nome()
                codigo = prod.get_codigo()
                quantidade = prod.get_quantidade()
                print(f'Nome: {nome}\nQuantidade: {quantidade}\nCodigo: {codigo}')
                print()
        except:
            return True


    def Selecionar_produto(self):
        while True:
            codigo = int(input("Informe o codigo do produto: "))
            for prod in self.estoque:
                if prod.codigo == codigo:
                    return prod
            print('Produto não encontrado!\nDigite novamente')
            return None
        
    def atualiza_qtprod(self, lista_compra):
        for produto in lista_compra:
            for prod in self.estoque:
                if prod.nome == produto.nome:
                    prod.quantidade -= lista_compra[produto]
                    break
        print("Estoque atualizado!")

    def atualizar_produto(self, codigo):
        while True:
            try:
                for prod in self.estoque:
                    if prod.codigo == codigo:
                        prod.set_nome()
                        prod.set_codigo()
                        prod.set_quantidade()
                        prod.set_preco()
                        return 'Produto atualizado com sucesso!'
            except:
                print('Produto não encontrado!\nDigite novamente: ')

    def excluir_produto(self):
        while True:
            try:
                codigo = input("Informe o codigo do produto: ")
                for prod in self.estoque:
                    if prod.codigo == codigo:
                        self.estoque.remove(prod)
                        return 'Produto excluido com sucesso!'
            except:
                print('Produto não encontrado!\nDigite novamente: ')

    #CRUD FUNCIONARIOS
    def criar_func(self):
            nome = input("Informe o nome completo: ")
            while len(nome) < 8:
                nome = input("Informe o nome completo: ")
            cpf = input("Informe o cpf: ")
            while len(cpf) != 11:
                cpf = input("Informe o cpf: ")
            senha = input("Informe a senha: ")
            while len(senha) < 8 or (senha.isalpha() == True) or (senha.isnumeric() == True):
                print("A senha deve possuir pelo menos 8 Caracteres, possuir vogais e numeros!!!")
                senha = input("Informe a senha: ")
            ultimo_nreg = (self.lista_func[-1].nreg)
            registro =  1 + ultimo_nreg
            conta_banc = int(input("Informe a conta bancaria(): "))
            salario = float(input("Informe o salario: R$"))
            while salario < 1320:
                salario = float(input("Salario mínimo = R$1320,00\nR$"))
            funcao = input("Gerente ou Funcionario?(G/F)")
            while funcao != 'G' and funcao != 'F':
                funcao = input("Gerente ou Funcionario?(G/F)")
            if funcao == 'G':
                novo_func = Gerente(nome,cpf,senha,registro,conta_banc,salario)
            else:
                novo_func = Funcionario(nome,cpf,senha,registro,conta_banc,salario)
                self.lista_func.append(novo_func)
            return novo_func

    def get_func(self):
        print('Lista de Funcionarios: ')
        for func in self.lista_func:
            nome = func.get_nome()
            cpf = func.get_cpf()
            salario = func.get_salario()
            conta_banc = func.get_conta_banc()
            nreg = func.get_nreg()
            print(f'Nome: {nome}, CPF: {cpf}\nSalario: {salario}, Conta Bancaria: {conta_banc}, Registro: {nreg}')
            print()

    def editar_dadosfunc(self):
        while True:
            try:
                cpf = input("Informe o cpf: ")
                senha = input("Informe a senha: ")
                for func in self.lista_func:
                    if func.cpf == cpf and func.senha == senha:
                        func.set_senha()
                        func.set_conta_banc()
                        func.set_salario()
                        return 'Dados atualizados com sucesso!'
            except:
                print('Funcionario não encontrado!\nDigite novamente: ')

    def excluir_func(self):
        while True:
            try:
                cpf = input("Informe o cpf: ")
                for func in self.lista_func:
                    if func.cpf == cpf:
                        self.lista_func.remove(func)
                        return 'Funcionario excluido com sucesso!'
            except:
                print('Funcionario não encontrado!\nDigite novamente: ')
    
    #CRUD CLIENTES
    def criar_cliente(self):
        nome = input("Informe o nome completo: ")
        while len(nome) < 8:
            nome = input("Informe o nome completo: ")
        cpf = input("Informe o cpf(Somente números): ")
        while len(cpf) != 11:
            cpf = input("Informe o cpf(Somente números): ")
        print("A senha deve possuir pelo menos 8 Caracteres, possuir vogais e numeros")
        senha = input("Informe a senha: ")
        while len(senha)< 8 or (senha.isalpha() == True) or (senha.isnumeric() == True):
            print("A senha deve possuir pelo menos 8 Caracteres, possuir vogais e numeros")
            senha = input("Informe a senha: ")        
        compras_realizadas = []
        novo_cliente = Cliente(nome,cpf,senha,compras_realizadas)
        self.lista_clientes.append(novo_cliente)
        return novo_cliente
    
    def get_clientes(self):
        print('Lista de Clientes: ')
        for cliente in self.lista_clientes:
            nome = cliente.get_nome()
            cpf = cliente.get_cpf()
            carrinho = cliente.get_carrinho
            print(f'Nome: {nome}CPF: {cpf}')
    
    def edit_clientes(self):
        while True:
            try:
                cpf = input("Informe o cpf: ")
                senha = input("Informe a senha: ")
                for cliente in self.lista_clientes:
                    if cliente.cpf == cpf and cliente.senha == senha:
                        cliente.set_senha()
                        return 'Senha atualizada com sucesso!'
            except:
                print('Cliente não encontrado!\nDigite novamente: ')
    
    def excluircliente(self, cpf):
        while True:
            try:
                for cliente in self.lista_clientes:
                    if cliente.cpf == cpf:
                        self.lista_clientes.remove(cliente)
                        return 'Cliente excluido com sucesso!'
            except:
                print('Cliente não encontrado!\nDigite novamente: ')
    
    def logar_func(self, cpf,senha):
        for func in self.lista_func:
            if func.cpf == cpf and func.senha == senha:
                print(f"Bem vindo(a) " + func.nome + "!")
                return func
        return None
    
    def logar_cliente(self, cpf, senha):
        for cliente in self.lista_clientes:
            if cliente.cpf == cpf and cliente.senha == senha:
                print(f"Bem vindo(a) " + cliente.nome + "!")
                return cliente
        return None


    
e1 = Empresa([],lista_clientes,lista_funcionarios)
