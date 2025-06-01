# Dependencias

La correcta ejecicion del programa, enfocado en la funcion WAN_network(), depende de la libreria de python NetworkX (https://networkx.org/documentation/stable/install.html), para el uso de grafos dirigidos y el algoritmo Edmonds-Karp.

Se debe tener acceso a python3 y el manager de paquetes pip previo a la instalacion de NetworkX. Se asumira que el usuario cuenta con ambos.

El comando de la instalacion base de NetworkX es:

```bash
pip install networkx
```

En caso de un error: externally-managed-environment, se debe usar el comando:

```bash
sudo apt install python3-networkx
```

# Ejecucion 

## WAN_network()

El programa se ejecuta llamando a la funcion WAN_network(D, b, k, d), donde D es la distancia maxima permitida para ser un backup (de D para abajo), b es el numero maximo de antenas a las que puede respaldar una sola antena, k es el numero  minimo de antenas por backup, y d es una matriz que describe en d[i][j] la distancia de la antena i a la j. 

El resultado, de ser posible, sera impreso y se retornara el diccionario que lo retrate. De no ser posible, se avisara por otro print.