num=-1
par=[]
impar=[]
def imprimir(vector):
    for i in range(len(vector)):
        print(vector[i])
while( num!=0):
    num=int(input('ingrese un numero: '))
    if num %2 ==0:
        par.append(num)
    else:
        impar.append(num)
print('Los numeros impares son')
imprimir(impar)
print('Los numeros pares son')
imprimir(par)