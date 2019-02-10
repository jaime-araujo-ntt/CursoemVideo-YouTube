imovel = float(input("Qual o valor do imóvel: "))
salario = float(input("Qual o seu salário: "))
anos = float(input("Quantos anos de Financiamento: "))

mensalidade = imovel/(anos*12)
mensalidade = round(mensalidade, 2)
print(mensalidade)
if mensalidade <= (0.30*salario):
    print("Empréstimo CONSEDIDO!")
    print("Sua prestação será de R${} por mês.".format(mensalidade))
else:
    print("Emprestimo NEGADO!")
    print("A prestação será maior que 30% do seu salário.")
