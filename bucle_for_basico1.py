#1.- Básico: imprime todos los números enteros del 0 al 100.
num1 = range(0,101)
for i in num1:
    print(i)
#2.- Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
num2 = range(2,501,2)
for i in num2:
    print(i)
#3.- Contando Vanilla Ice: imprime los números enteros del 1 al 100. 
# Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
num3 = range(1,101)
for i in num3:      #asumi que con los numeros divisibles por 10 solo se imprime "baby" y no "ice ice"
    if i%10 == 0:
        print("baby")
    elif i%5 ==0:
        print("ice ice")
    else:
        print(i)

#4.- Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. 
# (Sorpresa, será un número gigante).
num4 = range(0,500_000,2)
print(sum(num4))
#5.- Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
num5 = 2024
while num5 > 0:
    print(num5)
    num5 -= 3
#6.- Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. 
# Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. 
# Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 
# (en líneas sucesivas).
numInicial = 15
numFinal = 2800
multiplo = 50
multiploaux = multiplo
while multiplo <= numFinal and multiplo >= numInicial:
    print(multiplo)
    multiplo += multiploaux
