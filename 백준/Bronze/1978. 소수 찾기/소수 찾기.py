import math

n = int(input())
_list = list(map(int, input().split()))
count=0

def is_prime_number(x):
    for i in range(2,int(math.sqrt(x)) + 1):
        if x%i==0:
            return 0
    return 1

for l in _list:
    if l==1:
        pass
    elif l==2:
        count+=1
    else:
        count += is_prime_number(l)

print(count)