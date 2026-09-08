# Exercicio 21 - Aprovado ou reprovado
    # Leia duas notas, calcule a média e informe se o aluno foi aprovado ou reprovado.

nota_01 = float(input("Digite a primeira nota: ").replace(',', '.'))
nota_02 = float(input("Digite a segunda nota: ").replace(',', '.'))

soma = nota_01 + nota_02
media = soma / 2 

media_formatada = f"{media:.1f}".replace('.', ',')
print(f"Média do aluno: {media_formatada}")

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
