import itertools
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
_list = sorted(list(map(int, input().split())))

# permutation : 중복은 없지만, 순서를 구분
permu = itertools.permutations(_list, M)
for p in permu:
    print(" ".join(map(str, p)))