from sistema import Sistema
from telass import TelaInicio, usuarionaoencontrado, TelaCadastro, msgerror, TelaProjetos, TelaNovoProjeto, KanBan, TelaNovaTarefa
from cliente import Cliente
from tkinter import *
from projetos import Projetos
from tarefas import Tarefa

sis = Sistema({}, [])
sis.iniciarsistema()
sis.iniciarTelas()
for tela in sis.telas:
    print(tela)
while True:
    flag_sair = False
    tela_inicio = TelaInicio()
    saida_telalogin = tela_inicio.iniciar_tela()
    print(saida_telalogin)
    if saida_telalogin == {} or saida_telalogin['proxtela'] == 'sair':
        break
    if saida_telalogin['proxtela'] == 'cadastro':
        while True:
            tela_cadastro = TelaCadastro()
            saida_cadastro = tela_cadastro.iniciar_tela()

            if saida_cadastro['proxtela'] == 'voltar':
                break
            else:
                verificacao = sis.verificaNewUser(saida_cadastro)
                print(verificacao)
                if verificacao == True:
                    novocliente = sis.cadastroCliente(saida_cadastro['nome'], saida_cadastro['email'], saida_cadastro['username'], saida_cadastro['telefone'], saida_cadastro['senha'])
                    print(novocliente.nome)
                
                else:
                    msgerror(verificacao)

    elif saida_telalogin['proxtela'] == 'projetos':
        user = saida_telalogin['username']
        senha = saida_telalogin['senha']
        cliente = sis.getUsuario(user, senha)
        #Vrf se o usuario existe
        if cliente == False:
            print("Usuario não encontrado")
            usuarionaoencontrado()
        else:
            print(f"Usuario {cliente.getnome()} logado com sucesso")
            usuario_atual = Cliente(cliente.getnome(), cliente.getemail(), cliente.getusername(), cliente.gettelefone(), cliente.getsenha(), cliente.getprojetos())
            #Pega o usuario e manda para a tela do projeto dele
            while True:
                tela_projetos = TelaProjetos(usuario_atual)
                saida_projetos = tela_projetos.iniciar_tela()
                print(saida_projetos)
                if saida_projetos == {} or saida_projetos['proxtela'] == 'sair':
                    flag_sair = True
                    break
                #Vai para a tela para criar um projeto
                elif saida_projetos['proxtela'] == 'criar_projeto':
                    novo_proj = TelaNovoProjeto()
                    out_projeto = novo_proj.iniciar_tela(usuario_atual)
                    if out_projeto == {} or out_projeto['proxtela'] == 'voltar':
                        break
                    else:
                        novo_proj = Projetos(out_projeto['titulo'], out_projeto['descricao'], out_projeto['background'], [])
                        usuario_atual.addProjeto(novo_proj)
                        print("Projeto criado")
                        print(novo_proj.gettitulo())
                #Vai para a tela para excluir um projeto
                elif saida_projetos['proxtela'] == 'excluir_projeto':
                    titulo = saida_projetos['projeto_selecionado']
                    usuario_atual.removeProjeto(titulo)
                    print("Projeto excluido")
                #Vai para o projeto Kanban
                elif saida_projetos['proxtela'] == 'abrir_projeto':
                    projeto = saida_projetos['projeto_selecionado']
                    projeto_atual = usuario_atual.getProjeto(projeto)
                    print(projeto_atual.gettitulo())
                    #receber o projeto na saida de projeto selecionado

                    while True:
                        print("Abrir projeto")
                        tela_kanban = KanBan(projeto_atual)
                        saida_kanban = tela_kanban.iniciar_tela()
                        print(saida_kanban)
                        if saida_kanban == {}:
                            flag_sair = True
                            break
                        elif saida_kanban['proxtela'] == 'voltar':
                            break
                        elif saida_kanban['proxtela'] == 'add_tarefa':
                            print("Criar tarefa")
                            tela_atual = TelaNovaTarefa()
                            saida_tarefa = tela_atual.iniciar_tela()
                            titulo = saida_tarefa['titulo']
                            descricao = saida_tarefa['descricao']
                            status = saida_tarefa['status']
                            task = Tarefa(titulo, descricao, status)    
                            projeto_atual.addTarefa(task)
                            print("Tarefa criada")
                        projeto_atual.gettarefas()

                else:
                    print("Sair")
                    break
                if flag_sair == True:
                    break
        if flag_sair == True:
            break
    
    
    if flag_sair == True:
        break
    else:
        print("Error")