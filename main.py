import json
from Ejercicio2.programacion_lineal import publicity_optimization
from Ejercicio1.programacion_dinamica import min_palindrome_partition
from Ejercicio3.red_WAN import WAN_network

def main():
    with open("Tests/ejercicio1.json", "r") as file:
        datos = json.load(file)
    tests = datos["tests"]
    
    # Ejercicio 1: Palíndromos
    print("\n##########    Ejercicio 1: Min Particiones de Palíndromos    ##########\n")
    i = 0
    for s in tests:
        result = min_palindrome_partition(s)
        i+= 1
        print(f"Test {i}")
        print(f"\tCadena: {s}")
        print(f"\tMínimo de particiones: {result}\n")
    
    # Ejercicio 2: Programación lineal
    print("\n##########    Ejercicio 2: Optimización de publicidad    ##########\n")
    publicity_optimization()

    # Ejercicio 3: En desarrollo (placeholder)
    print("\n##########    Ejercicio 3: Redes de Flujo    ##########\n")
    with open("Tests/ejercicio3.json", "r") as f:
        datos = json.load(f)
    tests = datos["tests"]
    for i, test in enumerate(tests):
        D = test["D"]
        b = test["b"]
        k = test["k"]
        d = test["d"]
        print(f"\nTest {i+1}\n")
        print(f"D: {D}, b: {b}, k: {k}")
        WAN_network(D,b,k,d)


if __name__ == "__main__":
    main()
