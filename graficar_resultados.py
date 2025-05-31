from red_WAN import WAN_network
from random import randint
import time

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

def medir_tiempos():
    tiempos = []
    resultados = []
    for n in range(5, 500):
        D, b, k, d = crear_problema(n)
        tiempo = []
        resultado = []
        for i in range(2):
            t0 = time.time()
            resultado = WAN_network(D,b,k,d)
            print(resultado)
            tf = time.time()
            tiempo.append(tf - t0)
        tiempos.append(sum(tiempo) / 2)
    return tiempos

medir_tiempos()
