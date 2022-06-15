""""
7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.
"""

qt_pessoa = int(input('Digite a quantidade de pessoas: '))

if qt_pessoa >=8:
    print('Por gentileza aguardar a liberação da mesa')
else:
    print('Sua mesa está pronta!!')