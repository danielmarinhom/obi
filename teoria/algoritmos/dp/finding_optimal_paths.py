'''
[ se o comeco for o 0, para chegar no 3, o caminho otimo seria:
[1,1,3]   p[0][2] = 3 + max/min(p[0][1], p[1][2]), generalizando,
[2,2,1]   p[i][j] = v[i][j] + max/min(p[i][j-1], p[i+1][j])
[0,3,2]
]
'''