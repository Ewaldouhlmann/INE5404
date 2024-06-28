class Produto():
    def __init__(self,codigo,quantidade, nome, preco):
        self.codigo = codigo
        self.quantidade = int(quantidade)
        self.nome = nome
        self.preco = preco
    
    def get_codigo(self):
        return self.codigo
    
    def get_quantidade(self):
        return self.quantidade
    
    def get_nome(self):
        return self.nome
    
    def set_quantidade(self):
        quantidade = int(input("Informe a quantidade quantidade: "))
        self.quantidade = quantidade
        return 'Quantidade Atualizada!'

    def set_nome(self):
        nome = input("Atualize o nome: ")
        self.nome = nome
        return 'Nome Atualizado!'
    
    def set_codigo(self):
        codigo = input("Atualize o codigo: ")
        self.codigo = codigo
        return 'Codigo Atualizado!'
    
    def get_preco(self):
        return self.preco

    def set_preco(self):
        print(f"Valor atual: {self.preco}")
        self.preco = float(input("Novo valor: "))
        return "Valor atualizado!"
    
class Carrinho():
    def __init__(self, dic_prod, valor):
        self.produtos = dic_prod
        self.valor = valor
    
    def limpaCarrinho(self):
        self.produtos.clear()
        self.valor = 0
        return 'O carrinho foi limpo!'
        
    def add_item_carrinho(self,produto):
        self.consultaCarrinho()
        print(f"{produto.nome} - Valor por Unidade: R${produto.preco}")
        quantidade = int(input('quantidade: '))
        if quantidade > produto.quantidade:
            print(f"Sem produtos suficientes para a demanda solicitada!!\nAdicionado valor disponivel do produto : {produto.quantidade}")
            print()
            quantidade = produto.quantidade
        if produto in self.produtos.keys():
            if quantidade > produto.quantidade:
                print(f"Sem produtos suficientes para a demanda solicitada!!\nAdicionado valor disponivel do produto : {produto.quantidade}")
                print()
                produtos_adicionados = produtos.quantidade - quantidade
                total_produtos = produto.quantidade
                self.produtos[produto] = total_produtos
                self.valor += produtos_adicionados*produto.valor
                
            else:
                self[produto] += quantidade
                self.valor += produto.preco * quantidade
        else:
            self.produtos[produto] = quantidade
            self.valor += produto.preco * quantidade
        print(f'Produto {produto.nome} adicionado ao carrinho!\nValor do carrinho = {self.valor}')
        return True    

    def consultaCarrinho(self):
        print("Carrinho")
        try:
            if len(self.produtos) == 0:
                print("Vazio!")
                return True
            else:
                for produto, qt in self.produtos.items():
                    prod_atual = produto.get_nome()
                    print(f'Produtos: {prod_atual} - {qt} unidade(s)')
                print(f"Valor total = R${self.valor}")
                return False
        except:
            print("Vazio!")
    
    def setQtitens(self,produto):
        quantidade = int(input(f"Atualize a quantidade de itens de {produto.nome}: "))
        self.produtos[produto] = quantidade
        if quantidade > produto.quantidade:
            print(f"Sem produtos suficientes para a demanda solicitada!!\nAdicionado valor disponivel do produto : {produto.quantidade}")
            print()
            quantidade = produto.quantidade
        else:
            if self.produtos.keys() - quantidade < 0:
                self.valor -= (self.produtos[produtos].keys() - quantidade)* self.produtos[produtos.valor]

    def atualizarCarrinho(self):
        self.consultaCarrinho()
        codigo_produto = input("Informe o código do produto que deseja atualizar: ")
        for produto in self.produtos.keys:
            if produto.codigo == codigo_produto: 
                self.setQtitens(produto)
        else:
            print("Produto não está no carrinho!")

