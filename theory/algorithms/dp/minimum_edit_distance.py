def edit(stringA, stringB):
  lenA = len(stringA)
  lenB = len(stringB)
  dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]
  #exclusion
  for i in range(lenA + 1):
    dp[i][0] = i

  #insertion
  for j in range(lenB + 1):
    dp[0][j] = j

  for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
      dp[i][j] = min(dp[i-1][j] + 1,      # exclusion
                     dp[i][j-1] + 1,      # insertion
                     dp[i-1][j-1] + (1 if stringA[i-1] != stringB[j-1] else 0)  # substituicao
                     )
  for k in dp:
    print(k)
  return dp[lenA][lenB]
stringA = 'kitten'
stringB = 'sitting'
print(edit(stringA, stringB))
