def solve_festival(N, shows_by_stage):
    # Lista para todos os shows com (início, fim, valor, palco)
    all_shows = []
    stage = 0
    while stage < N:
        show_idx = 0
        while show_idx < len(shows_by_stage[stage]):
            start, end, value = shows_by_stage[stage][show_idx]
            all_shows.append((start, end, value, stage))
            show_idx += 1
        stage += 1
    
    def are_compatible(show1, show2):
        # Verifica se dois shows não têm sobreposição de horário
        return show1[0] >= show2[1] or show2[0] >= show1[1]
    
    n = len(all_shows)
    dp = {}
    visited_stages = {}
    
    def calculate_dp(mask):
        if mask in dp:
            return dp[mask]
        
        if mask == 0:
            dp[mask] = 0
            visited_stages[mask] = set()
            return 0
        
        best_value = -1
        best_stages = set()
        
        curr_pos = 0
        while curr_pos < n:
            if mask & (1 << curr_pos):
                remaining_mask = mask ^ (1 << curr_pos)
                curr_show = all_shows[curr_pos]
                
                compatible = True
                other_pos = 0
                while other_pos < n and compatible:
                    if remaining_mask & (1 << other_pos):
                        if not are_compatible(curr_show, all_shows[other_pos]):
                            compatible = False
                    other_pos += 1
                
                if compatible:
                    prev_value = calculate_dp(remaining_mask)
                    if prev_value != -1:
                        new_value = prev_value + curr_show[2]
                        new_stages = visited_stages[remaining_mask].copy()
                        new_stages.add(curr_show[3])
                        
                        if new_value > best_value:
                            best_value = new_value
                            best_stages = new_stages
            curr_pos += 1
        
        dp[mask] = best_value
        if best_value != -1:
            visited_stages[mask] = best_stages
        return best_value
    
    best_result = -1
    mask = 0
    while mask < (1 << n):
        value = calculate_dp(mask)
        if value != -1 and len(visited_stages[mask]) == N:
            best_result = max(best_result, value)
        mask += 1
    
    return best_result

if __name__ == "__main__":
    N = int(input())
    shows_by_stage = []
    
    i = 0
    while i < N:
        line = list(map(int, input().split()))
        M = line[0]
        shows = []
        idx = 1
        j = 0
        
        while j < M:
            start, end, value = line[idx:idx+3]
            shows.append((start, end, value))
            idx += 3
            j += 1
        
        shows_by_stage.append(shows)
        i += 1
    
    result = solve_festival(N, shows_by_stage)
    print(result)




