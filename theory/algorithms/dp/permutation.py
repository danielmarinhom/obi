def permutation(lista:list):
  if len(lista) == 0:
    return []
  elif len(lista) == 1:
    return [lista]
  
  permutations = []

  for i in range(len(lista)):
    current = lista[i]
    remaining = lista[:i] + lista[i+1:]

    for p in permutation(remaining):
      permutations.append([current] + p)
  return permutations