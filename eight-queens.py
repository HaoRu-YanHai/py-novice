"""
八皇后问题：
在8×8格的国际象棋上摆放8个皇后，使其不能互相攻击
即任意两个皇后都不能处于同一行、同一列或同一斜线上
问有多少种摆法
"""

#笨方法：枚举法
grida = ['a1','a2','a3','a4','a5','a6','a7','a8']
gridb = ['b1','b2','b3','b4','b5','b6','b7','b8']
gridc = ['c1','c2','c3','c4','c5','c6','c7','c8']
gridd = ['d1','d2','d3','d4','d5','d6','d7','d8']
gride = ['e1','e2','e3','e4','e5','e6','e7','e8']
gridf = ['f1','f2','f3','f4','f5','f6','f7','f8']
gridg = ['g1','g2','g3','g4','g5','g6','g7','g8']
gridh = ['h1','h2','h3','h4','h5','h6','h7','h8']
solution = []
solve=0
def judge(solution:list)->bool:
          col1=[i[1] for i in solution]
          
          for i in col1:
                    if col1.count(i) > 1:
                              return False
          for i in solution:
                    x,y = 1,1;
                    while(ord(i[1])-x >= ord('1')):
                              if chr(ord(i[0])+x)+chr(ord(i[1])-x) in solution:
                                        return False
                              x+=1;
                    while(ord(i[1])+y <= ord('8')):
                              if chr(ord(i[0])+y)+chr(ord(i[1])+y) in solution:
                                        return False
                              y+=1;
          print(solution)
          return True
for a in grida:
          for b in gridb:
                    for c in gridc:
                              for d in gridd:
                                        for e in gride:
                                                  for f in gridf:
                                                            for g in gridg:
                                                                      for h in gridh:
                                                                                solution=[a,b,c,d,e,f,g,h]
                                                                                if judge(solution):
                                                                                          solve+=1
print(solve)
