#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1000

int pyramid[MAX_N][MAX_N];
int dp[MAX_N][MAX_N];

// Função para calcular o maior prêmio possível começando da base da pirâmide
int calculate_max_prize(int N) {
    // Inicializa a tabela dp com os valores das bolas da última linha
    for (int i = 0; i < N; i++) {
        dp[N-1][i] = pyramid[N-1][i];
    }

    // Preenche a tabela dp de baixo para cima
    for (int i = N-2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            // O valor máximo que pode ser obtido pegando a bola na posição (i, j)
            dp[i][j] = pyramid[i][j] + (dp[i+1][j] > dp[i+1][j+1] ? dp[i+1][j] : dp[i+1][j+1]);
        }
    }

    // O valor máximo que pode ser obtido a partir do topo da pirâmide
    return dp[0][0];
}

int main() {
    int N;
    
    // Lê os casos de teste até encontrar um caso onde N é 0
    while (scanf("%d", &N) && N != 0) {
        // Lê a pirâmide de bolas
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                scanf("%d", &pyramid[i][j]);
            }
        }

        // Calcula e imprime o maior prêmio possível
        printf("%d\n", calculate_max_prize(N));
    }

    return 0;
}
