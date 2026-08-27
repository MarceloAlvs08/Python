

### Exercicio 08 - Desconto no produto ###

preço = float(input("Informar preço: R$ "))
desconto = (preço) * 0.10

preço_final = (preço - desconto)


print(f"Preço: R$  {preço:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preço_final:.2f}")

### VERIFICAÇÃO FINAL ###
### Some o desconto com o preço final e verifique se o resultado é igual ao preço original ###

retorno_preço = (desconto + preço_final)
print(f"Retorno preço: R$ {retorno_preço:.2f}")



