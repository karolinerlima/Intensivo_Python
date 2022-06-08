"""
   3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não
poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.
 
"""
convidado = ['Karol', 'Davi', 'Sophia', 'Roseli','Wagner']
desconvida = 'Karol'
convidado.remove(desconvida)
print(f'Infelizmente o convidado {desconvida} não podera comparecer.')
convidado.insert(0,'Ale')
print(f'Gostaria de convida você {convidado[0]} para um jantar.')
print(f'Gostaria de convida você {convidado[1]} para um jantar.')
print(f'Gostaria de convida você {convidado[2]} para um jantar.')
print(f'Gostaria de convida você {convidado[3]} para um jantar.')
print(f'Gostaria de convida você {convidado[4]} para um jantar.')