import verificacoes
class Pessoa():
    def __init__(self, nome, cpf, senhasistema, rua_endereco, n_casa, idade):
        self.nome = nome
        self.cpf = cpf
        self.senha = senhasistema
        self.rua_endereco = rua_endereco
        self.n_casa = n_casa
        self.idade = idade
    
    def getAtributos(self):
        print(f"Nome: {self.nome}, CPF:{self.cpf}")
        print(f"Senha do sistema: {self.senha}")
        print(f"Endereço: {self.rua_endereco} - {self.n_casa}")
    
    def alterar_Senha(pessoa, senha):
        pessoa.senha = senha

class Cliente(Pessoa):
    def __init__(self, nome, cpf, senhasistema, rua_endereco, n_casa, idade, CNH, categoria_CNH, dataexp_CNH):
        super().__init__(nome, cpf, senhasistema, rua_endereco, n_casa, idade)
        self.CNH = CNH
        self.categoria_cnh = categoria_CNH
        self.dataexp_CNH = dataexp_CNH
    
    def getAtributos(self):
        super().getAtributos()
        print(f"Nº CNH: {self.CNH}\nData de expedição: {self.dataexp_CNH}, Categoria: {self.categoria_cnh}")
        print()

    def criarCliente():
        print("Informe seus dados: ")
        nome = input("Nome: ")
        verificacoes.tamanhoStr(nome,8, 'Nome: ')
        cpf_input = input("CPF: ")
        cpf = ''.join(filter(str.isdigit, cpf_input))
        cpf = verificacoes.possui_n_certo(cpf)
        senha = input("Cadastrar senha: ")
        rua = input("Rua: ")
        n_casa = input("Número: ")
        idade = int(input("Idade: "))
        verificacoes.valor_min(idade,18)
        cnh = input("CNH: ")
        verificacoes.tamanhoStr(cnh,8, 'CNH: ')
        categoria_cnh = ''
        cnh_p_moto = verificacoes.escolhaNumerica(1, 2, 'Possui CNH para motos?(1 - Sim, 2 - Não)')
        if cnh_p_moto == 1:
            categoria_cnh += 'A'
        cnh_p_carro = verificacoes.escolhaNumerica(1, 2, 'Possui CNH para carros?(1 - Sim, 2 - Não)')
        if cnh_p_carro == 1:
            categoria_cnh += 'B'
        print("Informe a data de expedição da sua CNH:")
        dataexp_cnh = ''
        diaexp = str(verificacoes.valor_aceitavel(1,31, 'Dia inválido!', 'Dia'))
        dataexp_cnh += diaexp + '/'
        mesexp = str(verificacoes.valor_aceitavel(1,12,'Mês inválido!', 'Mês'))
        dataexp_cnh += mesexp + '/'
        anoexp = str(verificacoes.valor_aceitavel(1940,2023,'Ano inválido!', 'Ano'))
        dataexp_cnh += anoexp
        
        return Cliente(nome, cpf, senha, rua, n_casa,idade, cnh, categoria_cnh,dataexp_cnh)
    
    def cnh_comTsuf(self):
        if self.idade > 21:
            return True
        else:
            from datetime import datetime
            dia_atual = datetime.now().date()
            expedicao_cnh = datetime.strptime(self.dataexp_CNH, '%d/%m/%Y').date()
            if (dia_atual - expedicao_cnh).days > 730:
                return True
        print("O cliente não possui pelo menos 21 anos, nem CNH a mais de 2 anos!")
        return False
    
    def set_senha(self, senha):
        self.senha = senha
    
    def set_categria_cnh(self):
        categoria_cnh = ''
        cnh_p_moto = verificacoes.escolhaNumerica(1, 2, 'Possui CNH para motos?(1 - Sim, 2 - Não)')
        if cnh_p_moto == 1:
            categoria_cnh += 'A'
        cnh_p_carro = verificacoes.escolhaNumerica(1, 2, 'Possui CNH para carros?(1 - Sim, 2 - Não)')
        if cnh_p_carro == 1:
            categoria_cnh += 'B'
        self.categoria_cnh = categoria_cnh

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, senhasistema, rua_endereco, n_casa,idade, n_registro):
        super().__init__(nome, cpf, senhasistema, rua_endereco, n_casa, idade)
        self.nregistro = n_registro
    
    def getAtributos(self):
        super().getAtributos()
        print(f"Nº registro: {self.nregistro}")
        print()
    
cliente1 = Cliente("João da Silva", "12345678901", "senha123", "Rua A", "123",22, "987654321", "B", "30/08/2023")
cliente2 = Cliente("Maria Oliveira", "98765432109", "senha456", "Rua B", "456",25, "654321987", "A", "09/30/2020")
funcionario1 = Funcionario("Lucas Santos", "11122233344", "senha789", "Rua C",38, "789", "F12345")
funcionario2 = Funcionario("Ana Pereira", "55566677788", "senhaabc", "Rua D", 42,"987", "F67890")
lista_func = [funcionario1, funcionario2]
lista_cliente = [cliente1, cliente2]
