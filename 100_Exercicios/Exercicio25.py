# Exercicio 25 - Preço conforme a forma de pagamento
    # Leia o preço de um produto e a opção de pagamento. Calcule e mostre o valor final conforme a tabela.

preco = float(input("Digite o preço: R$ ").replace(',', '.'))
opcao = int (input("Digite a opção: "))

if opcao == 1:
    valor_final = preco - (preco * 0.10)
    forma_pagamento = "Dinheiro ou pix"
elif opcao == 2:
    valor_final = preco - (preco * 0.05)
    forma_pagamento = "Débito"
elif opcao == 3:
    valor_final = preco
    forma_pagamento = "Crédito à vista"
elif opcao == 4:
    valor_final = preco + (preco * 0.08)
    forma_pagamento = "Crédito parcelado"

valor_formatado = f"{valor_final:.2f}".replace('.', ',')

print(f"Forma de pagamento: {forma_pagamento}")
print(f"Valor final: R$ {valor_formatado}")

