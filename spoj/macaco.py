n = int(input())
retangulos = []
for _ in range(n):
  #x,y canto superior esquerdo
  #u,v canto inferior direito
  x,y, u,v = map(int,input().split())
  retangulos.append((x,y,u,v))

#coordenadas do retangulo de interseccao encontrada, caso seja vazia a segunda liha deve ser "nenhum"
