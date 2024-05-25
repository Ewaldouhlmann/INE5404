from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from clientes import Cliente, lista_clientes, lista_jornalistas, Jornalista, User
from blog import Blog
from datetime import datetime
from noticias import Noticias

def fazer_login(blog):
    resultado = {'user': None, 'senha': None}
    sair_loop = False  # Variável de controle para sair do loop

    def buttonsync():
        nonlocal resultado, sair_loop
        usuario = user.get()
        password = senha.get()
        if usuario == '' or password == '':
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos!')
        else:
            resultado = {'user': usuario, 'senha': password}
            janela_login.destroy()

    def sair():
        nonlocal sair_loop
        sair_loop = True
        janela_login.destroy()

    janela_login = Tk()
    janela_login.title("Login")
    janela_login.geometry("400x200")

    janela_user = Frame(janela_login, bg="#F0F0F0")
    janela_user.pack(pady=10)

    txt_nome = Label(janela_user, text='Usuário:', font=('Arial', 12), bg="#F0F0F0")
    txt_nome.grid(row=0, column=0, pady=10)

    user = StringVar()
    entrada_user = Entry(janela_user, textvariable=user)
    entrada_user.grid(row=0, column=1, pady=10, padx=10)

    janela_senha = Frame(janela_login, bg="#F0F0F0")
    janela_senha.pack(pady=10)

    txt_senha = Label(janela_senha, text='Senha:', font=('Arial', 12), bg="#F0F0F0")
    txt_senha.grid(row=0, column=0, pady=10)

    senha = StringVar()
    entrada_senha = Entry(janela_senha, textvariable=senha, show='*')
    entrada_senha.grid(row=0, column=1, pady=10, padx=10)

    botao_frame = Frame(janela_login, bg="#F0F0F0")
    botao_frame.pack()

    botao_login = Button(botao_frame, text='Login', command=buttonsync, bg="#4CAF50", fg="white")
    botao_login.pack(side=LEFT, pady=10, padx=10)

    botao_sair = Button(botao_frame, text='Sair', command=sair, bg="#FF5733", fg="white")
    botao_sair.pack(side=LEFT, pady=10, padx=10)

    botao_cadastro = Button(botao_frame, text='Cadastro', command=lambda: cadastrar(blog), bg="#007BFF", fg="white")
    botao_cadastro.pack(side=LEFT, pady=10, padx=10)

    janela_login.mainloop()
    return resultado['user'], resultado['senha'], sair_loop

def cadastrar(blog):
    user, senha = None, None
    def salvar_cadastro():
        novo_usuario = entry_novo_user.get()
        nova_senha = entry_nova_senha.get()

        messagebox.showinfo('Cadastro', f'Novo usuário: {novo_usuario}\nNova senha: {nova_senha}')
        user = novo_usuario
        senha = nova_senha
        blog.cadastroClient(novo_usuario, nova_senha)
        janela_cadastro.destroy()

    # Cria a janela de cadastro
    janela_cadastro = Tk()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("300x150")

    frame_cadastro = Frame(janela_cadastro, bg="#F0F0F0")
    frame_cadastro.pack(pady=10)

    label_novo_user = Label(frame_cadastro, text='Novo Usuário:', font=('Arial', 12), bg="#F0F0F0")
    label_novo_user.grid(row=0, column=0, pady=5)

    novo_user = StringVar()
    entry_novo_user = Entry(frame_cadastro, textvariable=novo_user)
    entry_novo_user.grid(row=0, column=1, pady=5, padx=10)

    label_nova_senha = Label(frame_cadastro, text='Nova Senha:', font=('Arial', 12), bg="#F0F0F0")
    label_nova_senha.grid(row=1, column=0, pady=5)

    nova_senha = StringVar()
    entry_nova_senha = Entry(frame_cadastro, textvariable=nova_senha, show='*')
    entry_nova_senha.grid(row=1, column=1, pady=5, padx=10)

    botao_salvar = Button(janela_cadastro, text='Salvar', command=salvar_cadastro, bg="#4CAF50", fg="white")
    botao_salvar.pack(pady=10)

    janela_cadastro.mainloop()
    return user, senha


