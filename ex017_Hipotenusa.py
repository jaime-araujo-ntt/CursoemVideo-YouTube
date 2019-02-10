from math import hypot
co = float(input('Insira o comprimento do Cateto Oposto:'))
ca = float(input('Insira o comprimento do Cateto Adjacente:'))
#hip = (co**2 + ca**2)**(1/2)
hip = hypot(co, ca)
print('A hipotenusa vale: {:.2f}'.format(hip))