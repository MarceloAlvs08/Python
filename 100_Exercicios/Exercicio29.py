# Exercicio 29 - Tipo de triângulo
    # Leia trẽs medidas. Primeiro verifique se elas formam um triângulo.
    # Se formarem, classifique-o como equilátero, isósceles ou escaleno.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n3 + n2 > n1):
    if n1 == n2 == n3:
        print("Triângulo equilátero")
    elif (n1 == n2) or (n1 == n3) or (n2 == n3):
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não forma um triângulo")





