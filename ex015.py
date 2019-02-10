d = int(input('Insira a quantidade de dias:'))
# d1 = d * 60
km = float(input('Insira a quantidade de Quilmetros:'))
# km1 = km * 0.15
pago = (d*60)+(km*0.15)
# print('O total a ser pago pela locação do veículo é R$ {}.'.format(d1 + km1))
print('O total a ser pago pela locação do veiculo é de R$ {:.2f}'.format(pago))
