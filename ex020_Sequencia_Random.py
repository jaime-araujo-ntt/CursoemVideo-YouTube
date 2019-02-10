# import random
from random import shuffle
n1 = input('PRIMEIRO ALUNO:')
n2 = input('SEGUNDO ALUNO:')
n3 = input('TERCEIRO ALUNO:')
n4 = input('QUARTO ALUNO:')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(lista)