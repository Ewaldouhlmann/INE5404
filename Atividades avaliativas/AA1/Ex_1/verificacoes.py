import Veiculos
import pessoa
def escolhaNumerica(valor_min, valor_max, mensagem):
    print(mensagem)
    escolha = int(input())
    while valor_min > escolha or valor_max < escolha:
        print(f"Escolha um valor maior que {valor_min} e menor que {valor_max}")
        escolha = int(input())
    return escolha

def tamanhoStr(str, tamanho_min, msg):
    while len(str) < tamanho_min:
        print(f"Minimo {tamanho_min} caracteres")
        str = input(msg)

def estanaLinsta(lista):
    cpf = input("Cpf: ")
    senha = input("Senha: ")
    while True:
        for pessoa in lista:
            if pessoa.senha == senha and pessoa.cpf == cpf:
                return pessoa
        print("Informe dados válidos: ")
        cpf = input("Cpf: ")
        senha = input("Senha: ")

def possui_n_certo(cpf):
    while True:
        if len(cpf) == 11:
            return cpf
        else:
            print("Informe o cpf sem '-' e '.'(11 digitos)")
            cpf = input('CPF')

def valor_aceitavel(nmin, nmax, mensagem_erro, mensagem_valor):
    valor = int(input(f"{mensagem_valor}: "))
    while nmin > valor or valor > nmax:
        print(mensagem_erro)
        valor = int(input(f'{mensagem_valor}: '))
    return valor

def valor_min(idade, valormin):
    while idade < valormin:
        print("O cliente deve ter no minimo 18 anos!")
        idade = int(input())

def continuar():
    while True:
        continuar = input("Continuar? (S/N)").upper()
        if continuar == 'S' or continuar == 'N':
            break