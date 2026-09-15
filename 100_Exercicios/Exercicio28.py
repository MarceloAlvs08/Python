# Exercicio 28 - É possível formar um triângulo?
    # Leia três medidas positivas e informe se elas podem formar um triângulo.

valor_a = int ( input ( "Digite um número: " ) )
valor_b = int ( input ( "Digite um número: " ) )
valor_c = int ( input ( "Digite um número: " ) )

if (valor_a + valor_b  > valor_c) and (valor_a + valor_c > valor_b) and (valor_b + valor_c > valor_a):
 print("Formam um triangulo")
else:
 print("Não formam um triangulo")




