n = int(input('Digite um número:'))
n1 = n*2
n2 = n*3
# n3 = n**(1/2)
n3 = pow(n, (1/2))
# print('> Seu numero é {}, \n> Seu dobro é {}, \n> Seu triplo é {}, \n> Sua raiz é {:.2f}.'.format(n, n1, n2, n3))
print('O seu numero é {}, \nSeu dobre é {}, \nSeu triplo é {}, \nSua raiz é {:.2f}.'.format(n, (n*2), (n*3), pow(n,(1/2))))
