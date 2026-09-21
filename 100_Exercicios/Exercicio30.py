# Exercicio 30 - Aprovação de emprestimo
    # Leia o valor de um imóvel, o salário mensal do comprador e o prazo de pagamento em anos.
    # Calcule a prestação mensal e informe se o empréstimo foi aprovado.

valor_imovel = float(input("Informe o valor do imóvel: R$ ").replace(',', '.'))
salario = float(input("Informe o salário: R$ ").replace(',', '.'))
prazo = int(input("Informe o prazo: "))

prestacao = valor_imovel / (prazo * 12)
limite = salario * 0.30

limite_formatado = f"{limite:.2f}".replace('.', ',')
prestacao_formatada = f"{prestacao:.2f}".replace('.', ',')

print(f"Prestação: R$ {prestacao_formatada}")
print(f"Limite: R$ {limite_formatado}")

if prestacao <= limite:
    print("Aprovado")
else:
    print("Negado")

