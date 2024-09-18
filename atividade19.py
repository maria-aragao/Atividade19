# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

def calcular_fatorial(número):
    resultado = 1
    for i in range(1, número + 1):
        resultado *= i
    return resultado

número = 111
resultado = calcular_fatorial(número)
print("O fatorial de", número, "é", resultado)