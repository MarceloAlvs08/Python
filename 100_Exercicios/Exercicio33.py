print("=" * 60)
print("Exercicio 33 - Dia da semana.")
print("Leia um número de 1 a 7 e mostre o dia da semana correspondente.")
print("Para quando outro valor, mostre OPÇÃO INVÁLIDA.")
print("=" * 60)
print()

numero = int(input("Digite um número: "))


if numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
elif numero == 1:
    print("Domingo")
else:
    print("Opção inválida")
    