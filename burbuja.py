lista = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]


def burbuja(lista):#creo la funcion y paso la lista que voy a ordenar
    for j in range(len(lista)-1,0,-1):#calculo la longitud de la lista y daria la posicion de los elementos de mi lista hasta llegar al ultimo elemento de la lista
        for i in range(j):#recorro la lista, el valor de j seria la posicion actual de mi lista
            if lista[i] > lista[i +1]:   #pregunto si el elemento actual[posicion] es mayor a el siguiente elemento[posicion+ 1]
                aux = lista[i]     #declaro una variable auxiliar y le asigno el valor actual [posicion]
                lista[i] = lista[i+1] # a esa posicion le asigno lo que hay en la lista[posicion + 1]
                lista[i+1] = aux # y en la[ posicion i+1] le coloco lo que hay en auxiliar

burbuja(lista)
print(lista)
