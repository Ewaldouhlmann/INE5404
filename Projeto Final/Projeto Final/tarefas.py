class Tarefa:
    def __init__(self, titulo, descricao, status):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
    
    def get_titulo(self):
        return self.titulo
    
    def get_descricao(self):
        return self.descricao
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
        return self.status
    