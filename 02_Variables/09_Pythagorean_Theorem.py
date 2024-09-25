""" Criar um programa que usa o Teorema de Pitágoras para calcular a 
hipotenusa. Ele deve solicitar os valores dos catetos.
"""

a = int(input("Insira o valor do cateto a: "))
b = int(input("Insira o valor do cateto b: "))

c = (a**2 + b**2) ** 0.5

print(c)