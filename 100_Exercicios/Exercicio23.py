# Exercicio 23 - Categoria de votação
    # Leia a idade de uma pessoa e informa a categoria de votação conforme as regras didáticas da tabela.

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não pode votar")
elif idade <= 17:
    print("Voto opcional")
elif idade <= 69:
    print("Voto obrigatório")
elif idade >= 70:
    print("Voto opcional")
    
