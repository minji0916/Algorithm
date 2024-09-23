a = int(input())
b = int(input())
c = int(input())

abc = str(a*b*c)
c = [0] * 10 # 0~9까지 횟수

for i in range(10):
    for s in abc:
        if s==str(i):
            c[i] += 1

for i in c:
    print(i)