#MANACHER
def manacher(string):
  pre_processed = '#' + '#'.join(string) + '#'
  n = len(pre_processed)
  palindrome_lengths = [0] * n
  center = 0
  right_edge = 0
  for i in range(n):
    mirror_index = 2 * center - i
    if i < right_edge:
      palindrome_lengths[i] = min(right_edge-i, palindrome_lengths[mirror_index])
    while ( i - palindrome_lengths[i] - 1 >= 0 and 
            i + palindrome_lengths[i] + 1 < n and
            pre_processed[i - palindrome_lengths[i] - 1] == pre_processed[i + palindrome_lengths[index] + 1]):
            palindrome_lengths[i] += 1
    if i + palindrome_lengths[i] > right_edge:
      center = i
      right_edge = i + palindrome_lengths[i]
  
  return max(palindrome_lengths)