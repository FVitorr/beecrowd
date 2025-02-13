// Nome(s) Discente(s): Vitor Augusto Alves Ferreira
// Matrícula(s): 0070315
// Data: 12-02-2025


// Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que 
//foram fornecidas pelo professor foram desenvolvidas por mim. Declaro também que
// sou responsável por todas  as eventuais cópias deste programa e que não distribui nem facilitei a 
//distribuição de cópias.

##########################################################################################################################################

# Este código implementa a solução do problema da Mochila (Knapsack) usando programação dinâmica com espaço linear.
# A função 'knapsack_linear_space' calcula o valor máximo que pode ser obtido com um conjunto de itens e uma capacidade máxima de mochila.
# Essa implementação utiliza uma versão otimizada do algoritmo de Mochila com uma tabela unidimensional (reduzindo o espaço utilizado).
# O tempo de execução do algoritmo é calculado e impresso.
# O código também inclui a leitura de instâncias do problema a partir de arquivos de entrada, e para cada instância, executa o algoritmo de Mochila.
# As instâncias de entrada estão localizadas nas pastas 'low-dimensional' e 'large-scale'.
# Este código faz uso de dados externos nos arquivos localizados em 'Instances_01/low-dimensional/' e 'Instances_01/large-scale/'.


import time

def knapsack_linear_space(items, L):
    start_time = time.time()
    n = len(items)
    # Cria uma tabela unidimensonal para armazenar os resultados parciais
    dp = [0] * (L + 1)

    # Preenche a tabela de programação dinâmica (com espaço otimizado)
    for i in range(n):
        for w in range(L, items[i][0] - 1, -1):  # Preenche de trás para frente para evitar sobrescrever resultados
            dp[w] = max(dp[w], dp[w - items[i][0]] + items[i][1])

    print(f"Tempo Final: {(time.time() - start_time)}\n Capacidade: {L} Quantidade de itens: {n}")
    return dp[L]


def read_knapsack_instance(filename):
    # Abre o arquivo e lê as informações
    with open(filename, 'r') as file:
        # Lê a primeira linha: n e wmax
        n, wmax = map(int, file.readline().split())
        
        items = []
        for _ in range(n):
            vi, wi = map(int, file.readline().split())
            items.append((wi, vi))  # Armazenar como (peso, utilidade)
    
    return items, wmax


low_dimensional = ["f1_l-d_kp_10_269", "f2_l-d_kp_20_878", "f3_l-d_kp_4_20", "f4_l-d_kp_4_11",
                   "f6_l-d_kp_10_60", "f7_l-d_kp_7_50", "f8_l-d_kp_23_10000", "f9_l-d_kp_5_80", "f10_l-d_kp_20_879"]

large_scale = ["knapPI_1_100_1000_1", "knapPI_1_200_1000_1","knapPI_1_500_1000_1", "knapPI_1_1000_1000_1", "knapPI_1_2000_1000_1", "knapPI_1_5000_1000_1", "knapPI_1_10000_1000_1", "knapPI_2_100_1000_1", "knapPI_2_200_1000_1","knapPI_2_500_1000_1", "knapPI_2_1000_1000_1", "knapPI_2_2000_1000_1", "knapPI_2_5000_1000_1", "knapPI_2_10000_1000_1","knapPI_3_100_1000_1", "knapPI_3_200_1000_1","knapPI_3_500_1000_1", "knapPI_3_1000_1000_1", "knapPI_3_2000_1000_1", "knapPI_3_5000_1000_1", "knapPI_3_10000_1000_1"]


#filename = "Instances_01/large_scale/knapPI_1_100_1000_1"


for i in range(len(low_dimensional)):
    print("\n________________________________________________________")
    filename = "Instances_01/low-dimensional/" + low_dimensional[i]
    items, L = read_knapsack_instance(filename)

    print("Arquivo:", filename)
    result = knapsack_linear_space(items, L)
    print("MAX:", result)


for i in range(len(large_scale)):
    print("\n________________________________________________________")
    filename = "Instances_01/large_scale/" + large_scale[i]
    items, L = read_knapsack_instance(filename)

    print("Arquivo:", filename)
    result = knapsack_linear_space(items, L)
    print("MAX:", result)

