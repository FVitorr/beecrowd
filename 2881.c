#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SHOWS 1000
#define MAX_STAGES 10
#define MAX_MASK (1 << 12)  // Suporta até 12 shows no total

// Estrutura para representar um show
typedef struct {
    int start;
    int end;
    int value;
    int stage;
} Show;

// Estrutura para armazenar os estágios visitados
typedef struct {
    int stages[MAX_STAGES];
    int count;
} VisitedStages;

// Estrutura para armazenar o DP
typedef struct {
    int value;
    VisitedStages stages;
    int calculated;
} DPState;

// Variáveis globais para evitar passar muitos parâmetros
Show all_shows[MAX_SHOWS];
int n_shows = 0;
DPState dp[MAX_MASK];
int N;

// Função para verificar se dois shows são compatíveis
int are_compatible(Show show1, Show show2) {
    return show1.start >= show2.end || show2.start >= show1.end;
}

// Função para copiar estrutura VisitedStages
VisitedStages copy_visited_stages(VisitedStages src) {
    VisitedStages dest;
    memcpy(dest.stages, src.stages, sizeof(src.stages));
    dest.count = src.count;
    return dest;
}

// Função para adicionar um estágio aos visitados
void add_stage(VisitedStages* stages, int stage) {
    int i;
    for (i = 0; i < stages->count; i++) {
        if (stages->stages[i] == stage) return;
    }
    stages->stages[stages->count++] = stage;
}

// Função para contar estágios visitados
int count_stages(VisitedStages stages) {
    int count = 0;
    int visited[MAX_STAGES] = {0};
    int i;
    
    for (i = 0; i < stages.count; i++) {
        if (!visited[stages.stages[i]]) {
            visited[stages.stages[i]] = 1;
            count++;
        }
    }
    return count;
}

// Função principal de programação dinâmica
int calculate_dp(int mask) {
    int curr_pos, other_pos, remaining_mask, prev_value, new_value;
    int compatible;
    
    // Se já calculado, retorna o valor
    if (dp[mask].calculated) {
        return dp[mask].value;
    }
    
    // Caso base
    if (mask == 0) {
        dp[mask].value = 0;
        dp[mask].stages.count = 0;
        dp[mask].calculated = 1;
        return 0;
    }
    
    int best_value = -1;
    VisitedStages best_stages;
    best_stages.count = 0;
    
    curr_pos = 0;
    while (curr_pos < n_shows) {
        if (mask & (1 << curr_pos)) {
            remaining_mask = mask ^ (1 << curr_pos);
            
            compatible = 1;
            other_pos = 0;
            while (other_pos < n_shows && compatible) {
                if (remaining_mask & (1 << other_pos)) {
                    if (!are_compatible(all_shows[curr_pos], all_shows[other_pos])) {
                        compatible = 0;
                    }
                }
                other_pos++;
            }
            
            if (compatible) {
                prev_value = calculate_dp(remaining_mask);
                if (prev_value != -1) {
                    new_value = prev_value + all_shows[curr_pos].value;
                    VisitedStages new_stages = copy_visited_stages(dp[remaining_mask].stages);
                    add_stage(&new_stages, all_shows[curr_pos].stage);
                    
                    if (new_value > best_value) {
                        best_value = new_value;
                        best_stages = new_stages;
                    }
                }
            }
        }
        curr_pos++;
    }
    
    dp[mask].value = best_value;
    dp[mask].stages = best_stages;
    dp[mask].calculated = 1;
    return best_value;
}

int solve_festival() {
    int mask;
    int best_result = -1;
    int value;
    
    // Inicializa o DP
    memset(dp, 0, sizeof(dp));
    
    mask = 0;
    while (mask < (1 << n_shows)) {
        value = calculate_dp(mask);
        if (value != -1 && count_stages(dp[mask].stages) == N) {
            if (value > best_result) {
                best_result = value;
            }
        }
        mask++;
    }
    
    return best_result;
}

int main() {
    int i, j, M;
    
    scanf("%d", &N);
    
    // Lê os shows de cada palco
    for (i = 0; i < N; i++) {
        scanf("%d", &M);
        for (j = 0; j < M; j++) {
            scanf("%d %d %d", 
                  &all_shows[n_shows].start,
                  &all_shows[n_shows].end,
                  &all_shows[n_shows].value);
            all_shows[n_shows].stage = i;
            n_shows++;
        }
    }
    
    int result = solve_festival();
    printf("%d\n", result);
    
    return 0;
}