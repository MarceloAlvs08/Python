### Exercicio 16 - Positivo, negativo ou zero.

# Leia um número real e informe se ele é positivo, negativo ou igual a zero

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")
