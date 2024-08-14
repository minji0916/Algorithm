import itertools
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
_list = sorted(list(map(int, input().split())))

# product : 동일한 요소를 여러 번 선택해서 뽑아도 됨
prod = itertools.product(_list, repeat=M)
for p in prod:
    print(" ".join(map(str, p)))