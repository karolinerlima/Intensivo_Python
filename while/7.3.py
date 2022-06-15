''''

7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
'''


numero = int(input('Digite um número: '))

multiplo = numero  % 10

if multiplo == 0:
    print('Multiplo')
else:
    print('Não é multiplo de 10')