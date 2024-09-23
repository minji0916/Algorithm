t = int(input())

for _ in range(t):
    p=""
    r, s = input().split()
    for a in s:
        for i in range(int(r)):
            p += a
    print(p)