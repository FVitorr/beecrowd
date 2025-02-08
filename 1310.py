while True:
    try:
        n_dias = int(input())
        custo_diario = int(input())

        receitas = []
        i = 0
        while i < n_dias:
            receitas.append(int(input()))
            i += 1

        lucros = []
        i = 0
        while i < len(receitas):
            lucros.append(receitas[i] - custo_diario)
            i += 1

        lucro_atual = lucro_maximo = lucros[0]

        i = 1
        while i < len(lucros):
            lucro_atual = max(lucros[i], lucro_atual + lucros[i])
            lucro_maximo = max(lucro_maximo, lucro_atual)
            i += 1

        print(max(0, lucro_maximo))
    except EOFError:
        break