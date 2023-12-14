import random

def generar_tablero(n):
    """Genera un tablero aleatorio de N reinas."""
    return [random.randint(0, n-1) for _ in range(n)]

def calcular_aptitud(tablero):
    """Calcula la aptitud de un tablero (número de conflictos)."""
    n = len(tablero)
    conflictos = 0
    for i in range(n):
        for j in range(i+1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1
    return conflictos

def seleccion_padres(poblacion):
    """Selecciona dos padres basados en el torneo."""
    torneo = random.sample(poblacion, 5)
    torneo.sort(key=lambda x: calcular_aptitud(x))
    return torneo[0], torneo[1]

def cruzar(padre1, padre2):
    """Realiza el cruce de dos padres para obtener un hijo."""
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

def mutar(tablero):
    """Realiza una mutación en el tablero intercambiando dos reinas."""
    i, j = random.sample(range(len(tablero)), 2)
    tablero[i], tablero[j] = tablero[j], tablero[i]
    return tablero

def algoritmo_genetico(n, tamano_poblacion, num_generaciones):
    """Implementa el algoritmo genético para el problema de las N reinas."""
    poblacion = [generar_tablero(n) for _ in range(tamano_poblacion)]

    for generacion in range(num_generaciones):
        poblacion = sorted(poblacion, key=lambda x: calcular_aptitud(x))

        if calcular_aptitud(poblacion[0]) == 0:
            print(f'Solución encontrada en la generación {generacion}:\n{poblacion[0]}')
            return poblacion[0]

        nueva_poblacion = []

        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = seleccion_padres(poblacion)
            hijo1 = cruzar(padre1, padre2)
            hijo2 = cruzar(padre2, padre1)

            if random.random() < 0.1:  # Probabilidad de mutación
                hijo1 = mutar(hijo1)
            if random.random() < 0.1:
                hijo2 = mutar(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion

    print(f'Solución no encontrada después de {num_generaciones} generaciones.')
    return None

# Parámetros del algoritmo genético
n_reinas = 8
tamano_poblacion = 100
num_generaciones = 1000

# Ejecutar el algoritmo genético
solucion = algoritmo_genetico(n_reinas, tamano_poblacion, num_generaciones)
