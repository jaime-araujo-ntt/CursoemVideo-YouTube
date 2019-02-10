# import math
from math import sin, cos, tan, radians

angulo = float(input('Insira o angulo escolhido em graus:'))
s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))
print('O seu SENO é = {:.2f}'.format(s))
print('O seu COSSENO é = {:.2f}'.format(c))
print('A sua TANGENTE é = {:.2f}'.format(t))
