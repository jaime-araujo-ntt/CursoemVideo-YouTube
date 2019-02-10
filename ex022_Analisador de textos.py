# ANALISANDO TEXTOS

nome = input("Insira o seu nome: ").strip()  # STRIP desconsidera espaços antes e depois da string

print("Seu nome em letras maiúsculas: {}".format(nome.upper())) # UPPER deixa tudo em maiusculo
print("Seu nome em Letras minúsculas: {}".format(nome.lower()))

print("Seu nome contém {} letras".format(len(nome) - nome.count(" ")))

# print("seu primeiro nome tem {} letras".format(nome.find(" ")))
nome = nome.split(" ")
print("seu primeiro nome é {} e tem {} letras".format(nome[0].upper(), len(nome[0])))
