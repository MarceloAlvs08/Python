
### Exercicio - Troca de valores ### 

a = int(input("A: "))
b = int(input("B: "))


# 1. Guarda o valor de 'a' na variável auxiliar 'aux'
aux = a

# 2. Agora 'a' pode receber o valor de 'b'
a = b

# 3. 'b' recebe o valor original de 'a' (que está salvo em 'aux')
b = aux

print("\nDepois da troca:")
print(f"A: {a}")
print(f"B: {b}")

# Segunda troca consecutiva (Verificação Final)
aux = a
a = b
b = aux

print("\nDepois da segunda troca (valores originais):")
print(f"A: {a}")
print(f"B: {b}")