class Compra():
    def __init__(self,comprador, produtos, valor):
        self.comprador = comprador
        self.produtos = produtos
        self.valor = valor
    
    def get_comprador(self):
        return self.comprador

    def get_produtos(self):
        return self.produtos
    
    def get_valor(self):
        return self.valor
    
    
    def finaliza_compra(self):
        print("Dados Comprador: ")
        print(f'Nome: {self.comprador.nome}\nCPF: {self.comprador.cpf}')
        print("Produtos: ")
        for produto, qt in self.produtos.items():
            print(f'Produto: {produto.nome} - Quantidade: {qt}')
        print(f'Valor total: {self.valor}')
        print("----------")
        confirmar_compra = input("Confirmar compra? (S/N): ")
        while confirmar_compra != 'S' and confirmar_compra != 'N':
            confirmar_compra = input("Confirmar compra? (S/N): ")
        if confirmar_compra == 'S':
            cliente = self.comprador 
            lista_produtos = self.produtos.copy()
            valor = self.valor
            return lista_produtos, valor
        else:
            self.comprador.limpaCarrinho()
            return 'Compra cancelada!'

class Pessoa():
    def __init__(self, nome,cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_senha(self):
        return self.senha
    
    def setSenha(self):
        senha = input("Informe a nova senha: ")
        while len(senha) < 8 or (senha.isalpha() == True) or (senha.isnumeric() == True):
            print("A senha deve possuir pelo menos 8 Caracteres, possuir vogais e numeros")
            senha = input("Informe a senha: ")
        self.senha = senha
        return 'Senha Atualizada!'

class Cliente(Pessoa): 
    def __init__(self,nome,cpf,senha,compras_realizadas):
        super().__init__(nome,cpf,senha)
        self.carrinho = Carrinho({}, 0)
        self.compras_realizadas = []

    def getCarrinho(self):
        return self.carrinho

    def limparCarrinho(self):
        self.carrinho = []
    
    def getComprasRealizadas(self):
        if len(self.compras_realizadas) == 0:
            return 'Nenhuma compra realizada!'
        else:
            for compra in self.compras_realizadas:
                for prod in compra.produtos:
                    print(f'Produto: {prod.nome} - Quantidade: {compra.produtos[prod]}')
                print(f'Valor total: {compra.valor}')
                print("----------")


    def realiza_compra(self, carrinho, valor):
        self.compras_realizadas.append(Compra(self.nome, carrinho, valor))
        self.carrinho.produtos.clear()
        self.carrinho.valor = 0
        print("Compra realizada com sucesso!")
        return True
    
    def getDados(self):
        print(self.nome)
        print(f'CPF = {self.cpf}')
        print(f'Senha do sistema = {self.senha}')
        print('Consultar extrato? digite "1" para sim')
        escolha = int(input())
        if escolha == 1:
            print(self.getComprasRealizadas())
    
class Funcionario(Pessoa): 
    def __init__(self,nome,cpf,senha,registro,conta_banc,salario):
        super().__init__(nome,cpf,senha)
        self.nreg = int(registro)
        self.conta_banc = conta_banc
        self.salario = salario
    
    def get_nreg(self):
        return self.nreg
    
    def get_conta_banc(self):
        return self.conta_banc
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self): 
        salario = float(input("Informe o novo salario"))
        self.salario = salario
        return 'Salário Atualizado!'

    def set_conta_banc(self):
        conta_banc = input("Informe a nova conta bancaria: ")
        self.conta_banc = conta_banc
        return 'Conta Bancaria Atualizada!'
    
class Gerente(Funcionario):
    def __init__(self,nome,cpf,senha,registro,conta_banc,salario):
        super().__init__(nome,cpf,senha,registro,conta_banc,salario)
        permissaoAdm = True
    
    


p1 = Produto(1,10,'Arroz', 10)
p2 = Produto(2,10,'Feijão', 5)
p3 = Produto(3,10,'Macarrão', 3)
p4 = Produto(4,10,'Carne', 20)
p5 = Produto(5,10,'Frango', 15)
p6 = Produto(6,10,'Coca-Cola', 5)
p7 = Produto(7,10,'Pepsi', 5)
p8 = Produto(8,10,'Guaraná', 5)
p9 = Produto(9,10,'Suco', 5)

produtos = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
