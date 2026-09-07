# Exercicio 18 - Maior de dois números
    # Leia dois números reais e mostra qual deles é o maior. Se os valores forem iguais, informe que não existe maior.

primeiro_valor = int(input("Digite um número: "))
segundo_valor = int(input("Digite um número: "))

if primeiro_valor > segundo_valor:
    print(f"Maior valor: {primeiro_valor}")
elif segundo_valor > primeiro_valor:
    print(f"Maior valor: {segundo_valor}")
else:
    print("Valore iguais")
