casos = []
N = int(input())
i = 0
while i < N:
    #lendo os casos
    Pac = int(input())
    pacotes = []
    j = 0
    while j < Pac:
        pacotes.append(tuple(map(int, input().split())))
        j += 1
    casos.append((Pac, pacotes))
    i += 1


i = 0
while i < len(casos):
    Pac, pacotes = casos[i] 
    peso_limite = 50 
    n = len(pacotes)   #número de pacotes
    
    dp = [[0] * (peso_limite + 1) for _ in range(n + 1)] #tabela de programação dinâmica
    
    i_pac = 1
    while i_pac <= n:
        qt, peso = pacotes[i_pac - 1] #n foi visitaso
        w = 0
        while w <= peso_limite:
            #preenchendo a tabela
            if peso > w:
                dp[i_pac][w] = dp[i_pac - 1][w]
            else:
                dp[i_pac][w] = max(dp[i_pac - 1][w], dp[i_pac - 1][w - peso] + qt)
            w += 1
        i_pac += 1
    
    brinquedos_totais = dp[n][peso_limite]
    peso_total = 0
    pacotes_usados = set()
    
    w = peso_limite
    i_pac = n
    while i_pac > 0:
        if dp[i_pac][w] != dp[i_pac - 1][w]:
            qt, peso = pacotes[i_pac - 1]
            pacotes_usados.add(i_pac - 1)
            peso_total += peso
            w -= peso
        i_pac -= 1
            
    pacotes_sobraram = Pac - len(pacotes_usados)
    
    print(f'{brinquedos_totais} brinquedos')
    print(f'Peso: {peso_total} kg')
    print(f'sobra(m) {pacotes_sobraram} pacote(s)')
    print()
    
    i += 1

