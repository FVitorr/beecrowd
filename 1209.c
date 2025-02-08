#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_N 1000

int main() {
    int n, m, k;
    while (scanf("%d %d %d", &n, &m, &k) != EOF) {
        int f[MAX_N + 1] = {0};  // Vetor de graus
        bool vis[MAX_N + 1] = {false};  //Vetor de visitados
        bool adj[MAX_N + 1][MAX_N + 1] = {false};  //Matriz de adjacência
        
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            adj[u][v] = adj[v][u] = true;
            f[u]++;
            f[v]++;
        }
        
        int queue[MAX_N];
        int front = 0, rear = 0;
        
        for (int i = 1; i <= n; i++) {
            if (f[i] < k) {
                queue[rear++] = i;
                vis[i] = true;
            }
        }
        
        while (front < rear) {
            int u = queue[front++];
            for (int i = 1; i <= n; i++) {
                if (adj[u][i] && !vis[i]) {
                    f[i]--;
                    if (f[i] < k) {
                        queue[rear++] = i;
                        vis[i] = true;
                    }
                }
            }
        }
        
        int ans[MAX_N];
        int ans_size = 0;
        for (int i = 1; i <= n; i++) {
            if (!vis[i]) {
                ans[ans_size++] = i;
            }
        }
        
        if (ans_size > 0) {
            for (int i = 0; i < ans_size; i++) {
                if (i > 0) printf(" ");
                printf("%d", ans[i]);
            }
            printf("\n");
        } else {
            printf("0\n");
        }
    }
    return 0;
}




