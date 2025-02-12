def solve_festival(N, shows_by_stage):
    # Lista para todos os shows com (início, fim, valor, palco)
    all_shows = []
    for stage in range(N):
        for start, end, value in shows_by_stage[stage]:
            all_shows.append((start, end, value, stage))
    
    def are_compatible(show1, show2):
        # Verifica se dois shows não têm sobreposição de horário
        return show1[0] >= show2[1] or show2[0] >= show1[1]
    
    n = len(all_shows)
    # dp[mask] armazena o melhor valor possível para uma combinação de shows
    dp = {}
    # visited_stages[mask] armazena os palcos visitados para cada combinação
    visited_stages = {}
    
    def calculate_dp(mask):
        if mask in dp:
            return dp[mask]
        
        # Base case: nenhum show selecionado
        if mask == 0:
            dp[mask] = 0
            visited_stages[mask] = set()
            return 0
        
        best_value = -1
        best_stages = set()
        
        # Tenta cada show como o último da sequência
        for curr_pos in range(n):
            if not (mask & (1 << curr_pos)):
                continue
                
            # Remove o show atual do mask
            remaining_mask = mask ^ (1 << curr_pos)
            curr_show = all_shows[curr_pos]
            
            # Verifica compatibilidade com outros shows selecionados
            compatible = True
            for other_pos in range(n):
                if remaining_mask & (1 << other_pos):
                    if not are_compatible(curr_show, all_shows[other_pos]):
                        compatible = False
                        break
            
            if compatible:
                prev_value = calculate_dp(remaining_mask)
                if prev_value != -1:
                    new_value = prev_value + curr_show[2]
                    new_stages = visited_stages[remaining_mask].copy()
                    new_stages.add(curr_show[3])
                    
                    if new_value > best_value:
                        best_value = new_value
                        best_stages = new_stages
        
        dp[mask] = best_value
        if best_value != -1:
            visited_stages[mask] = best_stages
        return best_value
    
    # Testa todas as combinações possíveis
    best_result = -1
    for mask in range(1 << n):
        value = calculate_dp(mask)
        if value != -1 and len(visited_stages[mask]) == N:
            best_result = max(best_result, value)
    
    return best_result

if __name__ == "__main__":
    
    N = int(input())
    shows_by_stage = []
    for _ in range(N):
        line = list(map(int, input().split()))
        M = line[0]
        shows = []
        idx = 1
        for _ in range(M):
            start, end, value = line[idx:idx+3]
            shows.append((start, end, value))
            idx += 3
        shows_by_stage.append(shows)
    
    
    result = solve_festival(N, shows_by_stage)
    print(result)