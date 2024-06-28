import Veiculos
import pessoa
import verificacoes
import locacao
import pagamento
lista_funcionarios = pessoa.lista_func
lista_cliente = pessoa.lista_cliente
lista_veiculos =Veiculos.lista_veiculos
lista_locacoes = locacao.lista_loc
while True:
    print('Bem vindo(a)!!!')
    escolha = verificacoes.escolhaNumerica(1,2, 'Escolha uma opção:\n1 - Cliente\n2 - Funcinário')
    if escolha == 1:
        cliente_cadastrado = verificacoes.escolhaNumerica(1,2, "1 - Possuo cadastro\n2 - Novo Usuário")
        if cliente_cadastrado == 1:
            print("Informe os seus dados: ")
            cliente_atual = verificacoes.estanaLinsta(lista_cliente)
            while True:
                print()
                print(f'Bem vindo(a) {cliente_atual.nome}!!\nComo poderiamos te ajudar?')
                escolha_cliente = verificacoes.escolhaNumerica(1,5,"1 - Locação\n2 - Minhas locações\n3 - Meus dados\n4 - Sair")
                if escolha_cliente == 1:
                    for veiculo in lista_veiculos:
                        if isinstance(veiculo, Veiculos.Carro) and veiculo.disponibilidade == True:
                            veiculo.Cliente_consulta_Carro()
                        elif isinstance(veiculo, Veiculos.Moto) and veiculo.disponibilidade == True:
                            veiculo.Cliente_consulta_Motos()
                        print()
                    print()
                    realiza_loc = verificacoes.escolhaNumerica(1,2,"Realizar locação?\n1- Sim, 2 - Não")
                    if realiza_loc == 1:
                        carro_locacao = Veiculos.Veiculo.pegaVeiculo(lista_veiculos)
                        cnh_pveic = locacao.Locacao.verifica_tipoCNH(cliente_atual, carro_locacao)
                        tempo_suficiente = pessoa.Cliente.cnh_comTsuf(cliente_atual)
                        if cnh_pveic == True and tempo_suficiente == True:
                            dias_loc = verificacoes.escolhaNumerica(0,20,"Informe a quantia de dias que deseja realizar a locação: ")
                            custo_locação = locacao.Locacao.setvalor_loc(carro_locacao, dias_loc)
                            print(f"Valor da locação: {custo_locação}")
                            continuar_pagamento = verificacoes.escolhaNumerica(1, 2, "Continuar para pagamento(1 - Sim, 2 - Não)")
                            if continuar_pagamento == 1:
                                print("Indo para pagamento!!")
                                while True:
                                    pagamento_cliente = pagamento.Pagamento.setDadosPagamento(cliente_atual)
                                    pagamento_realizado = pagamento.Pagamento.realizaPagamento(cliente_atual, pagamento_cliente)
                                    if pagamento_realizado == True:
                                        valor_locacao = locacao.Locacao.setvalor_loc(carro_locacao, dias_loc)
                                        locacao.Locacao.criarLocacao(cliente_atual, carro_locacao, valor_locacao, dias_loc, lista_locacoes)
                                        break
                                    else:
                                        print("Dados não coinsidem com a conta associada!")
                                        tentar_nov = verificacoes.escolhaNumerica(1, 2, "Continuar para pagamento(1 - Sim, 2 - Não)")
                                        if tentar_nov == 2:
                                            break
                                        print()
                                else:
                                    break
                            else:
                                break

                        else:
                            print("Locação não realizada!")


                    else:
                        break

                if escolha_cliente == 2:
                    opcoes = 0
                    bool_loca = False
                    locacaoporescolha = {}
                    for loca in lista_locacoes:
                        print()
                        if loca.pessoa.nome == cliente_atual.nome and loca.pessoa.cpf == cliente_atual.cpf:
                            opcoes += 1
                            print(opcoes, end=' - ')
                            if isinstance(loca.veiculo, Veiculos.Carro):
                                loca.veiculo.Cliente_consulta_Carro()
                                locacaoporescolha[loca.veiculo.placa] = loca
                    escolha = int(input("Informe qual veiculo deseja alterar: "))-1
                    locacao_alterar = None
                    for opcoes, locacao_ in locacaoporescolha.items():
                        print()
                        if opcoes == escolha:
                            locacao_alterar = locacao_
                    
                    alteracao = input("1 - Extender locacão, 2 - Diminuir locação")
                    dias = int(input("Quantos dias deseja diminuir ou extender?"))
                    print(locacao_alterar)
                    if locacao_alterar is not None:
                        alteracao = int(input("1 - Extender locação, 2 - Diminuir locação: "))
                        dias = int(input("Quantos dias deseja diminuir ou estender?"))

                        if alteracao == 1:
                            locacao_alterar.extenderLocacao(dias)
                        else:
                            locacao_alterar.reduzLocacao(dias)
                    else:
                        print("Escolha inválida.")

                if escolha_cliente == 3:
                    cliente_atual.getAtributos()
                    print("Deseja alterar algum dado?(1 - Sim, 2 - Não)")
                    print("1 - Categoria CNH")
                    print("2 - Senha")
                    print("3 - Nenhum")
                    escolha = int(input())
                    if escolha == 1:
                        cliente_atual.set_categria_cnh()
                    elif escolha == 2:
                        cliente_atual.set_senha(input("Nova senha: "))
                    else:
                        break
                if escolha_cliente == 4:
                    break
        if cliente_cadastrado == 2:
            novo_cliente = pessoa.Cliente.criarCliente()
            lista_cliente.append(novo_cliente)
    elif escolha == 2:
            print("Bem-vindo funcionário!")
            funcionario_atual = verificacoes.estanaLinsta(lista_funcionarios)

            while True:
                print("1 - Visualizar locações")
                print("2 - Adicionar veículo")
                print("3 - Remover veículo")
                print("4 - Consultar clientes")
                print("5 - Finalizar locações")
                print("6 - Consultar veículos")
                print("Outro -  Sair")
                escolha_func = int(input())
                if escolha_func == 1:
                    locacao.Locacao.consultarLocacoes(lista_locacoes)
                elif escolha_func == 2:
                    Veiculos.Veiculo.addVeiculo(lista_veiculos)
                elif escolha_func == 3:
                    for veiculo in lista_veiculos:
                        if isinstance(veiculo, Veiculos.Carro):
                            veiculo.Cliente_consulta_Carro()
                        else:
                            veiculo.Cliente_consulta_Motos()
                        print()
                    placa = input("Placa do veículo: ")
                    Veiculos.Veiculo.removerVeic(lista_veiculos, placa)
                elif escolha_func == 4:
                    for cliente in lista_cliente:
                        cliente.getAtributos()
                elif escolha_func == 5:
                    locacao.Locacao.finalizaLocacao(lista_locacoes)
                elif escolha_func == 6:
                    for veiculo in lista_veiculos:
                        if isinstance(veiculo, Veiculos.Carro):
                            print("Carro")
                            veiculo.Cliente_consulta_Carro()
                        elif isinstance(veiculo, Veiculos.Moto):
                            print("Moto")
                            veiculo.Cliente_consulta_Motos()
                        print()
                else:
                    break

