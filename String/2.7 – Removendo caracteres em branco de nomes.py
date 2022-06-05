"""
    2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do
nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três
funções de remoção de espaços: lstrip(), rstrip() e strip().

"""

nome = 'Karoline Lima'
print(f'\t {nome} \n é uma pessoa muito legal \t!!!')

nome2 = '  Karoline L'
nome2 = nome2.rstrip()
print(nome2)
nome3 = '  Karoline L'
nome3 = nome3.lstrip()
print(nome3)
nome4 = 'Karoline L'
nom4 = nome4.strip()
print(nome4)