n = int(input())
def primo(n):
  if n%2 == 0:
    return "nao"
  for i in range(3, int(n**0.5) + 1, 2):
    if n%i == 0:
      return "nao"
  return "sim"
print(primo(n))