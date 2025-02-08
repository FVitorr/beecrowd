#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main() {
    int V, M;
    
    scanf("%d %d", &V, &M);
    
    int* moedas = (int*) malloc(M * sizeof(int));
    
    for (int i = 0; i < M; i++) {
        scanf("%d", &moedas[i]);
    }
    
    bool* dp = (bool*) malloc((V + 1) * sizeof(bool));
    
    for (int i = 0; i <= V; i++) {
        dp[i] = false;
    }
    dp[0] = true;
    
    for (int i = 0; i < M; i++) {
        int moeda = moedas[i];
        
        for (int valor = V; valor >= moeda; valor--) {
            if (dp[valor - moeda]) {
                dp[valor] = true;
            }
        }
    }
    
    // Imprime o resultado
    if (dp[V]) {
        printf("S\n");
    } else {
        printf("N\n");
    }
    
    // Libera a memória alocada
    free(moedas);
    free(dp);
    
    return 0;
}

