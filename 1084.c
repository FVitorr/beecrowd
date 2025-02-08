#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* maior_premio(int N, int D, char* numero) {
    char* pilha = (char*)malloc(N * sizeof(char));  // Pilha para armazenar os dígitos do maior número possível
    int remover = D;  // Quantidade de dígitos que ainda precisamos remover
    int i = 0, top = 0;

    while (i < N) {
        // Enquanto a pilha não está vazia e ainda podemos remover números menores
        while (top > 0 && remover > 0 && pilha[top - 1] < numero[i]) {
            top--;
            remover--;
        }
        
        // Adiciona o próximo número na pilha
        pilha[top++] = numero[i];
        i++;
    }
    pilha[top - remover] = '\0';  
    char* resultado = (char*)malloc((N - D + 1) * sizeof(char));
    strncpy(resultado, pilha, N - D);
    resultado[N - D] = '\0'; 

    free(pilha);
    return resultado;
}

int main() {

    /**
     * Escreva a sua solução aqui
     * Code your solution here
     * Escriba su solución aquí
     */

    while (1) {
        int N, D;
        scanf("%d %d", &N, &D); // Lê N e D
        if (N == 0 && D == 0) {
            break;  
        }

        char numero[N + 1]; 
        scanf("%s", numero);

        char* resultado = maior_premio(N, D, numero);
        printf("%s\n", resultado);
        free(resultado);
    }

    return 0;
}

