class User:
    def __init__(self,user,senha):
        self.user = user
        self.senha = senha
    
    def __user__(self):
        return self.user
    
    def __senha__(self):
        return self.senha
    
    def __setuser__(self):
        return self.user
    
    def __setsenha__(self):
        return self.senha

class Cliente(User):
    def __init__(self,user,senha):
        super().__init__(user,senha)
    
    def consultarNoticias(self):
        pass
    
    def escolherFiltros(self):
        pass
    
    def escolherNoticia(self):
        pass

class Jornalista(User):
    def __init__(self,user,senha):
        super().__init__(user,senha)
    
    def escreverNoticia(self):
        pass
        
    def excluirNoticia(self):
        pass

lista_clientes = [Cliente('Pedro','123456'),Cliente('Maria','123456'),Cliente('João','123456')]
lista_jornalistas = [Jornalista('José','123456'),Jornalista('Carlos','123456'),Jornalista('Ana','123456')]