def detect(pattern, string):
  m = len(string)
  index = -1
  for i in range(m):
    intervalo = string[i:i+m]
    print(intervalo)
    if intervalo == pattern:
      index = i
  return index+1
  #return False if index < 0 else True

pattern, string = "aaab","aaaaaaab" 

print(detect(pattern, string))