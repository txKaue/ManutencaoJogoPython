class Player:

    def __init__(self, nome):
        self.nome = nome
        self.local = "floresta"
        self.inventario = []

    def __str__(self):
        return f"{self.nome}\nInventário: {self.inventario}"

    def getLocal(self):
        return self.local
    
    def setLocal(self, local):
        self.local = local

    def addItem(self, item):
        self.inventario.append(item)

    def temItem(self, item):
        if item in self.inventario:
            return True
        else:
            False
    
    # função interna
    def findItem(self, item):
        if item in self.inventario:
            return self.inventario.index(item)
        else:
            return None
    
    def removeItem(self, item):
        if self.findItem(item) != None:
            self.inventario.pop(self.findItem(item))