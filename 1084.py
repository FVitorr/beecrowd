import sys

def maior_premio(N, D, numero):
    pilha = []  # Pilha para armazenar os dígitos do maior número possível
    remover = D  # Quantidade de dígitos que ainda precisamos remover

    i = 0
    while i < N:
        # Enquanto a pilha não está vazia e ainda podemos remover números menores
        while pilha and remover > 0 and pilha[-1] < numero[i]:
            pilha.pop()
            remover -= 1
        
        # Adiciona o próximo número na pilha
        pilha.append(numero[i])
        i += 1

    # O resultado final terá exatamente (N-D) dígitos
    resultado = ''.join(pilha[:N - D])
    
    return resultado

# Leitura da entrada
while True:
    # Lê N e D
    linha = sys.stdin.readline().strip()
    if linha == "0 0":
        break  # Termina o programa

    N, D = map(int, linha.split())  # Converte para inteiros

    # Lê o número digitado na lousa
    numero = sys.stdin.readline().strip()

    # Resolve o problema e imprime a saída
    print(maior_premio(N, D, numero))
