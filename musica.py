class Orquesta:
    
    def __init__(self, nombre=''):
        self.nombre = nombre
        self.componentes = [] # lista de instrumentos: [violin:Instrumento, piano:Instrumento, timbal:Instrumento]

    def agregarInstrumento(self, instrumento):
        if not isinstance(instrumento, Instrumento):
            raise TypeError(f'{instrumento} no es un instrumento válido')
        self.componentes.append(instrumento)

    def listarInstrumentos(self):
        #for instrumento in self.componentes:
        #    print(instrumento)

        # listar por gurpos: cuerdas, vientos, percusión

        cuerda = []
        viento = []
        percusion = []
        resto = []

        for instrumento in self.componentes:
            if isinstance(instrumento, Cuerda):
                cuerda.append(instrumento)
            elif isinstance(instrumento, Viento):
                viento.append(instrumento)
            elif isinstance(instrumento, Percusion):
                percusion.append(instrumento)
            else:
                resto.append(instrumento)

        print('cuerda:', cuerda)
        print('Viento:', viento)
        print('Percusión', percusion)
        print('Otros', resto)

        # ojo: ordenar la lista por el metodo sort self.componentes.sort mirar en la documentación de python


    def interpretar(self, obra=''):
        if len(self.componentes) < 1:
            print(f'No hay instrumentos para interpretar {obra}')
            return
        if obra != '':
            print('-'*60)
            print('\tInterprentando:', obra)
            print('-'*60)

        for instrumento in self.componentes:
            instrumento.sonar()

    def __str__(self):
        resultado = ''
        for instrumento in self.componentes:
            resultado = resultado + ', ' + str(instrumento)
        if len(resultado) > 2:
            return resultado[2:]
        return 'No hay instrumentos'
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sonido = None
        self.cualidad = ''
    def sonar(self):
        if self.sonido:
            print(f'{self.sonido} {self.cualidad} {self.sonido}')
        else:
            print('silencio')
    
    def __str__(self):
        return self.nombre

class Viento(Instrumento):
    

    def sonar(self):
        print('sopla', end=' ')
        super().sonar()

class Percusion(Instrumento):
    def sonar(self):
        print('golpea', end=' ')
        super().sonar()

class Cuerda(Instrumento):
    pass

class Pulsada(Cuerda):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.cualidad = 'con la pua'

    def sonar(self):
        print('con la pua', end=' ')
        super().sonar()

class Frotada(Cuerda):
    def sonar(self):
        print('con el arco', end=' ')
        super().sonar()

class Golpeada(Cuerda):
    def sonar(self):
        print('golpea', end=' ')
        super().sonar()

if __name__ == '__main__':
    orquesta = Orquesta()
    piano = Golpeada('primer piano')
    piano.sonido = 'pin pin pin'
    violin = Frotada('violín 1')
    violin.sonido = 'flic flic flic'
    vn = Frotada('violín 2')
    vn.sonido = 'flac flac flac'
    timbal = Percusion('timbal principal')
    timbal.sonido = 'pum pum pum'
    fagot = Viento('fagot alto')
    fagot.sonido = 'fiw fiu fiu'
    pulsada = Pulsada('guitarra')
    pulsada.sonido ='clin clin clin'

    orquesta.agregarInstrumento(piano)
    orquesta.agregarInstrumento(violin)
    orquesta.componentes.append(vn)
    orquesta.componentes.append(timbal)
    orquesta.componentes.append(fagot)
    orquesta.agregarInstrumento(pulsada)

    orquesta.listarInstrumentos()

    #orquesta.interpretar('El cascanueces')



    print('='*80)
    print(orquesta)