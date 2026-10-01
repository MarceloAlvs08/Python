print("=" * 60)
print("Exercício 24 - Ano bissexto.")
print("Leia um ano inteiro e informe se ele é bissexto.")
print("=" * 60)
print()

ano = int(input("Digite o ano: "))


if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")

