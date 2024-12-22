x,y = map(int,input().split())
lim1, lim2 = (0,0), (432, 468)
limx = (0, 432)
limy = (0, 468)
def dentro(x,y, limx, limy):
  return "fora" if x > limx[1] or x < limx[0] or y > limy[1] or y < limy[0] else "dentro"
print(dentro(x,y,limx,limy))