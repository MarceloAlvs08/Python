# Exercicio 20 - Trẽs valores em ordem crescente.
    # Leia três números inteiros e mostre os valores em ordem crescente.


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# Guardamos os valores originais para a Verificação Final
v1_orig, v2_orig, v3_orig = valor1, valor2, valor3

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

if valor1 > valor3:
    valor1, valor3 = valor3, valor1

if valor2 > valor3:
    valor2, valor3 = valor3, valor2

print(f"Ordem crescente: {valor1}, {valor2}, {valor3}")

# VERIFICAÇÃO FINAL
print("--- VERIFICAÇÃO FINAL ---")
print(f"Valores originais (Antes):  {v1_orig}, {v2_orig}, {v3_orig}")
print(f"Valores ordenados (Depois): {valor1}, {valor2}, {valor3}")


    
