lista = [0, 2, 3, 5, 6, 13, 15]
lista.sort()
target = 15
def binary(lista, left, right, target):
  if left > right:
    return -1
  mid = (left + right) // 2
  if lista[mid] == target:
    return mid
  elif lista[mid] > target:
    return binary(lista, left, mid - 1, target)
  elif lista[mid] < target:
    return binary(lista, mid+1, right, target)
  

print(binary(lista, 0, len(lista)-1, target))