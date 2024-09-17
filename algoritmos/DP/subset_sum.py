#Retornando se eh possivel ou nao
def subset_sum(values, target):
  n = len(values) # Número de valores
  dp = [False] * (target + 1) # Inicializa o vetor de DP com False
  dp[0] = True # É sempre possível obter soma 0 sem escolher nenhum item
    
  # Itera sobre cada valor
  for value in values:
    # Atualiza o vetor DP de trás para frente para evitar múltiplas contagens
    for j in range(target, value - 1, -1):
      if dp[j - value]:
        dp[j] = True
    
  # Retorna se o alvo pode ser alcançado
  return dp[target]

#Retornando o indice dos numeros
def subset_sum_indices(values, target):
  seen = {}  # Dicionário para armazenar os valores já vistos e seus índices

    # Itera sobre cada valor na lista juntamente com seu índice
  for i, value in enumerate(values):
    # Calcula o complemento necessário para atingir o target
    needed = target - value   
    # Verifica se o complemento necessário já está no dicionário
    if needed in seen:
      # Se estiver, retorna os índices do complemento e do valor atual
      return seen[needed], i
    # Adiciona o valor atual ao dicionário com seu índice
    seen[value] = i
    
    # Retorna None se não encontrar dois números que somam o target
  return None

values = [2, 7, 11, 15]
target = 17
result = subset_sum_indices(values, target)
if result:
  print(f"Índices dos números que somam {target}: {result}")
else:
  print(f"Não foi possível encontrar dois números que somam {target}.")

