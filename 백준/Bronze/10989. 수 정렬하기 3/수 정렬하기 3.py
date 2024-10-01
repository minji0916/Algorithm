import sys
input = sys.stdin.readline

n = int(input())
l = [0]*10001

for _ in range(n):
    l[int(input())]+=1

for i,n in enumerate(l):
    if n>0:
        for _ in range(n):
            print(i)