

### Exercicio 09 - Ajuste salaraial ###

salario = float(input("Salário atual: R$ "))
aumento = salario * 0.15
novo_salario = aumento + salario
print(f"Salário atual: R$ {salario:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

### Subtraia o salário antigo do novo salário e verifique se o resultado é igual ao aumento ###

diferenca_aumento = salario - novo_salario
print(f"Diferença do aumento: R$ {diferenca_aumento:.2f}")
