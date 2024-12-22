#por exemplo se temos [1,2,3,4,5], as subsequencias CONTIGUAS podem ser:
#[1],[2],[3],[4],[5],[1,2],[2,3],[3,4],[4,5],[1,2,3],[2,3,4],[3,4,5],[1,2,3,4]

def kadane(array):
  max_so_far = float('-inf')  #menor valor possivel
  max_ending_here = 0 #soma da subsequencia atual
  for num in array:
    max_ending_here += num #adiciona o elemento atual a soma da subsequencia
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here  #atualiza a maior soma encontrada ate agora
    if max_ending_here < 0:
      max_ending_here = 0 #redefine soma da subsequencia caso seja negativa
  return max_so_far
