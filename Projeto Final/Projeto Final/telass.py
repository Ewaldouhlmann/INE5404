from tkinter import *
from tkinter import ttk, messagebox
from cliente import Cliente
from projetos import Projetos
from tarefas import Tarefa

class Tela:
    def __init__(self, botoes, labels, entradas):
        self.janela = None
        self.botoes = botoes
        self.labels = labels
        self.entradas = entradas

    def iniciar_botoes(self):
        for botao in self.botoes:
            botao.criar(self.janela)

    def iniciar_labels(self):
        for label in self.labels:
            label.criar(self.janela)

    def iniciar_entradas(self):
        for entrada in self.entradas:
            entrada.criar(self.janela)

class Botao:
    def __init__(self, texto, relx, rely, comando=None, width=None, bg=None, fg=None):
        self.texto = texto
        self.relx = relx
        self.rely = rely
        self.comando = comando
        self.width = width
        self.bg = bg
        self.fg = fg

    def criar(self, janela):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5, background=self.bg, foreground=self.fg)

        botao = ttk.Button(janela, text=self.texto, command=self.comando, width=self.width, style='TButton')
        botao.place(relx=self.relx, rely=self.rely, anchor='center')
        return botao

class LabelElemento:
    def __init__(self, texto, relx, rely, width=None, height=None, bg=None, fg=None,font=None):
        self.texto = texto
        self.relx = relx
        self.rely = rely
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.font = font

    def criar(self, janela):
        style = ttk.Style()
        if self.font != None:
            style.configure('TLabel', font=self.font, padding=5, background=self.bg, foreground=self.fg)
        else:
            style.configure('TLabel', font=('Arial', 12), padding=5, background=self.bg, foreground=self.fg)

        label_frame = Frame(janela, bg=self.bg)
        label_frame.place(relx=self.relx, rely=self.rely)

        label = ttk.Label(label_frame, text=self.texto, width=self.width, style='TLabel')
        label.pack(side=LEFT, padx=5)

        # Adicione um espaço vazio para controlar a altura
        empty_space = Label(label_frame, height=self.height, bg=self.bg)
        empty_space.pack(side=LEFT)

        return label



class EntradaElemento:
    def __init__(self, relx, rely, width=None, bg=None, fg=None, placeholder=None, show=None):
        self.relx = relx
        self.rely = rely
        self.width = width
        self.bg = bg
        self.fg = fg
        self.placeholder = placeholder
        self.show = show
        self.entrada = None  # Inicialize com None

    def criar(self, janela):
        style = ttk.Style()
        style.configure('TEntry', font=('Arial', 12), padding=5, background=self.bg, foreground=self.fg)

        entry_var = StringVar()
        entry = ttk.Entry(janela, textvariable=entry_var, width=self.width, style='TEntry', show=self.show)

        if self.placeholder:
            entry.insert(0, self.placeholder)
            entry.bind("<FocusIn>", lambda event, var=entry_var: self.clear_placeholder(event, var))
            entry.bind("<FocusOut>", lambda event, var=entry_var: self.restore_placeholder(event, var))

        entry.place(relx=self.relx, rely=self.rely)

        # Atribua a entrada ao atributo de instância
        self.entrada = entry
        
        return entry, entry_var

    def clear_placeholder(self, event, var):
        if var.get() == self.placeholder:
            var.set("")

    def restore_placeholder(self, event, var):
        if not var.get():
            var.set(self.placeholder)

