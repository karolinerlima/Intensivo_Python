"""
3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
uma moto Honda”.

"""
from asyncio import transports
from tracemalloc import take_snapshot


transporte = ['carro', 'moto','avião']
print(f'Gostaria de comprar um {transporte[0]}\n Gostaria de uma {transporte[1]}\n Gostaria de andar de {transporte[2]}')