print("=" * 60)
print("Exercicio 34 - Quantidade de dias do mês.")
print("Leia o número de um mês e um ano. Mostre quantos dias o mês possui.")
print("=" * 60)
print()

mes = int(input("Digite o mês (númerico): "))
ano = int(input("Digite o ano: "))


if mes in (1, 3, 5, 7, 8, 10, 12):
    print("31 dias")
elif mes in (4, 6, 9, 11):
    print("30 dias")
elif mes == 2:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print("29 dias")
    else:
        print("28 dias")
else:
    print("Mês inválido: ")



input("Pressione ENTER para sair...")