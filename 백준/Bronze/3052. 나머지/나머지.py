# 수 10개 입력
a = set()

for _ in range(10):
    n = int(input()) % 42
    a.add(n)

# 서로 다른 나머지 몇개인지 확인
print(len(a))

