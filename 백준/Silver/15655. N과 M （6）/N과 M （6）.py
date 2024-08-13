import itertools
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
_list = sorted(list(map(int, input().split())))

comb = itertools.combinations(_list, M)
for c in comb:
    print(" ".join(map(str, c)))