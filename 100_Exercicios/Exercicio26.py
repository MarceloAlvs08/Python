print("=" * 60)
print("Exercicio 26 - Reajuste por faixa salarial.")
print("Leia o salário atual e calcule o novo.")
print("=" * 60)
print()

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


print()
input("Pressione ENTER para sair...")

