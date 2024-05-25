from pessoa import Cliente
import Veiculos

class Locacao():
    def __init__(self, pessoa, veiculo, tempo_locacao, valor_locacao):
        self.pessoa = pessoa
        self.veiculo = veiculo
        self.tempo_loc = tempo_locacao
        self.valor_loc = valor_locacao
    
    def setvalor_loc(veiculo, dias):
        valor_loc = veiculo.preco * dias
        return valor_loc
    
    @classmethod
    def getLocacoes(loca, cliente):
        if loca.pessoa.cpf == cliente.cpf:
            if isinstance (loca.veiculo, Veiculos.Carro):
                loca.veiculo.Cliente_consulta_Carro()
            else:
                loca.veiculo.Cliente_consulta_Motos()
            return True, loca
        else:
            return False

    def getLocacao(self):
        return f'{self.pessoa.nome}, {self.pessoa.cpf} -> {self.veiculo.modelo}-{self.veiculo.ano}({self.veiculo.placa})'         
    
    @staticmethod
    def consultarLocacoes(lista_loc):
        for locacao in lista_loc:
            print(f'{locacao.pessoa.nome}, CPF: {locacao.pessoa.cpf} - > {locacao.veiculo.modelo} - {locacao.veiculo.ano}, Placa: {locacao.veiculo.placa}')
            print(f"Valor da locação: R${locacao.valor_loc}")
            print(f"Tempo de locação: {locacao.tempo_loc} dias")
            print()
        placa = input()
        return placa

    def getLocabycar(carro, lista_loc):
        for loc in lista_loc:
            if carro == lista_loc.veic:
                return loc



    def criarLocacao(cliente, veiculo, valor, tempolocacao, lista_locacao):
        new_loc = Locacao(cliente, veiculo, tempolocacao, valor)
        lista_locacao.append(new_loc) 
    
    def verifica_tipoCNH(cliente, veiculo):
        if 'A' in cliente.categoria_cnh and isinstance(veiculo, Veiculos.Moto):
            return True
        elif 'B' in cliente.categoria_cnh and isinstance(veiculo, Veiculos.Carro):
            return True
        else:
            print("O cliente não possui CNH para esse tipo de veículo!")
            return False


    def extenderLocacao(self, qtdias):
        self.tempo_loc += qtdias
        self.valor_loc = self.veiculo.preco * qtdias
        print(f"Prazo e valores alterados!!")

    def reduzLocacao(self, qtdias):
        self.tempo_loc -= qtdias
        self.valor_loc = self.veiculo.preco * qtdias
        print("Locação reduzida!")
    
    def finalizaLocacao(lista_locacao):
        indice = 0
        for locacao in lista_locacao:
            print(indice)
            print(locacao.pessoa.nome)
            print(f'{locacao.veiculo.modelo} - {locacao.veiculo.ano}')
            indice += 1

        print("Qual locacao deseja finalizar? ")
        opcao = int(input())
        lista_locacao[opcao-1].veiculo.disponibilidade = True
        lista_locacao.pop(opcao)
        print("Locacao finalizada!")



cliente = Cliente("João da Silva", "12345678901", "senha123", "Rua A", "123",15, "987654321", "B", "2023-08-31")
carro = Veiculos.Carro("Ford", "Fiesta", 2022, "Azul", "ABC123", True, 100, "Sedan", ["Ar condicionado", "GPS"])
loc1 = Locacao(cliente, carro, 15, 185)
lista_loc = []
lista_loc.append(loc1)

