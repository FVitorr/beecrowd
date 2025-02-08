'''Você está num supermercado e está na fila do caixa para comprar alguns produtos.
 Assim que você termina de passar as compras pelo caixa, se lembra que tem várias moedas 
 em seu bolso, algumas repetidas, e fica pensando se com elas dá para pagar exatamente o valor 
 das compras (para assim se livrar destas moedas e ficar com os bolsos mais leves). Você consegue pagar
   o valor exato da conta usando estas moedas?

Entrada
A primeira linha da entrada contém dois números inteiros V (1 ≤ V ≤ 105) e M (1 ≤ M ≤ 103), indicando,
 respectivamente, o valor final da compra e o número de moedas que você tem em seu bolso. 
 A segunda linha contém M números inteiros que descrevem o valor Mi (1 ≤ Mi ≤ 105)de cada moeda existente em seu bolso.

Saída
Seu programa deve imprimir apenas uma linha, contendo apenas um caractere: 
S caso seja possível pagar o valor exato da conta usando apenas suas moedas, ou N caso contrário.
'''

# Leitura da entrada
V, M = map(int, input().split())
moedas = list(map(int, input().split()))

dp = [False] * (V + 1)
dp[0] = True  

i = 0
while i < len(moedas):
    moeda = moedas[i]
    j = V
    while j >= moeda:
        if dp[j - moeda]:
            dp[j] = True
        j -= 1
    i += 1


print('S' if dp[V] else 'N')



