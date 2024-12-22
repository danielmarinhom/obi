def is_palindrome(string):
  return string == string[::-1]
def longest(string):
  n = len(string)
  max_length = 0
  start_index = 0
  for start in range(n):
    for end in range(start, n):
      substring = string[start:end+1]
      if is_palindrome(substring):
        current_length = end-start+1
        if current_length > max_length:
          max_length = current_length
          start_index = start
  return string[start_index:start_index + max_length], max_length
print(longest("abcd"))
