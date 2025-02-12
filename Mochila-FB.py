#problema da mochila 0,1 em força bruta

import time

def knapsack_brute_force(items, L):
    start_time = time.time()
    n = len(items)
    max_utility = 0
    
    for mask in range(1 << n):
        weight = 0
        utility = 0
        for i in range(n):
            if mask & (1 << i):
                weight += items[i][0]
                utility += items[i][1]
        
        if weight <= L:
            max_utility = max(max_utility, utility)
    
    print(f"Tempo Final: {(time.time() - start_time)}\n Capacidade: {L} Quantidade de itens: {n}")
    return max_utility


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
    result = knapsack_brute_force(items, L)
    print("MAX:", result)