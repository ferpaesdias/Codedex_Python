""" Pergunte ao usuário qual é sua altura e quantos créditos ele possui, e 
armazene os valores em uma variável de altura e em uma variável de crédito

* Se eles forem altos e tiverem créditos suficientes, imprima "Aproveite o passeio!"
* Caso contrário, se eles tiverem créditos suficientes, mas não forem altos o 
suficiente, imprima "Você não é alto o suficiente para andar".
* Caso contrário, se eles forem altos o suficiente, mas não tiverem créditos 
suficientes, imprima "Você não tem créditos suficientes".
* Caso contrário, imprima uma mensagem dizendo que eles não atenderam a 
nenhum dos requisitos.

"""

altura = int(input("Qual a sua altura em centimetros: \n"))
creditos = int(input("Quantos créditos você possui: \n"))

if altura >= 137 and creditos >= 10:
    print("Aproveite o passeio!")
elif altura < 137 and creditos >= 10:
    print("Você não é alto o suficiente para andar")
elif altura >= 137 and creditos < 10:
    print("Você não tem créditos suficientes")
else:
    print("Você não atende nenhum dos requisitos")    