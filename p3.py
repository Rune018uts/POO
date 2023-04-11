class Instrumento:
    def __init__(self, precio):
        self.precio= precio

    
    def tocar(self):
        print('estamos tocando musica')
    
    def romper(self):
        print('eso lo pagas tu')
        print('Son', self.precio, '$$$')

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    def __init__(self, precio, cuerdas):
        super().__init__(precio)
        self.cuerdas=cuerdas

    def estallar(self):
        if self.cuerdas<=0:
            print('no se pueden romper mas cuerdas')
        else:
            self.cuerdas-=1
            print('se ha roto una cuerda, quedan', self.cuerdas, 'cuerdas')

    def reponer(self):
        if self.cuerdas>=6:
            print('no se pueden reponer mas cuerdas')
        else:
            self.cuerdas+=1
            print('se ha reparado una cuerda, tienes', self.cuerdas, 'cuerdas')





print('······················guitarraElectrica······························')

guitarraElectrica= Guitarra(50000, 6)
guitarraElectrica.tocar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.estallar()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
guitarraElectrica.reponer()
