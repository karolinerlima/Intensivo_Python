"""
   3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
crie uma lista contendo esses itens e então utilize cada função apresentada
neste capítulo pelo menos uma vez.
 
"""

livros = ['A Guerra dos Tronos','A Fúria dos Reis','A Tormenta de Espadas','O Festim dos Corvos','A Dança dos Dragões']
print(f'Quantidade de livros na biblioteca: {len(livros)}')
livros.append('George R.R. Martin')
remove = livros.pop(5)
print(f'{remove.title()}, foi removido da lista.\nCriar uma lista paraa autores!')
print(livros)

autores = []
autores.append('George R.R. Martin')
autores.insert(0,'stephen king')
autores.insert(2,'john green')
print(autores)
autores.sort()
print(autores)
autores.reverse()
print(autores)
