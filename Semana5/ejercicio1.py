"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
Una usando iteración (for o while)
Una usando recursividad
"""

def secuencia_iter(limite):
    resultado = []
    contador = 1
    while contador <= limite:
        resultado.append(contador)
        contador += 1
    return resultado

num_final = 15
print(f"Resultado iterativo: {secuencia_iter(num_final)}")


def secuencia_recursiva(valor):
    if valor <= 0:
        return []
    
    coleccion_numeros = secuencia_recursiva(valor - 1)
    coleccion_numeros.append(valor)
    
    return coleccion_numeros

print("Resultado recursivo:", secuencia_recursiva(15))