import networkx as nx
import matplotlib.pyplot as plt

def WAN_network(D, b, k, d):
    create_graph(D, b, k, d)

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


    
    # DIBUJO DEL GRAFO 
    pos = {}
    spacing = 1.5

    pos['S'] = (0, -spacing)
    pos['T'] = (3, -spacing)

    for i in range(len(d)):
        pos[f"{i}_IN"] = (1, -i * spacing)
        pos[f"{i}_OUT"] = (2, -i * spacing)

    plt.figure(figsize=(10, len(d))) 
    nx.draw(newGraph, pos, with_labels=True, node_size=1000, node_color="lightblue", arrowsize=20)
    edge_labels = nx.get_edge_attributes(newGraph, 'capacity')
    nx.draw_networkx_edge_labels(newGraph, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

    return newGraph

def main():
    WAN_network(6, 2, 5, [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5], 
        [1, 2, 3, 4, 5], 
        [1, 2, 3, 4, 5]
    ])

main()
