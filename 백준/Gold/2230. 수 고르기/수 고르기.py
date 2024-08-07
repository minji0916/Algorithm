import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = []
for i in range(N):
    A += map(int,(input().split()))
end = 0
min_diff = 2000000001 
A.sort()

for start in range(N):
    while A[end]-A[start]<M and end<N-1:
        end += 1
    if A[end]-A[start]>=M and A[end]-A[start]<min_diff:
        min_diff = A[end]-A[start]
print(min_diff)