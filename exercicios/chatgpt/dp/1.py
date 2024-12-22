def longestCommonSubsequence(text1, text2):
  res = 0  
  for i in range(1,len(text2)+1):
    for j in range(len(text1)):
      if text2[i-1] == text1[j]:
        res += 1
      else:
        break
  return res
text1 = 'abcde'
text2 = 'ace'
print(longestCommonSubsequence(text1, text2))