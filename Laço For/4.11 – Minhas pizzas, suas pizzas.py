"""
   4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte: • Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
um laço for para exibir a segunda lista. Certifique-se de que cada pizza
nova esteja armazenada na lista apropriada.
 
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