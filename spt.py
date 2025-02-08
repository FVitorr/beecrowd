while True:
    try:
        data = input().split()
        
        n = int(data[0])
        m = int(data[1])
        min_r = int(data[2])

        rel = [[0] * n for _ in range(n)]

        for _ in range(m):  # Mapear relações
            r = list(map(int, input().split()))
            rel[r[0] - 1][r[1] - 1] = 1
            rel[r[1] - 1][r[0] - 1] = 1

        i = 0
        while i < n:
            if rel[i][i] == -1:  # Candidato já é inválido
                i += 1
                continue
            
            k = 0
            for j in range(n):  # Testa conexão
                if rel[i][j] == 1:
                    k += 1

            if k < min_r and rel[i][i] != -1:  # Elimina candidato
                for j in range(n):
                    rel[i][j] = -1
                    rel[j][i] = -1
                
                i = 0
                continue

            i += 1

        resultado = []
        for i in range(n):
            if rel[i][i] == 0:
                resultado.append(str(i + 1))

        print(" ".join(resultado) if resultado else "0")

    except EOFError:
        break  # Sai do loop quando chegar ao final do arquivo  