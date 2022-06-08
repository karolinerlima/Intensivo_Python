"""
3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma
mensagem informando o número de pessoas que você está convidando para o
jantar.

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
soma = len(convidado) + len(convidado2)
print(f'O total de convidados por mim: {len(convidado)}\nTotal de convidados dos convidados {len(convidado2)}\nTotal geral: {soma}')