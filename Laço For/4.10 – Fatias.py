"""
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para
exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
exibir os três últimos itens da lista
"""

lista = ['Karol', 'Davi', 'Sophia', 'Roseli','Wagner','Luana', 'Josi','Allison','Lucas','Andre']
print('Os tres primeiros:')
for listas in lista [:3]:
    print((listas.title()))
print('Do meio:')
for listas in lista[3:6]:
    print(listas.title())
print('Final:')
for listas in lista[6:9]:
    print(listas.title())
print(f'Ultimo: \n{lista[9]}')