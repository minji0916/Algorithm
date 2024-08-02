from collections import deque

n = int(input())

# 1~n까지 카드 리스트 만듦
dq_cards = deque(i for i in range(1,n+1))

# cards 리스트에 1장 남았을 때까지 반복
while len(dq_cards) > 1:
    # 맨 앞의 카드 버림
    dq_cards.popleft()
    # 맨 앞의 카드 맨 뒤로 보냄
    dq_cards.rotate(-1)
        
print(dq_cards.pop())