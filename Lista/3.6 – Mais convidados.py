"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que
você encontrou uma mesa de jantar maior.
79
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa
que está em sua lista.

"""
convidado = ['Karol', 'Davi', 'Sophia', 'Roseli','Wagner']
print(f'Para nossa alegria consegui uma mesa maior.\nVocês poderam convidar uma pessoa cada')
convidado2 = ['Luana', 'Josi','Allison','Lucas','Andre']

print(f'{convidado[0]} Gostaria de convidar {convidado2[0]}')
print(f'{convidado[1]} Gostaria de convidar {convidado2[1]}')
print(f'{convidado[2]} Gostaria de convidar {convidado2[2]}')
print(f'{convidado[3]} Gostaria de convidar {convidado2[3]}')
print(f'{convidado[4]} Gostaria de convidar {convidado2[4]}')

print(f'Os convidados adicionais são: {convidado2[0]}, {convidado2[1]}, {convidado2[2]}, {convidado2[3]}, {convidado2[4]}')