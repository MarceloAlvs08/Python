print("=" * 60)
print("Exercicio 23 - Categoria de votação.")
print("Leia a idade de uma pessoa e informa a categoria de votação conforme as regras didáticas da tabela.")
print("=" * 60)
print()

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar")
elif idade <= 17:
    print("Voto opcional")
elif idade <= 69:
    print("Voto obrigatório")
elif idade >= 70:
    print("Voto opcional")
    
