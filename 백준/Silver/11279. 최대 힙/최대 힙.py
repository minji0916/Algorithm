import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())

    if num>0:
        # 최대힙을 만들기 위해서 원래 값에 '-'
        heapq.heappush(heap, -(num))
    if num==0:
        if len(heap)>0:
            print(-heapq.heappop(heap)) # 출력할 땐, 다시 원래 값으로 (-)
        else:
            print(0)
        