class Terrestre:
    def __init__(self, ibMeses):
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
    def desplazar2(self):
        print('El animal nada')

class Cocodrilo(Terrestre, Acuatico):
    pass

# c= Cocodrilo(0)
# c.desplazar()
# c.desplazar2()
# print('·········································')
# ardilla= Terrestre()
# ardilla.desplazar()

oso= Terrestre(3)
oso.ibernar()
oso.ibernar()
oso.ibernar()
oso.ibernar()
oso.ibernar()