import itertools

n,m = map(int, input().split())
cards = list(map(int, input().split()))
iter = itertools.combinations(cards, 3)
sum_iter = []
for i in iter:
    a = sum(i)
    if m>=a:
        sum_iter.append(sum(i))
sum_iter.sort()
print(sum_iter[-1])