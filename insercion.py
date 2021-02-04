
lista = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
def insercion(lista ):
    for i in range(1,len(lista)): #empezamos con el elemento 1 de mi lista en este caso el 44 hasta el ultimo que es el 48
        print(lista)
        valor = lista[i] #cogemo el elemento 44  y lo guardamos en la variable valor
        indice = i # guardamos el indice que vamos a ir iterando en una variable
        print(indice)
        while indice > 0 and lista[indice-1] > valor:
            lista[indice] = lista[indice - 1]
            indice = indice-1
            lista[indice] = valor

insercion(lista)
print(lista)


