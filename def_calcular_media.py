def calcular_media(lista_de_numeros):
    total = sum(lista_de_numeros)
    quantidade = len(lista_de_numeros)
    if quantidade == 0:
        return 0
    media = total / quantidade
    return media

notas_aluno1 = (8.5, 7.0, 9.0, 10.0)
media_aluno1 = calcular_media(notas_aluno1)

print(f"A média do aluno 1 é: {media_aluno1:.2}")

notas_aluno2 = (5.5, 6.0, 7.5)
media_aluno2 = calcular_media(notas_aluno2)

print(f"A média do aluno 2 é: {media_aluno2:}")
