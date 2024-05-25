class Cartas():
    def __init__(self, valores, naipe):
        self.carta = valores + ' de ' + naipe

class Baralho():
    def __init__(self):
        self.baralho = []
        valores = ('Ás', '2', '3', '4','5','6','7','8','9','10','J','Q','K')
        naipes = ('Paus', 'Copas', 'Espadas','Ouros')
        for valor in valores:
            for naipe in naipes:
                self.baralho.append(Cartas(valor, naipe))

    def getCartas(self):
        cartas_str = ' - '.join([carta.carta for carta in self.baralho])
        print(cartas_str)
        print()
        

class Jogador():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.lista_cartas = []
    
    def embaralhar(self, baralho):
        from random import shuffle
        print(f'{self.nome} irá embaralhar!')
        print("Embaralhando...")
        print()
        shuffle(baralho.baralho)

    def AdicionarJogadores():
        lista_jogadores = []
        numero_jogadores = int(input("Informe o número de jogadores: "))
        while 0 > numero_jogadores or numero_jogadores > 9:
            numero_jogadores = int(input("Informe o número de jogadores: "))
        for i in range(numero_jogadores):
            print(f"Informe os dados do jogador {i+1}")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            novo_jog = Jogador(nome, idade)
            lista_jogadores.append(novo_jog)
        return lista_jogadores

    def entregarCartas(self, lista_jogadores, baralho):
        cartas_por_jog = int(input("Número de cartas por jogador: "))
        while cartas_por_jog * len(lista_jogadores) > 52+len(lista_jogadores):
             cartas_por_jog = int(input("Número de cartas por jogador: "))
        while True:
            try:
                for jogador in lista_jogadores:
                    carta = baralho.pop()
                    if len(jogador.lista_cartas) < cartas_por_jog:
                        jogador.lista_cartas.append(carta)
                        print(f"{jogador.nome} recebeu a carta: {carta.carta}")
                    else:
                        print("Todos os jogadores receberam o número de cartas solicitadas!")
                        return True 
            except IndexError:
                print("Todas as cartas do baralho foram entregues!")
                print("Não foi possível entregar o número de carros solicitadas para todos os jogadores.")
                break
    
    def consultarcartas_por_jogador(self, lista_jogadores):
        for j in lista_jogadores:
            print(j.nome, end = ' Cartas: ')
            for c in j.lista_cartas:
                if c == j.lista_cartas[-1]:
                    print(c.carta)
                else:
                    print(c.carta, end = ' - ')
            print()


    
    
    
    
jogadores = [
    Jogador(nome="Jogador 1", idade=25),
    Jogador(nome="Jogador 2", idade=30),
    Jogador(nome="Jogador 3", idade=22),
    Jogador(nome="Jogador 4", idade=28),
    Jogador(nome="Jogador 5", idade=35),
    Jogador(nome="Jogador 6", idade=19),
    Jogador(nome="Jogador 7", idade=40),
    Jogador(nome="Jogador 8", idade=27),
    Jogador(nome="Jogador 9", idade=23)
]
b1 = Baralho()


def escolhanum_valida(msg, menoropc, maioropc):
    print("Escolha uma opção: ")
    print(msg)
    escolha = int(input())
    while menoropc > escolha or escolha > maioropc:
        print("Escolha uma opção válida: ")
        print(msg)
        escolha = int(input())
    return escolha


def gerar_rodadas():
    from random import randint
    indice_atual_dealer = randint(0,len(lista_jogadores))
    while True:
        baralho = Baralho()
        for i, jogador in enumerate(lista_jogadores):
            if i == indice_atual_dealer:
                dealer_atual = jogador
                indice_atual_dealer = i
        baralho.getCartas()
        dealer_atual.embaralhar(baralho)
        baralho.getCartas()
        dealer_atual.entregarCartas(lista_jogadores, baralho.baralho)
        consulta_cartas = escolhanum_valida("Consultar cartas por jogador?(1 - Sim, 2 - Não)",1,2)
        if consulta_cartas == 1:
            dealer_atual.consultarcartas_por_jogador(lista_jogadores)
            nova_rodada = escolhanum_valida("Nova rodada\n1 - Sim\n2 - Não",1,2)
        if nova_rodada == 1:
            if len(lista_jogadores) > indice_atual_dealer+1:
                    indice_atual_dealer += 1
            else:
                indice_atual_dealer = 0
            for j in lista_jogadores:
                j.lista_cartas.clear()
        if nova_rodada == 2:
            break

lista_jogadores = jogadores
while True:
    novo_jogo = escolhanum_valida("1 - Nova partida com mesmos jogadores\n2 - Nova partida com jogadores diferentes", 1 ,2)
    if novo_jogo == 1:
        gerar_rodadas()
    if novo_jogo == 2:
        lista_jogadores = Jogador.AdicionarJogadores()
        gerar_rodadas()
    
    
    
    