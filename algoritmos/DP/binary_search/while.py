lista = [0, 2, 3, 5, 6, 13, 15]
lista.sort()
target = 15

def binary(lista, target):
  left, right = 0, len(lista)-1

  while left <= right:
    mid = (left+right) // 2
    if lista[mid] == target:
      return mid
    elif lista[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

print(binary(lista, target))