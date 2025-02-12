
####################################### Implementação da Mochila ########################################################

#Dado um conjunto Cn de n itens, representado por Cn = {1,2,…,n} em que cada i e cn tem um peso pi e 
#utilidade ui(pi>0 ui>0). desejamos determinar um subconjunto S dos itens, tal que a soma dos pesos dos elementos 
#de S seja menor ou igual à capacidade da mochila L e que a utilidade total dos elementos S seja a maior possível.

#########################################################################################################################

import time

def knapsack(items, L):
    start_time = time.time()
    n = len(items)
    dp = [[0] * (L + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(L + 1):
            if items[i - 1][0] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    print(f"Tempo Final: {(time.time() - start_time)}\n Capacidade: {L} Quantidade de itens: {n}")
    return dp[n][L]


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


#filename = "Instances_01/large_scale/knapPI_1_100_1000_1"


for i in range(len(low_dimensional)):
    print("\n________________________________________________________")
    filename = "Instances_01/low-dimensional/" + low_dimensional[i]
    items, L = read_knapsack_instance(filename)

    print("Arquivo:", filename)
    result = knapsack(items, L)
    print("MAX:", result)

