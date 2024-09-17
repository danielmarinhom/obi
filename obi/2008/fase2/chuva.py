#norte, usl, leste e oeste
#bfs

#Xi, Yi, Xf e Yf - posicao atual e final
#n - indicando o numero de areas cobertas na fabrica
#n linhas seguintes - X1, Y1, X2 e Y2 - indincaod uma regiao coberta
#uma regiao coberta eh um retangulo de lados paralelos aos eixos tal que 

xi, yi, xf, yf = list(map(int, input().split()))
n = int(input())
areas_cobertas = [(list(map(int,input().split()))) for _ in range(n)]

def esta_coberto(x, y, areas_cobertas):
  for x1,y1,x2,y2 in areas_cobertas:
    if x1 <= x <= x2 and y1 <= y <= y2:
      return True
  return False

def bfs(xi, yi, xf, yf, areas_cobertas):
  queue = [(xi, yi, 0)]
  visited = set([(xi,yi)])
  directions = [(0,-1), (0,1), (1,0), (-1,0)]
  while queue:
    x, y, distancia = queue.pop(0)
    if x == xf and y == yf:
      return distancia
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      if 0 <= nx <= 10**6 and 0 <= ny <= 10**6 and (nx, ny) not in visited:
        visited.add((nx, ny))
        if not esta_coberto(nx,ny,areas_cobertas):
          queue.append((nx,ny,distancia+1))
        else:
          queue.append((nx,ny,distancia))

print(bfs(xi,yi,xf,yf,areas_cobertas))