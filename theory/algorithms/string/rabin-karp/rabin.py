def rabin_karp(texto, padrao):
  n = len(texto)
  m = len(padrao)
  b = 256   # numero de caracters possiveis no ascii
  q = 101   # numero primo para verificacao do modulo (pode ser qualquer um)
  p_hash = 0  # hash do padrao
  t_hash = 0   # has do text
  h = 1

  for i in range(m-1):
    h = (h * b) % q #b^(m-1) % q
  for i in range(m):
    p_hash = (b * p_hash + ord(padrao[i])) %q
    t_hash = (b * t_hash + ord(texto[i])) %q
  
  resultado = []
  for i in range(n-m+1):
    if p_hash == t_hash:
      if texto[i:i+m] == padrao:
        resultado.append(i)
    if i < n-m:
      t_hash = (b * (t_hash - ord(texto[i]) * h) + ord(texto[i + m])) % q
      if t_hash < 0:
        t_hash += q
  return resultado


def mine(texto, padrao):
  #abracadabra
  #abra
  index = []
  for i in range(len(texto)):
    if texto[i:i+len(padrao)] == padrao:
      index.append(i)
  return index
print(mine("aabrapipa", "abra"))
print(rabin_karp("abracadabra", "abra"))
  