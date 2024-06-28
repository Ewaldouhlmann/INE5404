from classes import Produto, Funcionario, Cliente, Gerente
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
#Lista de funcionarios  
funcionario1 = Funcionario("Pedrinho", "98765432101", "senha123", 1000, 1,1750)
funcionario2 = Funcionario("Joaozinho", "98765432102", "senha123", 1000, 2,1750)
funcionario3 = Funcionario("Carlinhos", "98765432103", "senha123", 1000, 3,1750)
gerente1 = Gerente("Gerente", "98765432100", "senha123", 1000, 0,1750)
lista_funcionarios = [funcionario1,funcionario2,funcionario3, gerente1]

#Lista de clientes
pessoa2 = Cliente('Joao','12345678910','123456',[])
pessoa3 = Cliente('Carlos','12345678911','123457',[])
pessoa4 = Cliente('Pedro','12345678912','123458',[])
pessoa5 = Cliente('Maria','12345678913','123459',[])
pessoa6 = Cliente('Ana','12345678914','123450',[])
lista_clientes = [pessoa2,pessoa3,pessoa4,pessoa5,pessoa6]  