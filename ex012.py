p = int(input('Insira o preço:'))
d = (p * (5 / 100))
np = p - d
print('O preço com o desconto é de R$ {:.2f}!'.format(p - d))
