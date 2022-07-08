'''
N个人围成一圈
从第一个开始报数，第M个将被杀掉
接着下一个开始报数，第M个将被杀死
直到最后剩下一个，其余人都将被杀掉。
问哪个位置是安全的？
如果你想验证，这有几个正确答案：
N    M    result
6    5    ([1], [5, 4, 6, 2, 3])
41   3    ([31], [3, 6, 9, 12, 15, 18,21, 24, 27, 30, 33, 36,
                  39, 1, 5, 10, 14, 19,23, 28, 32, 37, 41, 7,
                  13, 20, 26, 34, 40, 8,17, 29, 38, 11, 25, 2,
                  22, 4, 35, 16])
30   9    ([21], [9, 18, 27, 6, 16, 26, 7, 19, 30, 12, 24, 8,
                  22, 5, 23, 11, 29, 17, 10, 2, 28, 25, 1, 4,
                  15, 13, 14, 3, 20])
'''             
def Josephus_ver1(N:int,M:int)->list:
          lists=[i for i in range(1,N+1)]#创建一个从1到N的列表
          L=[]#创建一个空列表 用于存储出列人编号
          index=1
          while(len(lists)!=1):
                    if index+M-1>len(lists):#判断下一个索引是否超出列表长度
                              if (index+M-1)%len(lists):#判断下一个索引是否超出列表长度的整数倍
                                        index = (index+M-1)%len(lists)#索引等于下一个索引对长度取余
                              else:#超出列表长度的整数倍
                                        index = len(lists)#索引等于列表长度
                    else:#没有超出就自增M-1
                              index+=M-1
                    L.append(lists[index-1])
                    lists.pop(index-1)
          return lists,L
Josephus_ver1(6,5)
Josephus_ver1(41,3)
Josephus_ver1(30,9)
