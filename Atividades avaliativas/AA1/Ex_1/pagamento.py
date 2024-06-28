from pessoa import Cliente
import verificacoes
class Pagamento(Cliente):
    def __init__(self, cliente,nome_cartao, cpf_cartao, num_cartao, cod):
        self.cliente = cliente
        self.nome_cartao = nome_cartao
        self.cpf_cartao = cpf_cartao
        self.num_cartao = num_cartao
        self.cod = cod
    
    def setDadosPagamento(cliente):
        print("Informe os dados do cartão de crédito:")
        nome_cartao = input("Nome: ")
        cpf_cartao = input("CPF do dono do cartão:")
        num_cartao = input("Número do cartão: ")
        cod_cartao = input("Código de verificação: ")
        return Pagamento(cliente, nome_cartao, cpf_cartao, num_cartao, cod_cartao)
    
    def realizaPagamento(cliente, pagamento):
        while True:
            possuiLimite = True
            if cliente.cpf == pagamento.cpf_cartao and possuiLimite == True:
                print("Pagamento realizado!!\nVá até a locadora com sua CNH para retirada do veículo.")
                return True
            else:
                print("Pagamento não realizado!")
                return False

