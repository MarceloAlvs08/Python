# Exercicio 22 - Situação do aluno por faixa
    # Leia duas notas, calcule a média e informe a situação do aluno conforme a tabela.

nota_01 = float(input("Digite a primeira nota do aluno: ").replace(',', '.'))
nota_02 = float(input("Digite a segunda nota do aluno: ").replace(',', '.'))

soma = nota_01 + nota_02
media = soma / 2

media_aluno = f"{media:.1f}".replace('.', ',')
print(f"Media: {media_aluno}")

if media < 5:
    print("Aluno reprovado")
elif media >= 5 and media < 7:
    print("Aluno em recuperação")
else:
    print("Aluno aprovado")
    
