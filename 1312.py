def solve_max_prize(N, pyramid):
    dp = {}
    
    def can_take_ball(row, col, taken):
        """Verifica se podemos pegar a bola na posição (row, col)"""
        if row == 0:  # Bolas no topo podem sempre ser pegas
            return True
            
        # Verifica se todas as bolas acima desta estão marcadas como pegas
        if row > 0:
            # Precisamos verificar as duas bolas possíveis acima
            upper_row = row - 1
            # A bola diretamente acima
            if col < len(pyramid[upper_row]) and not taken[upper_row][col]:
                return False
            # A bola acima à esquerda (se não for a primeira da linha)
            if col > 0 and not taken[upper_row][col-1]:
                return False
        return True

    def calculate_max_prize(row, col, taken):
        if row >= N:
            return 0
            
        state = (row, col, tuple(tuple(row) for row in taken))
        if state in dp:
            return dp[state]
            
        # Não pegar esta bola
        max_prize = calculate_max_prize(row, col + 1, taken) if col + 1 < len(pyramid[row]) else \
                   calculate_max_prize(row + 1, 0, taken) if row + 1 < N else 0
        
        # Tentar pegar esta bola se possível
        if can_take_ball(row, col, taken):
            # Criar uma nova matriz de taken para este caminho
            new_taken = [row[:] for row in taken]
            new_taken[row][col] = True
            
            prize_with_ball = pyramid[row][col] + \
                            (calculate_max_prize(row, col + 1, new_taken) if col + 1 < len(pyramid[row]) else \
                             calculate_max_prize(row + 1, 0, new_taken) if row + 1 < N else 0)
            
            max_prize = max(max_prize, prize_with_ball)
        
        dp[state] = max_prize
        return max_prize

    # Inicializar matriz de bolas pegas
    taken = [[False] * i for i in range(1, N + 1)]
    
    result = calculate_max_prize(0, 0, taken)
    return max(0, result) 

def main():
    while True:
        N = int(input())
        if N == 0:
            break
            
        pyramid = []
        i = 0
        while i < N:
            row = list(map(int, input().split()))
            pyramid.append(row)
            i += 1
            
        result = solve_max_prize(N, pyramid)
        print(result)

if __name__ == "__main__":
    main()