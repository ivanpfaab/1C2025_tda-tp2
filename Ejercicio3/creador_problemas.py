from random import randint
def crear_problema(tamanio):
    D = randint(1, tamanio-1)
    b = randint(tamanio // 20, tamanio //3)
    k = randint(tamanio // 20, tamanio //3)
    d = [[0]*tamanio for _ in range(tamanio)]
    for i in range(tamanio):
        for j in range(i+1, tamanio):
            valor = randint(1, tamanio)
            d[i][j] = valor
            d[j][i] = valor
    return D, b,k,d

print(crear_problema(10))
