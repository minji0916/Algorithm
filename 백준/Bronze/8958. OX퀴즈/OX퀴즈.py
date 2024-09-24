for _ in range(int(input())):
    arr = list(input())
    sum = 0
    cnt = 0
    for a in arr:
        if a == 'O':
            cnt +=1
            sum += cnt
        else:
            cnt = 0
    print(sum)