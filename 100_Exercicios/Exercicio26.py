# Exercicio 26 - Reajuste por faixa salarial
    # Leia o salário atual e calcule o novo

salario = float(input("Salário atual: R$ ").replace(',', '.'))

if salario <= 1500.00:
    reajuste = salario + (salario * 0.15)
    reajuste_salarial = "15%"
elif salario <= 3000.00:
    reajuste = salario + (salario * 0.10)
    reajuste_salarial = "10%"
elif salario > 3000.00:
    reajuste = salario + (salario * 0.05)
    reajuste_salarial = "5%"

valor_formatado = f"{reajuste:.2f}".replace('.', ',')

print(f"Reajuste salárial: {reajuste_salarial}")
print(f"Novo salário: R$ {valor_formatado}")


