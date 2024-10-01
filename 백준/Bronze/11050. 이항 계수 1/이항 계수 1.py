import math

n,r = map(int, input().split())

up=1

for i in range(r):
    up *= (n-i)
print(int(up/math.factorial(r)))