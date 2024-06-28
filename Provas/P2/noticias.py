class Noticias:
    def __init__(self,area, titulo, descricao, data, link):
        self.area = area
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.link = link
    
    def getTitulo(self):
        return self.titulo
    
    def getArea(self):
        return self.area
    
    def getDescricao(self):
        return self.descricao
    
    def getData(self):
        return self.data
    
    def getLink(self):
        return self.link
    
