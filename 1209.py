import sys
from collections import deque


linha = sys.stdin.readline()
while linha:
    # Lendo valores de entrada
    n, m, k = map(int, linha.split())
    
    # Inicializando estruturas de dados
    f = [0] * (n + 1)  # Array que armazena a quantidade de conexões de cada nó
    vis = [False] * (n + 1)  # Array que marca os nós visitados
    adj = [[False] * (n + 1) for _ in range(n + 1)]  # Matriz de adjacência
    
    # Lendo as conexões
    i = 0
    while i < m:
        u, v = map(int, sys.stdin.readline().split())
        adj[u][v] = adj[v][u] = True
        f[u] += 1
        f[v] += 1
        i += 1
    
    # Fila para BFS
    queue = deque()
    
    # Adicionando nós que têm menos que k conexões
    i = 1
    while i <= n:
        if f[i] < k:
            queue.append(i)
            vis[i] = True
        i += 1
    
    # Removendo nós da fila e ajustando conexões
    while queue:
        u = queue.popleft()
        i = 1
        while i <= n:
            if adj[u][i] and not vis[i]:
                f[i] -= 1
                if f[i] < k:
                    queue.append(i)
                    vis[i] = True
            i += 1
    
    # Criando a resposta com os nós restantes
    ans = []
    i = 1
    while i <= n:
        if not vis[i]:
            ans.append(i)
        i += 1
    
    # Imprimindo a resposta
    if ans:
        print(" ".join(map(str, ans)))
    else:
        print(0)
    
    linha = sys.stdin.readline()
