#inserções, exclusões, substituições necessárias para transformar uma string em outra

def edit(stringA, stringB):
  lenA = len(stringA)
  lenB = len(stringB)
  dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
  # coluna exclusao
  for i in range(lenA + 1):
    dp[i][0] = i

  # linha insercao
  for j in range(lenB + 1):
    dp[0][j] = j

  # preenchendo o resto
  for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
      dp[i][j] = min(dp[i-1][j] + 1,      # exclusao
                     dp[i][j-1] + 1,      # insercao
                     dp[i-1][j-1] + (1 if stringA[i-1] != stringB[j-1] else 0)  # substituicao
                     )
  for k in dp:
    print(k)
  return dp[lenA][lenB]
stringA = 'kitten'
stringB = 'sitting'
print(edit(stringA, stringB))
