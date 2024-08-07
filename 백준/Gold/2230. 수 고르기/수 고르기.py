"""
N개의 정수로 이루어진 수열 
두 수의 차이가 M 이상일 때, 차이가 가장 작은 경우 print
"""

import sys
input = sys.stdin.readline

# 입력
N,M = map(int, input().split())
A = []
for i in range(N):
    A += map(int,(input().split()))
end = 0
diff = 0
min_diff = 2000000001 # 최소로 될 수 없는 수 (M+1)

# 리스트 정렬
A.sort()

# start=0, end=0부터 시작
# 1. A[end]-A[start] < M : end를 한칸 뒤로 
# 2. A[end]-A[start] >= M : 두 개의 차이 구해서 min_diff보다 작은 경우 update
# start를 한 칸씩 전진하면서 1,2 과정 반복 

for start in range(N):
    while A[end]-A[start]<M and end<N-1:
        end += 1
    if A[end]-A[start]>=M and A[end]-A[start]<min_diff:
        min_diff = A[end]-A[start]

print(min_diff)