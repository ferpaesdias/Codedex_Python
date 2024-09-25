pesos = int(input("What do you have left in pesos? "))
soles = int(input("What do you have left in soles? "))
reais = int(input("What do you have left in reais? "))

dolar_pesos = (pesos * 0.00024)
dolar_soles = (soles * 0.27)
dolar_reais = (reais * 0.18)

print(dolar_pesos + dolar_soles + dolar_reais)