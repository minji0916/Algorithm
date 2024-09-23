t = int(input())

for _ in range(t):
    r,s = input().split()
    for _s in s:
        print(_s*int(r),end="")
    print()