class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.color = ''
        self.sonido = ''
        
    def escuchar(self):
        return f'{self.nombre} suena así: {self.sonido}'


class Mamifero(Animal):
    def __init__(self,nombre, patas=4):
        super().__init__(nombre)
        self.num_patas = patas
        
                      

class Ave(Animal):

    def __init__(self, nombre, color_plumas = 'blanco'):
        super().__init(nombre)
        self.plumas = color_plumas
        self.color = color_plumas

class Humano(Mamifero):

    def __init__(self, nombre):
        super().__init__(nombre, 2)
        self.apellido = ''
        self.sonido = 'habla'