class TelaInicio(Tela):
    def __init__(self):
        super().__init__([
            Botao("Entrar", 0.3, 0.8, self.entrar, width=8, bg="#4CAF50", fg="#000000"),
            Botao("Cadastrar", 0.5, 0.8, self.cadastrar, width=8, bg="#2196F3", fg="#000000"),
            Botao("Sair", 0.7, 0.8, self.sair, width=8, bg="#F44336", fg="#000000")
        ],[
            LabelElemento("User:", 0.2, 0.4, width=6, bg="#B0E57C", fg="#333333"),
            LabelElemento("Senha:", 0.2, 0.5, width=6, bg="#B0E57C", fg="#333333")
        ],[
            EntradaElemento(0.4, 0.4, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.5, width=30, bg="#FFFFFF", fg="#333333", show="*")
        ])
        self.resultados = {}

    def iniciar_tela(self):
        self.janela = Tk()
        self.janela.title("Kanban - Tela de Início")
        self.janela.geometry("500x500")
        self.janela.resizable(True, True)
        self.janela.minsize(300, 300)
        self.janela.configure(bg="#f0f0f0")

        self.iniciar_botoes()
        self.iniciar_labels()
        self.iniciar_entradas()

        self.janela.mainloop()
        return self.resultados
    
    def entrar(self):
        
        username = self.entradas[0].entrada.get()
        senha = self.entradas[1].entrada.get()
        if username == "" or senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            self.resultados["username"] = username
            self.resultados["senha"] = senha
            self.resultados["proxtela"] = 'projetos'
            self.janela.destroy()
        

    def cadastrar(self):
        self.resultados["proxtela"] = 'cadastro'
        self.janela.destroy()

    def sair(self):
        # Você pode retornar os resultados ou fazer outras operações necessárias aqui
        self.resultados["proxtela"] = 'sair'
        self.janela.destroy()

