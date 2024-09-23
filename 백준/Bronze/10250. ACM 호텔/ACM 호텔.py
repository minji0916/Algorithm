import math
t = int(input()) # 몇개의 테스트 케이스인지
for _ in range(t):
    h,m,n = map(int, input().split())
    new_h = n%h
    new_h = (h if new_h==0 else new_h)
    new_m = math.ceil(n/h)
    print(new_h*100+new_m)