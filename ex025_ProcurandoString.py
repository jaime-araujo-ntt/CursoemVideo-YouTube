nome = str(input("Digite seu nome completo: ")).strip().lower()
print("Seu nome contém Silva? {}".format("silva" in nome))

if "silva" in nome:
    print("quem massa!! seu nome também tem Silva")
else:
    print("que pena, não somos parentes!")