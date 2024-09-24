import math 
N = int(input())    # 참가자 수
t_size = list(map(int, input().split()))    # 사이즈별 주문 수
T, P = map(int, input().split())    # 티셔츠 묶음 수 / 펜 묶음 수 

# 티셔츠를 T장씩 최소 몇 묶음 주문해야하는지 
cnt = 0
for t in t_size:
    if t==0:
        pass
    elif t<=T:
        cnt +=1
    else:
        cnt += math.ceil(t/T)
print(cnt)
# 다음 줄에 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
print(N//P, N%P)
