a,b,v = map(int, input().split())

v-=a
day=1

if v>0:
    if v>(a-b):
        day += v//(a-b)
        v%=(a-b)
        if v>0:
            day+=1

    else:
        day+=1

print(day)