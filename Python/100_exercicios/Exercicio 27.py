# Exercicio 27 - Classificação de IMC
    # Leia o peso em quilogramas e a altura em metros. Calcule o IMC e classifique o resultado usando apenas as regras didaticas da tabela.


peso = float(input("Informe seu peso: ").replace(',', '.'))
altura = float(input("Informe sua altura: ").replace(',', '.'))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao_esperada = "Abaixo da faixa"
elif imc >= 18.5 and imc < 25.0:
    classificacao_esperada = "Faixa normal"
elif imc >= 25.0 and imc < 30.0:
    classificacao_esperada = "Acima da faixa"
elif imc >= 30.0:
    classificacao_esperada = "Faixa elevada"

valor_formatado = f"{imc:.2f}".replace('.', ',')

print(f"IMC: {valor_formatado}")
print(f"Classificação: {classificacao_esperada}")


