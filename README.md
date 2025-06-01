# Sistema de Ejercicios de Algoritmos y Optimización

Este repositorio contiene implementaciones y ejemplos en Python para diferentes ejercicios relacionados con algoritmos, programación lineal y redes de flujo máximo. Incluye código en cada ejercicio, pruebas y scripts para análisis de rendimiento y visualización.

---

## Dependencias

El programa completo requiere instalar las siguientes librerías de Python:

- **Python 3**: Lenguaje en el que está implementado.
- **pip**: Gestor de paquetes de Python.

### Librerías necesarias

- **networkx**: Biblioteca para modelar y analizar grafos dirigidos. Se usa en el ejercicio de Redes WAN para crear grafos, calcular flujos máximos y mostrar conexiones de respaldo.
- **pulp**: Biblioteca para resolver problemas de programación lineal. Se emplea en el ejercicio de optimización de campañas publicitarias.
- **scipy** (opcional): Utilizada para funciones de ajuste de curvas en análisis de rendimiento y tiempos de resolución.
- **matplotlib** (opcional): Para graficar resultados de rendimiento y ajuste de curvas.

### Instalación de dependencias

Para instalar todas las librerías necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

## Instrucciones de Ejecución

### (Opcional) Crear un entorno virtual para aislar las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
### Instalar las dependencias:

```bash
pip install -r requirements.txt
```

En caso que la libreria networkx arroje error, se puede instalar independientemente utilizando el siguiente comando:
```bash
sudo apt install python3-networkx
```

### Ejecutar el archivo principal:

```bash
python3 main.py
```
Este script ejecutará todas las tareas, mostrando en consola los resultados.

## Descripción de los ejercicios
### Ejercicio 1: Particiones mínimas de palíndromos
Función min_palindrome_partition(s) en Ejercicio1/programacion_dinamica.py calcula, usando programación dinámica, la cantidad mínima de particiones para que una cadena de entrada se divida en segmentos que sean palíndromos. Incluye ejemplos variados y pruebas automáticas que muestran los resultados en consola.

### Ejercicio 2: Optimización de campañas publicitarias
El ejercicio implementado en Ejercicio2/programacion_lineal.py resuelve un problema de programación lineal con restricciones, para determinar qué clientes deben ser contactados con el objetivo de maximizar el dinero obtenido de publicidades. Se utilizan variables binarias para decidir si aceptar la oferta a cada cliente, respetando límites de recursos y condiciones del problema.

### Ejercicio 3: Redes WAN y flujo máximo
El método WAN_network(D, b, k, d) en Ejercicio3/red_WAN.py construye un grafo dirigido que modela una red WAN, usando la librería networkx. Calcula el flujo máximo desde un nodo 'S' (origen) a 'T' (destino) mediante el algoritmo Edmonds-Karp. También verifica si el flujo alcanzado cumple con el respaldo mínimo, e imprime las conexiones de respaldo si es factible.
El archivo graficar_resultados.py permite generar problemas en diferentes tamaños y graficar estadísticas de tiempo de resolución y su ajuste, ayudando a analizar el rendimiento del algoritmo en distintas escalas.

El programa se ejecuta llamando a la funcion WAN_network(D, b, k, d), donde D es la distancia maxima permitida para ser un backup (de D para abajo), b es el numero maximo de antenas a las que puede respaldar una sola antena, k es el numero minimo de antenas por backup, y d es una matriz que describe en d[i][j] la distancia de la antena i a la j.

El resultado, de ser posible, sera impreso y se retornara el diccionario que lo retrate. De no ser posible, se avisara por otro print.