def tela_pesquisa(user, blog):
    #Tela de pesquisa d
    resultado = {'categoria': None, 'datainicio': None, 'datafim': None}
    flag_sair = False
    def selecionar_categoria(event):
        categoria_selecionada = categoria.get()
        return categoria_selecionada

    def calendario(entrada):
        #Cria um calnedário
        cal = Calendar(
            escolhas,
            fg="black",
            bg="white",
            font=("Times", 4, 'bold'),
            locale='pt_BR',
            showweeknumbers=False
        )
        cal.grid(row=1, column=0, pady=10, sticky="nsew")

        def inserir_data():
            #Insere a data selecionada no campo de entrada
            data_selecionada = cal.get_date()
            entrada.delete(0, END)
            entrada.insert(END, data_selecionada)
            cal.destroy()
            bt_mostrar_cal.destroy() 

        bt_mostrar_cal = Button(escolhas, text="Inserir Data", command=inserir_data, bg="#007BFF", fg="white")
        bt_mostrar_cal.grid(row=2, column=0, pady=10)

    def MandarPesquisar(categoria, datainicio, datafim):
        #Retorna categoria e datas para filtrar a pesquisa de noticias
        nonlocal resultado
        categoria = str(categoria.get())
        datainicio = entry_data_inicio.get()
        datafim = entry_data_fim.get()
        #Transformar data em datetime
        print(categoria, datainicio, datafim)
        if datainicio == None or datafim == None or categoria == "Escolha a Categoria":
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos!')
        else:
            datainic_date = datetime.strptime(datainicio, '%d/%m/%Y')
            datafim_date = datetime.strptime(datafim, '%d/%m/%Y')
            diferenca_dias = (datainic_date - datafim_date).days
            if diferenca_dias > 0:
                messagebox.showerror('Erro', 'A data de início não pode ser maior que a data de fim!')
            else:
                resultado = {'categoria': categoria, 'datainicio': datainicio, 'datafim': datafim}
                tela_pesquisa.destroy()

    def sair():
        nonlocal resultado, flag_sair
        resultado = {'categoria': None, 'datainicio': None, 'datafim': None}
        flag_sair = True
        tela_pesquisa.destroy()
    
    tela_pesquisa = Tk()
    tela_pesquisa.title("Bem vindo, " + user.user + "!")
    tela_pesquisa.geometry("800x600")
    tela_pesquisa.configure(bg="#F0F0F0")

    # Escolhas
    escolhas = Frame(tela_pesquisa, bg="#F0F0F0")
    escolhas.pack(pady=10, padx=10, fill="both", expand=True)

    #Tela Bem Vindo
    label_bem_vindo = Label(escolhas, text="Bem vindo, " + user.user + "!", bg="#F0F0F0")
    label_bem_vindo.grid(row=0, column=0, pady=(0, 10), padx=(10, 10), sticky="nsew")

    # Categorias
    categorias = ["Esportes", "Economia", "Política"]
    categoria = ttk.Combobox(escolhas, values=categorias, state="readonly")
    categoria.set("Escolha a Categoria")
    categoria.grid(row=0, column=0, pady=(0, 10), padx=(10, 10), sticky="nsew")
    categoria.bind("<<ComboboxSelected>>", selecionar_categoria)

    # Data Início
    label_data_inicio = Label(escolhas, text="Data Início", bg="#F0F0F0")
    label_data_inicio.grid(row=0, column=1, pady=(0, 10), padx=(0, 10), sticky="nsew")
    entry_data_inicio = Entry(escolhas, width=10)
    entry_data_inicio.grid(row=0, column=2, pady=(0, 10), padx=(0, 10), sticky="nsew")
    bt_calendario_inicio = Button(escolhas, text="Calendário", command=lambda:calendario(entry_data_inicio), bg="#007BFF", fg="white")
    bt_calendario_inicio.grid(row=1, column=1, columnspan=2, pady=(10, 0), padx=(0, 100), sticky="nsew")

    # Data Fim
    label_data_fim = Label(escolhas, text="Data Fim", bg="#F0F0F0")
    label_data_fim.grid(row=0, column=3, pady=(0, 10), padx=(0, 10), sticky="nsew")
    entry_data_fim = Entry(escolhas, width=10)
    entry_data_fim.grid(row=0, column=4, pady=(0, 10), padx=(0, 10), sticky="nsew")
    bt_calendario_fim = Button(escolhas, text="Calendário", command=lambda: calendario(entry_data_fim), bg="#007BFF", fg="white")
    bt_calendario_fim.grid(row=1, column=3, columnspan=2, pady=(10, 0), padx=(0, 100), sticky="nsew")

    # Botão de Busca
    bt_buscar = Button(escolhas, text="Buscar", bg="#28A745", fg="white", command=lambda: MandarPesquisar(categoria, entry_data_inicio, entry_data_fim))
    bt_buscar.grid(row=2, column=4, pady=(10, 0), padx=(0, 100), sticky="nsew")

    # Botão de Sair
    bt_sair = Button(escolhas, text="Sair", bg="#FF5733", fg="white", command=lambda: sair())
    bt_sair.grid(row=2, column=5, pady=(10, 0), padx=(0, 100), sticky="nsew")

    
    tela_pesquisa.mainloop()
    return resultado['categoria'], resultado['datainicio'], resultado['datafim'], flag_sair

