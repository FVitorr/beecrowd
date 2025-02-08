import sys
T = int(sys.stdin.readline().strip())  # Número de instâncias
while T > 0:
    N, M = map(int, sys.stdin.readline().split())  # Lê N e M
    blocos = list(map(int, sys.stdin.readline().split()))  # Lê os blocos disponíveis

    dp = [float('inf')] * (M + 1)  # Inicializa com infinito (valor alto)
    dp[0] = 0  # Base: comprimento 0 requer 0 blocos

    i = 0
    while i < N:  # Iterando pelos tipos de blocos
        bloco = blocos[i]
        j = bloco
        while j <= M:  # Atualizando dp[j] para todos os valores possíveis
            dp[j] = min(dp[j], dp[j - bloco] + 1)
            j += 1
        i += 1

    print(dp[M] if dp[M] != float('inf') else -1 )    
    T -= 1  # Decrementa o número de instâncias
