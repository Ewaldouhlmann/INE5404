import pessoa
class Produto():
    def __init__(self,codigo,quantidade, nome, preco):
        self.codigo = codigo
        self.quantidade = quantidade
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
    
    def remove_quantidade(self,unidades):
        self.quantidade -= 1*unidades
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
        while quantidade > produto.quantidade:
            print(f"Sem produtos suficientes para a demanda solicitada!!/n{produto.nome} - quantidade: {produto.quantidade}")
            quantidade = int(input('Informe a quantidade de itens que deseja: '))
        self.produtos[produto] = quantidade
        self.valor += produto.preco * quantidade
        return f'Produto {produto.nome} adicionado ao carrinho!/nValor do carrinho = {self.valor}        '
 
    def consultaCarrinho(self):
        print("Carrinho")
        for produto, qt in self.produtos.items():
            prod_atual = produto.get_nome()
            print(f'Produtos: {prod_atual} - {qt} unidade(s)')
        return f"Valor total = R${self.valor}"


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
        self.comprador.finaliza_compra(self.comprador, self.produtos, self.valor)
        for produto, qt in self.produtos.items():
            produto.remove_quantidade(qt)
        self.comprador.carrinho.limpaCarrinho()
        return 'Compra realizada com sucesso!'
    

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
