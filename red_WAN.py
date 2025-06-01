import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt

def WAN_network(distancia_max, limite_antenas, antenas_por_conjunto, d):
    network = create_graph(distancia_max, limite_antenas, antenas_por_conjunto, d)
    
    #La libreria NetworkX de python provee un algoritmo Edmonds_Karp que nos da el 
    #Flujo maximo y un diccionario con los caminos resultantes.
    flujo_maximo, residual_ek = nx.maximum_flow(network, 'S', 'T', 'capacity', edmonds_karp)

    if flujo_maximo < len(d[0]) * antenas_por_conjunto:
        #print("Numero minimo de backups inalcanzable")
        return 0
    else:
        return 1
        print_connections(residual_ek)
    
    return residual_ek

def print_connections(residual_ek):
    for u in residual_ek:
        for v in residual_ek[u]:
            flow = residual_ek[u][v]
            if flow:
                print(f"{u} → {v}: {flow}")

def create_graph(distancia_max, limite_antenas, antenas_por_conjunto, d):
    newGraph = nx.DiGraph()

    newGraph.add_node('S')
    newGraph.add_node('T')

    for i in range(len(d)):
        newGraph.add_node(f"{i}_IN")
        newGraph.add_node(f"{i}_OUT")
        newGraph.add_edge('S', f"{i}_IN", capacity = antenas_por_conjunto)
        newGraph.add_edge(f"{i}_OUT", 'T', capacity = limite_antenas)

    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] < distancia_max and i != j:
                newGraph.add_edge(f"{i}_IN", f"{j}_OUT", capacity = 1)


    return newGraph


def main():
    #D, b, k, d
    #Distancia max, limite antenas, minimo antenas
    WAN_network(5, 2, 3, [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 1], 
        [1, 2, 3, 4, 1], 
        [5, 5, 5, 4, 5]
    ])

