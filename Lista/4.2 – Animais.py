    
"""
    4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por
exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses
animais têm em comum. Você poderia exibir uma frase como Qualquer um
desses animais seria um ótimo animal de estimação!  
    
"""
animal = ['Gato','Cachorro','Coelho']

for animais in animal:
    print('Animais de estimação: ' + animais.title())
    print(animais.title() + ', seria um ótimo animal de estimação')
    print(animais.title() + ', são fofinhos!!!')