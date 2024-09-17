#um jogador tem 3 pokemons
n = int(input())
x = int(input())
y = int(input())
z = int(input())
pokemons = [x,y,z]
def evoluir(n,pokemons):
  res = 0
  for pokemon in sorted(pokemons):
    if pokemon < n:
      n -= pokemon
      res += 1
  return res
print(evoluir(n,pokemons))
#4 min e 30 s