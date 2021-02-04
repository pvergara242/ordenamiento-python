lista = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

def seleccion(lista):
    for i in range(len(lista)-1,0,-1):
        print(lista)
        posicion_mayor = 0
        for j in range(1, i+1):
            if lista[j] > lista[posicion_mayor]:
                posicion_mayor = j
        aux = lista[i]
        lista[i] = lista[posicion_mayor]
        lista[posicion_mayor] = aux


seleccion(lista)
print(lista)