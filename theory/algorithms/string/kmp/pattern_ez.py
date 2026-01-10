string = 'wqwpeoasdvvvaaa'
pattern = 'vvv'
def index(string, pattern):
  if pattern in string:
    return string.index(pattern[0])
print(index(string,pattern))