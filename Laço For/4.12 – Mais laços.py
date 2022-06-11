"""
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
laços for para fazer exibições a fim de economizar espaço. Escolha uma
versão de foods.py e escreva dois laços for para exibir cada lista de comidas.
"""
pizza = ['Frango Catupiry', 'Calabresa','Lombo','Brocolis']
pizza_amigos = ['Portugues', 'Quatro Queijo', 'Mexicana','Frango']

pizza.append('Toscana')
print(pizza)
pizza_amigos.append('Peperoni')
print(pizza_amigos)

print('Minhas pizzas preferidas são: ')
for pizzas in pizza:
    print(pizzas)
print('Pizza favorita dos meus amigos: ')
for pizza_amigoos in pizza_amigos:
    print(pizza_amigoos)