print("=" * 60)
print("Exercicio 35 - Valor do ingresso.")
print("O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é estudante.")
print("Calcule o valor final conforme as regras.")
print("Regra")
print("Paga meia-entrada quem tiver menos de 12 anos, quem for estudante ou quem tiver 60 anos ou mais.")
print("O desconto é de 50% e não é acumulativo.")
print("=" * 60)
print()

idade = int(input("Digite sua idade: "))
estudante = input("Estudante - Sim ou Não? ").lower()

ingresso = 30.00
desconto = ingresso * 0.50


valor_formatado = f"{desconto:.2f}".replace('.', ',')
valor_formatado2 = f"{ingresso:.2f}".replace('.', ',')


if estudante == 'sim' or idade < 12 or idade >= 60:
    print(f"Valor meia entrada: R$ {valor_formatado}")
else:
    print(f"Valor normal: R$ {valor_formatado2}")