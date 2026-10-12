# O loop 'while' (enquanto) executa um bloco de código repetidamente,
# contanto que uma determinada condição seja verdadeira.

# --- Sintaxe ---
# while condicao:
#     # Bloco de código que será executado
#
# É fundamental garantir que a condição se torne falsa em algum momento,
# para evitar um loop infinito.

# Exemplo 1: Contagem simples
# O loop continuará enquanto 'contador' for menor ou igual a 5.
print("--- Exemplo 1: Contagem de 1 a 5 ---")
contador = 1
while contador <= 5:
    print(f"Contador está em: {contador}")
    contador += 1  # Incrementamos o contador para que ele eventualmente chegue a 6 e pare o loop.

print("Loop 1 finalizado.\n")

# Exemplo 2: Loop controlado por entrada do usuário
print("--- Exemplo 2: Adivinhe a palavra secreta ---")
palavra_secreta = "python"
palpite = ""

while palpite.lower() != palavra_secreta:
    palpite = input("Adivinhe a palavra secreta (ou digite 'sair'): ")
    if palpite.lower() == "sair":
        print("Que pena! Vocẽ desistiu.")
        break # O camando 'break' interrompe o loop imediatamente.
    if palpite.lower() == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta!")
    else:
        print("Palpite incorreto. Tente novamente.")

print("Loop 2 finalizado. \n")



# Exemplo 3: Usando 'continue' para pular uma iteração
# Vamos imprimir apenas os números ímpares de 1 a 10.
print("--- Exemplo 3: Imprimindo apenas números ímpares ---")
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0: #Se o número for par...
        continue # ...o 'continue' pula o resto do código e vai para a próxima iteração.
    print(f"Número ímpar: {numero}")

print()
print("Loop 3 finalizado.\n")


