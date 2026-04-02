def suma_ciclo(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def suma_recursiva(n):
    if n <= 0:
        return 0
    return n + suma_recursiva(n - 1)

print(suma_ciclo(10))
print(suma_recursiva(10))