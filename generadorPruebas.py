import matplotlib.pyplot as plt
import time
import numpy as np

def min_palindrome_partition(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_pal[i][i] = True
    
    for length in range(2, n+1):
        for start in range(n-length+1):
            end = start + length - 1
            if s[start] == s[end]:
                if length == 2:
                    is_pal[start][end] = True
                else:
                    is_pal[start][end] = is_pal[start+1][end-1]
    
    dp = [float('inf')] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 1
        else:
            for j in range(1, i+1):
                if is_pal[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)
    return dp[n-1]


def gen_cadena_sin_palindromo(multiplo):
    # Cada multiplo representa 10 caracteres
    base = "ABCDEFGHIJ"
    return (base * multiplo)[:multiplo * 10]


def medir_tiempos_y_graficar():
    multiplicadores = [1, 5, 10, 50, 80, 100]
    longitudes = [x * 10 for x in multiplicadores]
    tiempos = []

    for m in multiplicadores:
        cadena = gen_cadena_sin_palindromo(m)
        inicio = time.perf_counter()
        min_palindrome_partition(cadena)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)

    # Calcular curva teórica O(n^2)
    C = tiempos[-1] / (longitudes[-1] ** 2)  # ajustar con el último valor
    n_teorico = np.linspace(min(longitudes), max(longitudes), 100)
    t_teorico = C * n_teorico**2

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, tiempos, marker='o', linestyle='-', color='blue', label='Tiempos medidos')
    plt.plot(n_teorico, t_teorico, 'r--', label='Ajuste teórico $O(n^2)$')
    plt.title('Tiempo de ejecución vs Longitud de cadena')
    plt.xlabel('Longitud de la cadena')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Ejecutar
medir_tiempos_y_graficar()
