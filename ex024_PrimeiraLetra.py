cidade = input("insira o nome de uma cidade -> ").strip().lower()
print(cidade[0:5] == "santo")

separador = cidade.split(" ")

if separador[0] == "santo":
    print("sua cidade começa com o nome {}. \nAMÉM!".format(separador[0].upper()))
elif separador[0] == "barreiras":
    print("{} é a melhor cidade de todas!!".format(separador[0].upper()))
else:
    print("{}... \nque nome comum!".format(separador[0]))