def expand_dna(sequence):
    expanded = ''
    for char in sequence:
        if char.islower():
            expanded += char.upper() * 2  # Expande a letra minúscula para duas maiúsculas
        else:
            expanded += char  # Mantém a letra maiúscula como está
    return expanded

seq1 = input().strip()
seq2 = input().strip()

seq1 = expand_dna(seq1)
seq2 = expand_dna(seq2)

# Define m e n
m, n = len(seq1), len(seq2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

i = 1
while i <= m:
    j = 1
    while j <= n:
        if seq1[i-1] == seq2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        j += 1
    i += 1

print(dp[m][n])
