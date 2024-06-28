# Função: Classe Pessoa, Cliente e Funcionario

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
        senha = input("Informe a nova senha")
        while len(senha) < 8 or (senha.isalpha() == True) or (senha.isnumeric() == True):
            print("A senha deve possuir pelo menos 8 Caracteres, possuir vogais e numeros")
            senha = input("Informe a senha: ")
            return 'Senha Atualizada!'

class Cliente(Pessoa): 
    def __init__(self,nome,cpf,senha,carrinho,compras_realizadas):
        super().__init__(nome,cpf,senha)
        self.carrinho = carrinho
        self.compras_realizadas = compras_realizadas

    def getCarrinho(self):
        return self.carrinho

    def limparCarrinho(self):
        self.carrinho = []
    
    def getComprasRealizadas(self):
        if len(self.compras_realizadas) == 0:
            return 'Nenhuma compra realizada!'
        else:
            return self.compras_realizadas

    def finaliza_compra(self, carrinho, valor):
        self.compras_realizadas[carrinho] = valor
        return 'Compra realizada com sucesso!'
    
    
class Funcionario(Pessoa): 
    def __init__(self,nome,cpf,senha,registro,conta_banc,salario):
        super().__init__(nome,cpf,senha)
        self.nreg = registro
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

#Lista de funcionarios  
pessoa1 = Funcionario('Joao','12345678910','123456','123456','123456789','1000')
pessoa2 = Funcionario('Carlos','12345678911','123457','123457','123456780','2000')
pessoa3 = Funcionario('Pedro','12345678912','123458','123458','123456781','3000')
lista_funcionarios = [pessoa1,pessoa2,pessoa3]

#Lista de clientes
pessoa2 = Cliente('Joao','12345678910','123456',[],[])
pessoa3 = Cliente('Carlos','12345678911','123457',[],[])
pessoa4 = Cliente('Pedro','12345678912','123458',[],[])
pessoa5 = Cliente('Maria','12345678913','123459',[],[])
pessoa6 = Cliente('Ana','12345678914','123450',[],[])
lista_clientes = [pessoa2,pessoa3,pessoa4,pessoa5,pessoa6]  