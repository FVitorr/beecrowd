from itertools import product

def melhor_selecao(N, palcos):
    # Ordena os shows de cada palco por horário de término
    for i in range(N):
        palcos[i].sort(key=lambda show: show[1])
    
    melhor_pontuacao = -1
    
    # Gera todas as combinações possíveis escolhendo um show por palco
    for combinacao in product(*palcos):
        combinacao = sorted(combinacao, key=lambda show: show[1])  # Ordena por horário de término
        
        # Verifica se há sobreposição de horários
        valido = True
        ultima_fim = 0
        total_musicas = 0
        
        for inicio, fim, musicas in combinacao:
            if inicio < ultima_fim:  # Sobreposição detectada
                valido = False
                break
            total_musicas += musicas
            ultima_fim = fim
        
        if valido:
            melhor_pontuacao = max(melhor_pontuacao, total_musicas)
    
    return melhor_pontuacao

# Entrada de dados
N = int(input())
palcos = []

for _ in range(N):
    dados = list(map(int, input().split()))
    Mi = dados[0]
    shows = [tuple(dados[i:i+3]) for i in range(1, len(dados), 3)]
    palcos.append(shows)

# Processamento e saída
print(melhor_selecao(N, palcos))

