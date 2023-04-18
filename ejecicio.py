class Animal:
    def __init__(self, edad, edadMax):
        self.edad=edad
        self.edadMax= edadMax
    def cicloDeVida(self):
        if self.edad< (self.edadMax*0.25):
            print('Joven')
        elif (self.edad >= (self.edadMax*0.25)) and (self.edad< (self.edadMax*0.5)):
            print('Adulto')
        elif (self.edad>= (self.edadMax*0.5)) and (self.edad< (self.edadMax*0.75)):
            print('viejo')
        elif (self.edad>= (self.edadMax*0.75)) and (self.edad< (self.edadMax*0.100)):
            print('Proximo a morir')
        elif self.edad>= (self.edadMax*0.25):
            print('Muerto')

class Terrestre(Animal):
    
    def __init__(self, ibMeses,edad, edadMax):
        super().__init__(edad, edadMax)
        self.ibMeses=ibMeses
        self.mDormidos=0

    def desplazar(self):
            print('El animal anda')

    def ibernar(self):
        if self.ibMeses>0:
            self.ibMeses-=1
            self.mDormidos+=1
            print('ha dormido por', self.mDormidos, 'meses')
            print('faltan', self.ibMeses, 'meses para despertar')
        elif self.ibMeses==0:
            print('el animal esta despierto')

class Acuatico:
    
    def __init__(self,edad, edadMax):
        super().__init__(edad, edadMax)

    def desplazar2(self):
        print('El animal nada')

class Cocodrilo(Terrestre, Acuatico):
    pass

cocodrilin = Cocodrilo(0, 1,10)
print(cocodrilin.cicloDeVida())
