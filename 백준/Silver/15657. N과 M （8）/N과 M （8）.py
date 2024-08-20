import itertools
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
_list = sorted(list(map(int, input().split())))

# combinations_with_replacement : 중복 허용, 순서는 고려하지 않음
comb = itertools.combinations_with_replacement(_list, M)
for c in comb:
    print(" ".join(map(str, c)))