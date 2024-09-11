#begin in top left, objective is on bottom right only moving right and down
memo = {}
def gridTraveler(rows,columns, memo):
  key = (rows,columns)
  if key in memo:
    return memo[key]
  if rows == 1 and columns == 1:
    return 1
  if rows == 0 or columns == 0:
    return 0
  memo[key] = gridTraveler(rows-1,columns, memo) + gridTraveler(rows,columns-1, memo)
  return memo[key]
  
x,y = map(int,input().split())
print(gridTraveler(x,y, memo))