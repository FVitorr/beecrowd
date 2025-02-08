def solve_max_prize(N, pyramid):
    # Inicializa a tabela dp onde dp[i][j] guarda o valor máximo que podemos pegar na posição (i, j)
    dp = [row[:] for row in pyramid]  # Faz uma cópia da pirâmide para manipular
    
    # Preenche a tabela dp de baixo para cima
    for row in range(N-2, -1, -1):  # Começamos da penúltima linha para cima
        for col in range(len(pyramid[row])):
            # A soma será o valor da bola atual mais o valor máximo das duas bolas abaixo
            dp[row][col] += max(dp[row+1][col], dp[row+1][col+1] if col + 1 < len(pyramid[row+1]) else float('-inf'))
    
    # O resultado estará na posição dp[0][0], que é o topo da pirâmide
    return dp[0][0]

def main():
    while True:
        N = int(input())
        if N == 0:
            break
            
        pyramid = []
        for i in range(N):
            row = list(map(int, input().split()))
            pyramid.append(row)
            
        result = solve_max_prize(N, pyramid)
        print(result)

if __name__ == "__main__":
    main()
