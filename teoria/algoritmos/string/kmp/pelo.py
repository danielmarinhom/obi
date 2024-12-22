import time
start = time.time()
def detect(pattern, string):
  n, m = len(pattern),len(string)
  index = []
  for i in range(m-n+1):
    intervalo = string[i:i+n]
    if intervalo == pattern:
      index.append(i+1)
  return index
  #return index if index else "ERRO"
  #return False if index < 0 else True

pattern = "a" * 100,
string = pattern * 100000
res = detect(pattern, string)
end = time.time()
print(res)
print(f"TEMPO, {end-start:.7f} segundos")
