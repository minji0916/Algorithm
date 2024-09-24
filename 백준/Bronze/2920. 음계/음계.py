# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed
l = list(map(int, input().split()))
a = sorted(l)
b = sorted(l, reverse=True)

if l == a:
    print("ascending")
elif l == b:
    print("descending")
else:
    print("mixed")