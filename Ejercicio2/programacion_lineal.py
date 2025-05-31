from pulp import LpMaximize, LpProblem, LpVariable, LpBinary

# Crear el problema
prob = LpProblem("Maximizar_Beneficio_Publicidad", LpMaximize)

# Variables: Hago una variable binaria para cada uno de los clientes
# que pueden ser seleccionados para publicidad
# Las variables representan si se elige o no la opción de publicidad
A = LpVariable('A', cat=LpBinary)
# Separo al cliente B en dos opciones (B1 y B2) para representar diferentes campañas
B1 = LpVariable('B1', cat=LpBinary)  
B2 = LpVariable('B2', cat=LpBinary)  
C = LpVariable('C', cat=LpBinary)
D = LpVariable('D', cat=LpBinary)
E = LpVariable('E', cat=LpBinary)
F = LpVariable('F', cat=LpBinary)
G = LpVariable('G', cat=LpBinary)

# Restriccion: La suma de paradas no puede superar las 200 totales
prob += (
    30  * A + 
    80  * B1 + 
    120 * B2 +
    75  * C +
    50  * D +
    2   * E +
    20  * F +
    100 * G) <= 200

# Restricción: no se pueden concesionar A y D a la vez
prob += A + D <= 1

# Restricción: La elección de B puede ser solo una opción (o ninguna)
prob += B1 + B2 <= 1

# Función objetivo: maximizar beneficio
prob += (
    50000   * A +
    100000  * B1 + 
    120000  * B2 +
    100000  * C +
    80000   * D +
    5000    * E +
    40000   * F +
    90000   * G
)

# Resolver
prob.solve()

# Resultado
resultado = {
    'A': A.varValue,
    'B1': B1.varValue,
    'B2': B2.varValue,
    'C': C.varValue,
    'D': D.varValue,
    'E': E.varValue,
    'F': F.varValue,
    'G': G.varValue,
    'Beneficio_Total': prob.objective.value()
}

print("Resultados de la optimización:")
for var, val in resultado.items():
    status = "Seleccionado" if val == 1 else "No seleccionado"
    print(f"{var}: {status}")