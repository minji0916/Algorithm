import sys
import heapq

input = sys.stdin.readline

# N 입력 받기
N = int(input())

# 최소 힙 초기화
min_heap = []

for _ in range(N):
    # 한 줄의 숫자들을 입력받아 리스트로 변환
    numbers = list(map(int, input().split()))
    
    for num in numbers:
        if len(min_heap) < N:
            # 힙의 크기가 N보다 작으면 숫자를 그냥 추가
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            # 힙의 크기가 N이고, 현재 숫자가 힙의 최소값보다 크면
            # 최소값을 제거하고 현재 숫자를 추가
            heapq.heapreplace(min_heap, num)

# N번째로 큰 수 출력 (최소 힙의 루트 노드)
print(min_heap[0])