


preco = float(input("Preço unitário: R$ "))
quantidade_item = int(input("Quantidade: "))
frete = float(input("Valor do frete: R$ "))

subtotal = preco * quantidade_item
total = subtotal + frete

print(f"Subtotal R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")


confirmacao_valor_frete = subtotal - total
print(f"Confirmação do valor do frete: R$ {confirmacao_valor_frete:.2f}")




