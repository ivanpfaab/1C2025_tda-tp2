import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt

def WAN_network(D, b, k, d):
    network = create_graph(D, b, k, d)
    
    #La libreria NetworkX de python provee un algoritmo Edmonds_Karp que nos da el 
    #Flujo maximo y un diccionario con los caminos resultantes.
    flujo_maximo, residual_ek = nx.maximum_flow(network, 'S', 'T', 'capacity', edmonds_karp)

    if flujo_maximo < len(d[0]) * k:
        print("Numero minimo de backups inalcanzable")
        return
    else:
        print_connections(residual_ek)
    
    return residual_ek

def print_connections(residual_ek):
    for u in residual_ek:
        for v in residual_ek[u]:
            flow = residual_ek[u][v]
            if flow:
                print(f"{u} → {v}: {flow}")

def create_graph(D, b, k, d):
    newGraph = nx.DiGraph()

    newGraph.add_node('S')
    newGraph.add_node('T')

    for i in range(len(d)):
        newGraph.add_node(f"{i}_IN")
        newGraph.add_node(f"{i}_OUT")
        newGraph.add_edge('S', f"{i}_IN", capacity = k)
        newGraph.add_edge(f"{i}_OUT", 'T', capacity = b)

    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] < D and i != j:
                newGraph.add_edge(f"{i}_IN", f"{j}_OUT", capacity = 1)

    show_graph(newGraph)

    return newGraph

def show_graph(newGraph):

    # DIBUJO DEL GRAFO 
    pos = {}
    spacing = 1.5

    n = int((len(newGraph.nodes) - 2) / 2)

    pos['S'] = (0, -spacing)
    pos['T'] = (3, -spacing)

    for i in range(n):
        pos[f"{i}_IN"] = (1, -i * spacing)
        pos[f"{i}_OUT"] = (2, -i * spacing)

    plt.figure(figsize=(10, n)) 
    nx.draw(newGraph, pos, with_labels=True, node_size=1000, node_color="lightblue", arrowsize=20)
    edge_labels = nx.get_edge_attributes(newGraph, 'capacity')
    nx.draw_networkx_edge_labels(newGraph, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    #D, b, k, d
    #Distancia max, limite antenas, minimo antenas
    WAN_network(5, 2, 1, [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 1], 
        [1, 2, 3, 4, 1], 
        [5, 5, 5, 4, 5]
    ])

main()
