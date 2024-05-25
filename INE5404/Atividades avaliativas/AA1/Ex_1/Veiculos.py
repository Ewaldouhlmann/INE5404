class Veiculo:
    def __init__ (self, marca, modelo, ano, cor, placa, disponibilidade, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa
        self.disponibilidade = disponibilidade
        self.preco = preco

    def Cliente_consulta_Veiculos (self):
        print(f'Marca: {self.marca}')
        print(f"Modelo: {self.modelo} - {self.ano}({self.cor})")
        print(f"Placa: {self.placa}, Custo da diária = {self.preco}")
    
    def getPreco(self):
        return self.preco

    def pegaVeiculo(listaveiculos):
        placa = input('Placa do veículo: ')
        while True:
            for veic in lista_veiculos:
                if placa == veic.placa:
                    return veic
            print("Veículo não encontrado, informe uma placa válida: ")
            placa = input()
            
    def addVeiculo(listaveic):
        print("Informe os dados do veículo")
        marca = input("Marca:")
        modelo = input("Modelo:")
        ano = int(input("Ano"))
        cor = input("Cor")
        placa = input("Placa")
        disponibilida = True
        preco = float(input("Preco: "))
        print("1 - Carro, 2 - Moto")
        carro_moto = int(input())
        if carro_moto == 1:
            categoria = input("Categoria: ")
            adds = input("Adicionais: ")
            novo_carro = Carro(marca, modelo, ano, cor, placa, disponibilida, preco, categoria,adds)
            lista_veiculos.append(novo_carro)
        else:
            cilindradas = input("Cilindradas: ")
            nova_moto = Moto(marca, modelo, ano, cor, placa, disponibilida, preco, cilindradas)
            listaveic.append(nova_moto)

    def disp_veic(self):
        self.disponibilidade = bool("Disponivel? (True/False)")

    def removerVeic(lista, placa):
        for veiculo in lista_veiculos:
            if veiculo.placa == placa:
                lista_veiculos.remove(veiculo)  
                print("Veiculo removido!") 

class Carro(Veiculo):
    def __init__ (self, marca, modelo, ano, cor, placa, disponibilidade, preco, categoria, adicionais):
        super().__init__(marca,modelo, ano, cor, placa, disponibilidade, preco)
        self.categoria = categoria
        self.adicionais = adicionais
    
    def Cliente_consulta_Carro(self):
        print(self.categoria)
        super().Cliente_consulta_Veiculos()
        if not self.adicionais:
            print('Sem adicionais!')
        else:
            print(f'Adicionais: ', end= ' ')
            for add in self.adicionais:
                print(add, end = ',')
            print()




class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, placa, disponibilidade, preco, cilindradas):
        super().__init__(marca, modelo, ano, cor, placa, disponibilidade, preco)
        self.cilindradas = cilindradas

    def Cliente_consulta_Motos(self):
        print(f"Cilindradas: {self.cilindradas}cc")
        super().Cliente_consulta_Veiculos()


carro1 = Carro("Ford", "Fiesta", 2022, "Azul", "ABC123", True, 100, "Sedan", ["Ar condicionado", "GPS"])
carro2 = Carro("Toyota", "Corolla", 2023, "Prata", "XYZ456", True, 120, "Sedan", ["Ar condicionado"])
moto1 = Moto("Honda", "CBR", 2021, "Vermelha", "DEF789", True, 80, "250")
moto2 = Moto("Yamaha", "MT-07", 2022, "Preto", "GHI101", True, 90, "700")
lista_veiculos = [carro1, carro2, moto1, moto2]
