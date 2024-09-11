#

x,y = map(int,input().split()) #largura e altura da pagina do album
fotos = []
for _ in range(2):
  largura, altura = map(int,input().split())
  fotos.append((largura,altura))

def encaixar(fotos, x,y):
  album = [x,y]
  
  return "s" or "n"