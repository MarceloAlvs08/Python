print("=" * 60)
print("Exercicio 31 - Divisel por 3 e por 5.")
print("Leia um número inteiro e informe em qual situação ele se encontra.")
print("=" * 60)
print()

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Divisível por 3 e 5")
elif numero % 3 == 0:
    print("Apenas por 3")
elif numero % 5 == 0:
    print("Apenas por 5")
else:
    print("Por nenhum")
    

print()
input("Pressione ENTER para sair...")





    