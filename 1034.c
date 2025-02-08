#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int T;
    scanf("%d", &T);  // Número de instâncias
    while (T > 0) {
        int N, M;
        scanf("%d %d", &N, &M);  // Lê N e M
        int *blocos = (int *)malloc(N * sizeof(int));  // Lê os blocos disponíveis
        for (int i = 0; i < N; i++) {
            scanf("%d", &blocos[i]);
        }

        int *dp = (int *)malloc((M + 1) * sizeof(int));  // Inicializa dp
        for (int i = 0; i <= M; i++) {
            dp[i] = INT_MAX;  // Inicializa com infinito (valor alto)
        }
        dp[0] = 0;  // Base: comprimento 0 requer 0 blocos

        for (int i = 0; i < N; i++) {  // Iterando pelos tipos de blocos
            int bloco = blocos[i];
            for (int j = bloco; j <= M; j++) {  // Atualizando dp[j] para todos os valores possíveis
                if (dp[j - bloco] != INT_MAX) {
                    dp[j] = (dp[j] < dp[j - bloco] + 1) ? dp[j] : (dp[j - bloco] + 1);
                }
            }
        }

        printf("%d\n", dp[M] != INT_MAX ? dp[M] : -1);    
        free(blocos);
        free(dp);
        T--;  // Decrementa o número de instâncias
    }
    return 0;
}

