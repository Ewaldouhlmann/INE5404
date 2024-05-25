class Projetos:
    def __init__(self, titulo, descricao, cor, tarefas):
        self.titulo = titulo
        self.descricao = descricao
        self.cor = cor
        self.tarefas = tarefas

    
    def gettitulo(self):
        return self.titulo

    def getdescricao(self):
        return self.descricao

    def getbackground(self):
        return self.cor

    def gettarefas(self):
        for t in self.tarefas:
            print(t.get_titulo(), t.get_descricao(), t.get_status())
    
    def settitulo(self, titulo):
        self.titulo = titulo
    
    def setdescricao(self, descricao):
        self.descricao = descricao
    
    def setbackground(self, background):
        self.background = background
    
    def addTarefa(self, tarefa):
        self.tarefas.append(tarefa)
