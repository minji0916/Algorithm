N = int(input())

def findDivSum(N):
    for i in range(1,N):
        div_sum = i
        for s_i in str(i):
            div_sum += int(s_i)

        if div_sum==N:
            return i
    return 0

print(findDivSum(N))