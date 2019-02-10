import datetime

hoje = datetime.datetime.now()
idade = input("Insira sua data de nascimento (dd/mm/aaaa): ")
idade = idade.split('/')
idade = [int(i) for i in idade]

dias_18 = 365*18
dias_nascido = ((hoje.year - idade[2])*365)+((hoje.month - idade[1])*30)+(hoje.day - idade[0])
anos_nascido = int(dias_nascido/365)
print(anos_nascido)

if anos_nascido >= 18:
    print("Você ja se alistou?")
    alistar = input("Digite 1 para SIM ou 2 para NÃO")
    if alistar == "1":
        print("Nenhuma pendência com Alistamento! \nLIBERADO!")
    elif alistar == "2":
        tempo = anos_nascido - 18
        print("Voce passou {} anos do alistamento. SE APRESENTE!".format(tempo))
    else:
        print("Por Favor digite apenas '1' ou '2' para responder!")
else:
    tempo = 18 - anos_nascido
    print("Você tem {} anos. Ainda faltam {} anos para se alistar!".format(anos_nascido, tempo))
