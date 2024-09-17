#ela só responde
#uma mensagem como resposta
#só tem outra mensagem depois da resposta
#mensagem instantanea, chamadas de eventos
#R X - Recebido por X
#E X - Enviada pra X
#T X - Intervalo entre eventos
#se T X não existe, T=1
#Tempo de resposta = recebimento + envio da resposta
# se repostas = recebimentos, Tempo de resposta toal = soma dos tempos de resposta, senao, =-1

registros = []
numero_registros = int(input(" > "))

print("--------")
if(numero_registros < 1 or numero_registros > 20):
  print("INVALIDO")
  exit()

for _ in range(numero_registros):
  atual = []
  atual = input(" > ").split()
  registros.append(atual)
  
print(registros)