def telaResultados(noticias, categoria):
    def voltar():
        telaRes.destroy()
        tela_pesquisa.deiconify()   # Volta para a tela de pesquisa

    telaRes = Tk()
    telaRes.title(f"Resultados - {categoria}")
    telaRes.geometry("800x600")
    telaRes.configure(bg="#F0F0F0")

    # Adiciona uma barra de título
    titulo_label = Label(telaRes, text=f"Resultados - {categoria}", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
    titulo_label.pack(fill=X)

    # Adiciona um widget de texto para exibir os resultados
    txtResult = Text(telaRes, wrap=WORD, bg="#F0F0F0", relief=FLAT, borderwidth=0)
    txtResult.pack(expand=True, fill=BOTH)

    # Adiciona uma barra de rolagem
    barra_rolagem = Scrollbar(telaRes, command=txtResult.yview)
    barra_rolagem.pack(side=RIGHT, fill=Y)
    txtResult.config(yscrollcommand=barra_rolagem.set)

    # Adiciona os resultados ao widget de texto
    if len(noticias) == 0:
        txtResult.insert(END, "Nenhum resultado encontrado.")

    for n in noticias:
        titulo = n.getTitulo()
        data = n.getData()
        descricao = n.getDescricao()
        link = n.getLink()

        # Adiciona as informações ao widget de texto
        if titulo:
            txtResult.insert(END, f"{titulo}\n", "titulo")
        if data:
            txtResult.insert(END, f"{data}\n", "data")
        if descricao:
            txtResult.insert(END, f"{descricao}\n", "descricao")
        if link:
            txtResult.insert(END, f"Link: {link}\n", "link")

        # Adiciona uma linha divisória
        txtResult.insert(END, "\n" + "-"*50 + "\n\n")
        

    # Adiciona a tag de hiperlink
    hyperlink = (txtResult)

    # Configuração das tags para diferentes estilos de fonte
    txtResult.tag_config("titulo", font=("Arial", 14, "bold"), spacing1=5, spacing3=5, foreground="#4CAF50")
    txtResult.tag_config("data", font=("Arial", 10, "italic"), spacing1=3, spacing3=3)
    txtResult.tag_config("descricao", font=("Arial", 12), spacing1=5, spacing3=5)
    txtResult.tag_config("link", font=("Arial", 12, "underline"), foreground="#0066cc")

    # Adiciona a funcionalidade de link clicável
    txtResult.tag_bind("link", "<Button-1>", lambda event, link=n.getLink() if noticias else None: open_link(link, telaRes))

    # Botão para voltar
    btnVoltar = Button(telaRes, text="Voltar", command=voltar, bg="#FF5733", fg="white")
    btnVoltar.pack(pady=10)

    # Inicia o loop principal do Tkinter
    telaRes.mainloop()

# Função para abrir o link no navegador padrão
def open_link(link, root):
    root.destroy()  # Fecha a janela antes de abrir o navegador
    import webbrowser
    webbrowser.open(link)


def telaJornalista(user, blog):
    telaJorn = Tk()
    pesquisar = False
    escrever = False
    sair = False
    
    def tela_pesquisa():
        nonlocal pesquisar
        pesquisar = True
        telaJorn.destroy()
    
    def tela_escrever():
        nonlocal escrever
        escrever = True
        telaJorn.destroy()
    
    def sair():
        nonlocal sair
        sair = True
        telaJorn.destroy()

    telaJorn.title("Bem vindo, " + user.user + "!")
    telaJorn.geometry("800x600")
    telaJorn.configure(bg="#F0F0F0")

    bttPesquisar = Button(telaJorn, text="Pesquisar", command=tela_pesquisa, bg="#007BFF", fg="white")
    bttPesquisar.pack(pady=10)

    bttEscrever = Button(telaJorn, text="Escrever", command=tela_escrever, bg="#007BFF", fg="white")
    bttEscrever.pack(pady=10)

    bttSair = Button(telaJorn, text="Sair", command=sair, bg="#FF5733", fg="white")
    bttSair.pack(pady=10)

    telaJorn.mainloop()
    return pesquisar, escrever, sair

from tkinter import Tk, Label, Entry, Button, messagebox

def TelaEscrever(user, blog):
    def salvar():
        area = entr_area.get()
        titulo = entr_titulo.get()
        descricao = entr_descricao.get()
        link = entr_link.get()

        if not area or not titulo or not descricao or not link:
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos!')
        else:
            blog.novaNoticia(titulo, descricao, link, area)
            messagebox.showinfo('Novo Post', f'Novo Post: {titulo}\nDescrição: {descricao}\nLink: {link}')
            texto.destroy()

    texto = Tk()
    texto.title("Novo Post")
    texto.geometry("600x400")
    texto.configure(bg="#F0F0F0")

    # Labels and Entry Widgets
    label_area = Label(texto, text='Área:', bg="#F0F0F0", font=('Arial', 12))
    label_area.grid(row=0, column=0, pady=10, padx=10, sticky="e")
    entr_area = Entry(texto, width=50, font=('Arial', 12))
    entr_area.grid(row=0, column=1, pady=10, padx=10)

    label_titulo = Label(texto, text='Título:', bg="#F0F0F0", font=('Arial', 12))
    label_titulo.grid(row=1, column=0, pady=10, padx=10, sticky="e")
    entr_titulo = Entry(texto, width=50, font=('Arial', 12))
    entr_titulo.grid(row=1, column=1, pady=10, padx=10)

    label_descricao = Label(texto, text='Descrição:', bg="#F0F0F0", font=('Arial', 12))
    label_descricao.grid(row=2, column=0, pady=10, padx=10, sticky="e")
    entr_descricao = Entry(texto, width=50, font=('Arial', 12))
    entr_descricao.grid(row=2, column=1, pady=10, padx=10)

    label_link = Label(texto, text='Link:', bg="#F0F0F0", font=('Arial', 12))
    label_link.grid(row=3, column=0, pady=10, padx=10, sticky="e")
    entr_link = Entry(texto, width=50, font=('Arial', 12))
    entr_link.grid(row=3, column=1, pady=10, padx=10)

    # Button to Save
    btn_salvar = Button(texto, text="Salvar", command=salvar, bg="#4CAF50", fg="white", font=('Arial', 12))
    btn_salvar.grid(row=4, column=1, pady=20, padx=10)

    texto.mainloop()

# Example usage:
# TelaEscrever(user, blog)


# Chama a função de login e inicializa o programa
while True:
    lista_clientes = lista_clientes
    lista_jornalistas = lista_jornalistas
    b1 = Blog([], lista_clientes, lista_jornalistas)
    b1.iniciarApi()
    b1.addNoticias()
    flag_sair = False
    user, senha, sair = fazer_login(b1)
    if sair == True:
        break
    usuario = b1.verificaLogin(user, senha)
    if isinstance(usuario, Cliente):
        while True:
            categoria, datainicio, datafim, logout = tela_pesquisa(usuario, b1)
            if categoria == "Esportes":
                res_pesquisa = b1.consultarNoticias("Esportes", datainicio, datafim)
                telaResultados(res_pesquisa,"Esportes")
            elif categoria == "Economia":
                res_pesquisa = b1.consultarNoticias("Economia", datainicio, datafim)
                telaResultados(res_pesquisa,"Economia")
            elif categoria == "Política":
                res_pesquisa = b1.consultarNoticias("Política", datainicio, datafim)
                telaResultados(res_pesquisa,"Política")
            elif logout:
                flag_sair = True
                break

    elif isinstance(usuario, Jornalista):
        while True:
            pesquisar, escrever, logout = telaJornalista(usuario,b1)
            if pesquisar == True:
                categoria, datainicio, datafim, logout = tela_pesquisa(usuario, b1)
                if categoria == "Esportes":
                    res_pesquisa = b1.consultarNoticias("Esportes", datainicio, datafim)
                    telaResultados(res_pesquisa,"Esportes")
                elif categoria == "Economia":
                    res_pesquisa = b1.consultarNoticias("Economia", datainicio, datafim)
                    telaResultados(res_pesquisa,"Economia")
                elif categoria == "Política":
                    res_pesquisa = b1.consultarNoticias("Política", datainicio, datafim)
                    telaResultados(res_pesquisa,"Política")
                elif logout:
                    flag_sair = True
                    break
            elif escrever == True:
                print("Escrever")
                TelaEscrever(usuario,b1)
            elif logout:
                flag_sair = True
                break
    if flag_sair:
        break
