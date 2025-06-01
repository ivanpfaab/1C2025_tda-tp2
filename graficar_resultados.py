import matplotlib.pyplot as plt
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
    for n in list(range(30, 150)):
        D, b, k, d = crear_problema(n)
        tiempo = []
        res_temps = []
        for i in range(5):
            t0 = time.time()
            res_temps.append(WAN_network(D,b,k,d))
            tf = time.time()
            tiempo.append(tf - t0)
        if sum(res_temps) >= 2:
            resultados.append(1)
        else:
            resultados.append(0)
        tiempos.append(sum(tiempo) / 5)
    return tiempos, resultados

def graficar_tiempos():

    tiempos, resultados = medir_tiempos()
    tamanios = list(range(30, 150))

    print(f"len de tiempos, resultados y tamanios es: {len(tiempos), len(resultados), len(tamanios)}")
    # Separar puntos por color
    x_rojo = []
    x_azul = []
    y_rojo = []
    y_azul = []
    for i in range(len(resultados)):
        res = resultados[i]
        if res == 0:
            x_rojo.append(tamanios[i])
            y_rojo.append(tiempos[i])
        else:
            x_azul.append(tamanios[i])
            y_azul.append(tiempos[i])

    # Crear scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x_rojo, y_rojo, color='red', label='Resultado = 0')
    plt.scatter(x_azul, y_azul, color='blue', label='Resultado = 1')
    plt.xlabel('Tamaño del problema (n)')
    plt.ylabel('Tiempo promedio (segundos)')
    plt.title('Resultado vs Tiempo de ejecución')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # tiempos = medir_tiempos()
    # tamanios = list(range(30, 150))
    # 
    # plt.figure(figsize=(10, 6))
    # plt.plot(tamanios, tiempos, marker='o', linestyle='-', color='blue', label='Tiempo promedio')
    # plt.title('Tiempo promedio de ejecución vs Tamaño del problema (n)')
    # plt.xlabel('Tamaño del problema (n)')
    # plt.ylabel('Tiempo promedio (segundos)')
    # plt.grid(True)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

graficar_tiempos()