class TelaCadastro(Tela):
    def __init__(self):
        super().__init__([
            Botao("Cadastrar", 0.5, 0.8, self.cadastrar, width=8, bg="#2196F3", fg="#000000"),
            Botao("Voltar", 0.7, 0.8, self.voltar, width=8, bg="#F44336", fg="#000000")
        ],[
            LabelElemento("Nome:", 0.2, 0.1, width=8, bg="#B0E57C", fg="#333333"),
            LabelElemento("Email:", 0.2, 0.2, width=8, bg="#B0E57C", fg="#333333"),
            LabelElemento("Username:", 0.2, 0.3, width=8, bg="#B0E57C", fg="#333333"),
            LabelElemento("Telefone:", 0.2, 0.4, width=8, bg="#B0E57C", fg="#333333"),
            LabelElemento("Senha:", 0.2, 0.5, width=8, bg="#B0E57C", fg="#333333"),
            LabelElemento("Confirmar Senha:", 0.2, 0.6, width=8, bg="#B0E57C", fg="#333333")
        ],[
            EntradaElemento(0.4, 0.1, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.2, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.3, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.4, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.5, width=30, bg="#FFFFFF", fg="#333333", show="*"),
            EntradaElemento(0.4, 0.6, width=30, bg="#FFFFFF", fg="#333333", show="*")
        ])
        self.resultados = {}

    def cadastrar(self):
        nome = self.entradas[0].entrada.get()
        email = self.entradas[1].entrada.get()
        username = self.entradas[2].entrada.get()
        telefone = self.entradas[3].entrada.get()
        telefone = telefone.replace(" ", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")

        senha = self.entradas[4].entrada.get()
        confirmar_senha = self.entradas[5].entrada.get()
        if nome == "" or email == "" or username == "" or telefone == "" or senha == "" or confirmar_senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            self.resultados["nome"] = nome
            self.resultados["email"] = email
            self.resultados["username"] = username
            self.resultados["telefone"] = telefone
            self.resultados["senha"] = senha
            self.resultados["proxtela"] = 'projetos'
            self.resultados["confirmar_senha"] = confirmar_senha
            self.janela.destroy()
    
    def voltar(self):
        self.resultados["proxtela"] = 'voltar'
        self.janela.destroy()

    def iniciar_tela(self):
        self.janela = Tk()
        self.janela.title("Kanban - Tela de Cadastro")
        self.janela.geometry("500x500")
        self.janela.resizable(True, True)
        self.janela.minsize(300, 300)
        self.janela.configure(bg="#f0f0f0")

        self.iniciar_botoes()
        self.iniciar_labels()
        self.iniciar_entradas()

        self.janela.mainloop()
        return self.resultados
def usuarionaoencontrado():
    messagebox.showerror("Erro", "Usuario não encontrado")


def msgerror(msg):
    messagebox.showerror("Erro", msg)

class ProjetoFrame(Frame):
    def __init__(self, master, projeto, abrir_callback, excluir_callback,relx=0.5, rely=0.5):
        super().__init__(master, bg=projeto.cor, padx=10, pady=10, width=500, height=100, relief=SOLID, bd=1)

        Label(self, text=f"{projeto.titulo}:", font=("Arial", 12), bg=projeto.cor, fg="#000000").grid(row=0, column=0, columnspan=2, pady=(0, 5))
        Label(self, text=projeto.descricao, font=("Arial", 10), bg=projeto.cor, fg="#000000").grid(row=1, column=0, columnspan=2, pady=(0, 10))

        Button(self, text=f"Abrir Projeto", command=abrir_callback, width=15, bg="#2ecc71", fg="#000000").grid(row=2, column=0, pady=(10, 5), padx=(0, 5))
        Button(self, text=f"Excluir Projeto", command=excluir_callback, width=15, bg="#e74c3c", fg="#ffffff").grid(row=2, column=1, pady=(10, 5), padx=(5, 0))

class TelaProjetos(Tela):
    def __init__(self, usuario):
        super().__init__([], [], [])
        self.usuario = usuario

        # Elementos da tela
        super().__init__(
            [
                Botao("Criar Projeto", 0.5, 0.4, self.criar_projeto, width=15, bg="#55aacc", fg="#ffffff"),
                Botao("Sair", 0.9, 0.05, self.sair, width=8, bg="#cc5555", fg="#ffffff")
            ],
            [
                LabelElemento(f"Bem-vindo, {usuario.nome}!", 0.1, 0.08, width=30, height=2, bg="#55aacc", fg="#ffffff"),
                LabelElemento("Seus Projetos", 0.5, 0.6, width=150, height=2, bg="#55aacc", fg="#ffffff")
            ],
            []
        )
        self.resultados = {}

    def criar_projeto(self):
        self.resultados["proxtela"] = 'criar_projeto'
        self.janela.destroy()

    def abrir_projeto(self, projeto):
        # Lógica para abrir o projeto
        self.resultados["proxtela"] = 'abrir_projeto'
        self.resultados["projeto_selecionado"] = projeto
        self.janela.destroy()

    def excluir_projeto(self, projeto):
        # Lógica para excluir o projeto
        self.resultados["proxtela"] = 'excluir_projeto'
        self.resultados["projeto_selecionado"] = projeto
        #msg confirmação
        if messagebox.askokcancel("Confirmação", "Tem certeza que deseja excluir o projeto?"):
            print("verdade")
            
        self.janela.destroy()

    def sair(self):
        self.resultados["proxtela"] = 'sair'
        self.janela.destroy()

    def iniciar_tela(self):
        self.janela = Tk()
        self.janela.title("Kanban - Tela de Projetos")
        self.janela.geometry("800x600")
        self.janela.resizable(True, True)
        self.janela.minsize(600, 400)
        self.janela.configure(bg="#55aacc")

        self.iniciar_botoes()
        self.iniciar_labels()
        self.iniciar_entradas()

        # Adicionar Label "Seus Projetos"
        
        # Adicionar frames de projeto lado a lado
        if len(self.usuario.dicprojetos) == 0:
            Label(self.janela, text="Você não possui projetos!!", font=("Arial", 25), bg="#55aacc", fg="#ffffff").place(relx=0.5, rely=0.8, anchor='center')

        else:
            x = 0.2
            y = 0.8
            for projeto_nome, projeto in self.usuario.dicprojetos.items():
                print(projeto)
                projeto_atual = Projetos(projeto.gettitulo(), projeto.getdescricao(), projeto.getbackground(),{})
                print(projeto_atual, projeto_nome)
                projeto_frame = ProjetoFrame(
                    self.janela,
                    projeto,  # This might be an instance of Projetos class
                    abrir_callback=lambda p=projeto_nome: self.abrir_projeto(p),
                    excluir_callback=lambda p=projeto_nome: self.excluir_projeto(p)  # Removed the unnecessary parentheses
                )
                projeto_frame.place(relx=x, rely=y, anchor='center')

                x += 0.35

        self.janela.mainloop()
        return self.resultados

class TelaNovoProjeto(Tela):
    def __init__(self):

        super().__init__(
            [
                Botao("Criar", 0.5, 0.8, self.criar, width=8, bg="#55aacc", fg="#ffffff"),
                Botao("Voltar", 0.7, 0.8, self.voltar, width=8, bg="#cc5555", fg="#ffffff")
            ],
            [
                LabelElemento("Titulo:", 0.1, 0.1, width=12, bg="#55aacc", fg="#ffffff"),
                LabelElemento("Descrição:", 0.1, 0.3, width=12, bg="#55aacc", fg="#ffffff"),
                LabelElemento("Cor de Fundo:", 0.1, 0.5, width=12, bg="#55aacc", fg="#ffffff")
            ],
            [
                EntradaElemento(0.4, 0.1, width=30, bg="#FFFFFF", fg="#333333"),
                EntradaElemento(0.4, 0.3, width=30, bg="#FFFFFF", fg="#333333")
            ]
        )
        self.resultados = {}
    
    def iniciar_tela(self,cliente):
        self.janela = Tk()
        self.janela.title("Kanban - Tela de Novo Projeto")
        self.janela.geometry("500x500")
        self.janela.resizable(True, True)
        self.janela.minsize(300, 300)
        self.janela.configure(bg="#55aacc")

        self.iniciar_botoes()
        self.iniciar_labels()
        self.iniciar_entradas()
        cores = ["Branco", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Roxo", "Laranja", "Cinza"]
        combo_cor = ttk.Combobox(self.janela, values=cores, state="readonly")
        combo_cor.place(relx=0.4, rely=0.5)
        if len(cliente.dicprojetos) >= 3:
            messagebox.showerror("Você já possui 3 projetos, por favor exclua um para criar outro")
        self.janela.mainloop()
        return self.resultados
    
    def criar(self):
        titulo = self.entradas[0].entrada.get()
        descricao = self.entradas[1].entrada.get()

        # Obtém a cor selecionada em português
        cor_pt = self.janela.children['!combobox'].get()

        # Mapeia a cor para inglês usando o dicionário
        mapeamento_cores = {
            "Branco": "white",
            "Vermelho": "red",
            "Verde": "green",
            "Azul": "blue",
            "Amarelo": "yellow",
            "Rosa": "pink",
            "Roxo": "purple",
            "Laranja": "orange",
            "Cinza": "gray"
        }
        cor_en = mapeamento_cores.get(cor_pt, "")  # Se a cor não for encontrada, padrão para Branco
        if titulo == "" or descricao == "" or cor_en == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            print(titulo, descricao, cor_en)
            self.resultados["titulo"] = titulo
            self.resultados["descricao"] = descricao
            self.resultados["background"] = cor_en
            self.resultados["proxtela"] = 'projetos'
            self.janela.destroy()

        

    def voltar(self):
        pass


class KanBan(Tela):
    def __init__(self, projeto):
        super().__init__([],[],[])
        self.projeto = projeto
        self.resultados = {}
        self.janela = None

    def iniciar_tela(self):
        self.janela = Tk()
        print(self.projeto.titulo)
        self.janela.title(f"Kanban - Tela de {self.projeto.titulo}")
        self.janela.geometry("800x500")  # Increased width for three columns
        self.janela.resizable(True, True)
        self.janela.minsize(300, 300)
        self.janela.configure(bg="#55aacc")

        self.iniciar_botoes()

        # Display the project title at the top
        label_title = Label(self.janela, text=f"{self.projeto.titulo}", bg="#55aacc", fg="white", font=("Arial", 20, "bold"))
        label_title.pack(pady=5, padx=2)

        # Create three frames with different colors
        frame_blue = Frame(self.janela, bg="#87CEEB", width=800 / 3, height=500 * 0.8)
        frame_yellow = Frame(self.janela, bg="#FFFFE0", width=800 / 3, height=500 * 0.8)
        frame_red = Frame(self.janela, bg="#FF6347", width=800 / 3, height=500 * 0.8)

        # Place the frames below the title
        frame_blue.pack(side="left", expand=True, fill="both", padx=15)
        frame_yellow.pack(side="left", expand=True, fill="both", padx=5)
        frame_red.pack(side="left", expand=True, fill="both", padx=5)
        labeltodo = Label(frame_blue, text="To Do", bg="#87CEEB", fg="black", font=("Arial", 20, "bold"))
        labeltodo.pack(pady=5, padx=2)

        labelinprogress = Label(frame_yellow, text="In Progress", bg="#FFFFE0", fg="black", font=("Arial", 20, "bold"))
        labelinprogress.pack(pady=5, padx=2)

        labeldone = Label(frame_red, text="Done", bg="#FF6347", fg="black", font=("Arial", 20, "bold"))
        labeldone.pack(pady=5, padx=2)
        
        #Button to add a new task
        botaoadd = Button(self.janela, text="Adicionar Tarefa", command= lambda: self.add_tarefa(), width=15, bg="#55aacc", fg="#ffffff")
        botaoadd.place(relx=0.5, rely=0.9, anchor='center')

        #botao voltar
        botaoback = Button(self.janela, text="Voltar", command= lambda: self.voltar(), width=15, bg="#55aacc", fg="#ffffff")
        botaoback.place(relx=0.9, rely=0.05, anchor='center')
        # Display tasks in each frame
        self.exibir_tarefas(frame_blue, "To Do")
        self.exibir_tarefas(frame_yellow, "In Progress")
        self.exibir_tarefas(frame_red, "Done")

        self.janela.mainloop()
        return self.resultados
    
    def refresh_gui(self):
    # Destroy the current window and recreate it with updated tasks
        self.janela.destroy()
        self.iniciar_tela()

    def exibir_tarefas(self, frame, status):
        # Get tasks based on their status
        print(self.projeto.tarefas)
        lista_tarefas = self.projeto.tarefas
        print(lista_tarefas)
        tasks = [tarefa for tarefa in lista_tarefas if tarefa.get_status().lower() == status.lower()]

        # Display tasks in the frame
        for idx, tarefa in enumerate(tasks):
            # Create a frame for each task
            task_frame = Frame(frame, bg=frame["bg"], width=200, height=50)
            task_frame.pack(pady=5)

            # Display task details in the task frame
            label_task = Label(task_frame, text=f"{tarefa.get_titulo()}\n{tarefa.get_descricao()}", bg=frame["bg"], fg="black", font=("Arial", 12))
            label_task.pack(pady=5)

            # Add a button to move the task to the next phase
            button_move = Button(task_frame, text="Mover para a próxima fase", command=lambda t=tarefa, s=status: self.move_task_to_next_status(t, s))
            button_move.pack(pady=5)

    def move_task_to_next_status(self, task, current_status):
        status_order = ["To Do", "In Progress", "Done"]
        if current_status == "Done":
            next_status = "To Do"
        else:
            current_status_index = status_order.index(current_status)
            next_status = status_order[current_status_index + 1]
        print(next_status)
        
        #atualizar o status da tarefa
        task.set_status(next_status)
        
        print(task.get_status())

        #atualizar o status da tarefa no projeto
        self.refresh_gui()
    def add_tarefa(self):
        self.resultados["proxtela"] = 'add_tarefa'
        self.janela.destroy()
    def voltar(self):
        self.resultados["proxtela"] = 'voltar'
        self.janela.destroy()



class TelaNovaTarefa(Tela):
    def __init__(self):
        super().__init__([
            Botao("Confirmar", 0.3, 0.8, self.adicionar, width=8, bg="#2196F3", fg="#000000"),
            Botao("Voltar", 0.7, 0.8, self.voltar, width=8, bg="#F44336", fg="#000000")
        ],[
            LabelElemento("Titulo:", 0.2, 0.1, width=7, bg="#B0E57C", fg="#333333"),
            LabelElemento("Descricao:", 0.2, 0.2, width=7, bg="#B0E57C", fg="#333333"),
            LabelElemento("Status:", 0.2, 0.3, width=7, bg="#B0E57C", fg="#333333"),
        ],[
            EntradaElemento(0.4, 0.1, width=30, bg="#FFFFFF", fg="#333333"),
            EntradaElemento(0.4, 0.2, width=30, bg="#FFFFFF", fg="#333333"),
        ])
        self.resultados = {}

    def adicionar(self):
        titulo = self.entradas[0].entrada.get()
        descricao = self.entradas[1].entrada.get()
        status = self.janela.children['!combobox'].get()

        if titulo == "" or descricao == "" or status == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            self.resultados["titulo"] = titulo
            self.resultados["descricao"] = descricao
            self.resultados["status"] = status
            self.janela.destroy()
    
    def voltar(self):
        self.resultados["proxtela"] = 'voltar'
        self.janela.destroy()

    def iniciar_tela(self):
        self.janela = Tk()
        self.janela.title("Kanban - Tela de Cadastro")
        self.janela.geometry("500x500")
        self.janela.resizable(True, True)
        self.janela.minsize(300, 300)
        self.janela.configure(bg="#f0f0f0")
        combobox = ttk.Combobox(self.janela, values=["To Do", "In Progress", "Done"], state="readonly")
        combobox.place(relx=0.4, rely=0.3)
        self.iniciar_botoes()
        self.iniciar_labels()
        self.iniciar_entradas()

        self.janela.mainloop()
        return self.resultados
