from classes import Produto, Compra, Carrinho, Pessoa, Cliente, Funcionario, Gerente
from listas import lista_clientes, lista_funcionarios, produtos
from empresa import Empresa

def __menu_cliente(cliente, empresa):
    print(f"Bem vindo {cliente.nome}")
    while True:
        try:
            print("0 - Sair")
            print("1 - Meus dados")
            print("2 - Realizar compra")
            print("3 - Histórico de compras")
            escolha = int(input("Escolha uma opção: "))
            while escolha < 0 or escolha > 3:
                print("Opção inválida!")
                escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                cliente.getDados()
                print("0 - Sair")
                print("1 - Alterar senha")
                print("2 - Excluir usuário")
                escolha = int(input())
                while escolha < 0 or escolha > 2:
                    print("0 - Sair")
                    print("1 - Alterar senha")
                    escolha = int(input())
                if escolha == 1:
                    cliente.setSenha()
                if escolha == 2:
                    print(empresa.excluircliente(cliente.cpf))
                    break
 
            elif escolha == 2:
                print("Tela Produtos")
                while True:
                    empresa.get_produtos()              
                    print("1 - Adicionar produto ao carrinho")
                    print("2 - Finalizar compra")
                    print("3 - Voltar")
                    escolha = int(input())
                    if escolha < 1 or escolha > 3:
                        break
                    #Adicionar Produtos
                    if escolha == 1:
                        print("Adicionar item no carrinho")
                        produto_compra = empresa.Selecionar_produto()
                        carrinho_cliente = cliente.carrinho
                        carrinho_cliente.add_item_carrinho(produto_compra)
                    #Consultar Carrinho
                    elif escolha == 2:
                        print("Consultando carrinho...")
                        cliente.carrinho.consultaCarrinho()
                        while True:
                            print("1 - Prosseguir para compra\n2 - Limpar carrinho\n3 - Sair")
                            escolha = int(input("Escolha uma opção: "))
                            while escolha < 0 or escolha > 3:
                                print("Opção inválida!")
                                escolha = int(input("Escolha uma opção: "))
                            if escolha == 1:
                                print("Tela Compra")
                                carrinho_decompras = cliente.carrinho.produtos
                                valor_total = cliente.carrinho.valor
                                print(cliente.carrinho.valor)
                                print(cliente.carrinho.produtos)
                                compra_atual = Compra(cliente, carrinho_decompras, valor_total)   
                                lista_compras, custo_total = compra_atual.finaliza_compra()
                                cliente.realiza_compra(lista_compras, custo_total)
                                empresa.atualiza_qtprod(lista_compras)
                                print("Compra realizada com sucesso!")  
                                break
                            elif escolha == 2:
                                print(cliente.carrinho.limpaCarrinho())
                                break
                            else:
                                break  
                    elif escolha == 3:
                        break   
                    continuar = input('Continuar?')
                    if continuar == 'N':
                            break
                
            elif escolha == 3:
                cliente.getComprasRealizadas()

            else:
                return True
        except:
            print("Erro!")
    
def opcoesFunc():
    print("1 - Adicionar Produto")
    print("2 - Editar Produto")
    print("3 - Visualizar Produtos")
    print("4 - Excluir produto")
    print("5 - Editar meus dados")
    print("---GERENTE----")
    print("6 - Adicionar funcionário")
    print("7 - Excluir funcionários")
    print("8 - Consultar funcionários")
    print("9 - Editar dados dos funcionários")
    print("0 - Sair")
     
def telaFunc(empresa, funcionario):
    while True:
        print(f'Bem vindo {funcionario.nome}')
        opcoesFunc()
        escolha = int(input("Escolha uma opção: "))
        while escolha < 0 or escolha > 9:
            opcoesFunc()
            escolha = int(input("Escolha uma opção válida: "))
        if escolha == 1:
            empresa.criar_produto()
        elif escolha == 2:
            produto = empresa.Selecionar_produto()   
            produto.set_nome() 
            produto.set_quantidade()
            produto.set_preco()
            produto.set_codigo()
        elif escolha == 3:
            empresa.get_produtos()
        elif escolha == 4:
            empresa.excluir_produto()
        elif escolha == 5:
            funcionario.setSenha()
        else:
            if not isinstance(funcionario, Gerente):
                print("O usuário não é gerente, não tem permissão para acessar essa opção!")
            else:
                if escolha == 6:
                    empresa.criar_func()
                elif escolha == 7:
                    empresa.excluir_func()
                elif escolha == 8:
                    empresa.consultar_func()
                else:
                    empresa.editar_dadosfunc()
        continuar = int(input("Deseja continuar? 1 - Sim / 2 - Não: "))
        if continuar == 2:
            return True
        
    
while True:
    estoque = produtos
    lista_clientes = lista_clientes
    lista_func = lista_funcionarios 
    empresa = Empresa(estoque, lista_clientes, lista_func)
    try:
        #TELA INICIAL
        print("1 - Novo usuário")
        print("2 - Login")
        escolha = int(input("Escolha uma opção: "))
        while escolha < 0 or escolha > 2:
            print("Opção inválida!")
            escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            #CADASTRO DE NOVO USUARIO
            print("Cadastro de novo usuário: (1-Cliente / 2-Funcionário)")
            escolha = int(input("Escolha uma opção: ")) 
            while escolha < 0 or escolha > 2:
                print("Opção inválida!")
                escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                #CADASTRO DE CLIENTE
                novo_cliente = empresa.criar_cliente()
                #TELA CLIENTE
                continuar = __menu_cliente(novo_cliente,empresa)
                if continuar == True:
                    break
            if escolha == 2:
                #CADASTRO DE FUNCIONARIO
                senha_sistema = '1234senha'
                senha = input("Informe a senha do sistema: ")
                while senha != senha_sistema:
                    print("Senha incorreta!")
                    senha = input("Informe a senha do sistema: ")
                novo_func = empresa.criar_func()
                #TELA FUNCIONARIO
                telaFunc(empresa,novo_func)
# não esta saindo da tela do cliente
        if escolha == 2:
            #LOGIN
            print("Informe seus dados para acessar o sistema: ")
            cpf = input("Informe seu cpf: ")
            senha = input("Informe sua senha: ")
            while True:               
                cliente_atual = empresa.logar_cliente(cpf, senha)
                func_atual = empresa.logar_func(cpf, senha)
                if cliente_atual != None:
                    #TELA CLIENTE
                    print(cliente_atual.nome)
                    continuar = __menu_cliente(cliente_atual, empresa)   
                    if continuar == True:
                        break
                elif func_atual != None:
                    cont = telaFunc(empresa,func_atual)
                    if cont == True:
                        break
                else:
                    print("Usuário não encontrado\n1 - digite novamente ou 2 - sair!")
                    escolha = int(input())
                    while escolha < 0 or escolha > 2:
                        print("Opção inválida!\n1 - digite novamente ou 2 - sair!")
                        escolha = int(input("Escolha uma opção: "))
                    if escolha == 1: 
                        cpf = input("Informe seu cpf: ")
                        senha = input("Informe sua senha: ")
                    if escolha == 2:
                        break
                    
                
                    
    except:
        pass