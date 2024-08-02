# 그래프 입력 및 초기화
import sys
input = sys.stdin.readline
N, V, M = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# 그래프 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

#######################################
    
# N, M을 공백 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

