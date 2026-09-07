
### Exercicio 10 - Salário com comissão ###


salario = float(input("Salário fixo: R$ "))
vendas = float(input("Valor vendido: R$ "))

comissao = vendas * 0.04
salario_total = salario + comissao

print(f"Salário fixo: R$ {salario:.2f}")
print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")

# Verificação Final
print(f"Verificação (4% apenas das vendas): {vendas:.2f} x 0.04 = R$ {comissao:.2f}")

