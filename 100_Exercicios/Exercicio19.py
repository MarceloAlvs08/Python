print("=" * 60)
print("Exercicio 19 - Maior e menor de três números.")
print("Enunciado: Leia três números reais e mostre o maior e o menor valor informado.")
print("=" * 60)
print()

a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))
c = int(input("Informe o terceiro valor: "))


# Descobrindo o maior
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

# Descobrindo o menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print(f"Maior: {maior}")
print(f"Menor: {menor}")


input("Pressione ENTER para sair...")







