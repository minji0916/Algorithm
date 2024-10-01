# 초기화 
_list = [[0]*14 for _ in range(15)]
for i in range(14):
    _list[0][i] = i+1

# 각 층별로 값 넣기
for i in range(1, 15):
    for j in range(14):
        if j==0:
            _list[i][j]=1
        else:
            for n in range(j+1):
                _list[i][j] += _list[i-1][n]

# #층 값 확인
# for i in _list:
#     print(i)

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(_list[k][n-1])