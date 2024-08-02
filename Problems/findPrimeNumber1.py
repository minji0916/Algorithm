from itertools import permutations

"""
    에라토스테네스의 체 : 어떤 수의 소수 여부를 확인할 때는 특정 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구현 가능
    N = 71일 때, 제곱근이 8.xx니까 8의 배수까지만 제거하면 됨
    원래는 2~70까지 돌면서 약수가 있는지 배수를 확인해야하지만, 2~9까지 돌면서 배수 확인하면 됨
    ex) N = 72 = 9 * 8 / N' = N의 제곱근 = 8.xx 
        9 >= N'이면, a*b= N = N' * N' 이기 때문에 b < N'
        따라서 N'가지만 검사하면 합성수를 이루는 a,b 중 작은 수까지는 충분히 체크할 수 있고, 합성수가 존재하지 않으면 소수라고 할 수 있음.                  
"""

def solution(numbers):
    # 중복된 것을 제거하기 위해서 set 사용.
    # 만약 "117"이 들어오면, 17을 조합할 수 있는 경우의 수가 2가지이기 때문에 (첫번째1, 두번째1)
    prime_set = set()
    
    # 1. numbers를 조합해서 모든 숫자 조합을 만듦
    for i in range(len(numbers)):
        # print(list(numbers))   # ['1', '7']

        # ['1', '7']에서 1글자로 조합만들고, 2글자로 조합 만들고 이걸 numbers 길이만큼 반복해라
        numbers_permutation = permutations(list(numbers), i+1)
        # print(list(numbers_permutation)) # [('1',), ('7',)] / [('1', '7'), ('7', '1')]

        # int형으로 바꾸기
        # print(list(map("".join, numbers_permutation)))  # ['1', '7']  /  ['17', '71']
        # print(list(map(int, map("".join, numbers_permutation))))  # [1, 7]  /  [17, 71]
        numbers_perm_list = map(int, map("".join, numbers_permutation))
        
        # 소수 후보 집합에 넣기
        prime_set |= set(numbers_perm_list)

    # print(prime_set) # {1, 71, 17, 7}

    # 2. 소수가 아닌 수를 제거 (에라토스테네스의 체)
    ##   (1을 제외하고, 약수가 1과 자기자신밖에 없는 수)
    prime_set -= set(range(0,2))

    # range의 두번째 인자로 쓰기 위해서 1을 더함
    # prime_set의 max 값의 루트를 씌움
    lim = int(max(prime_set) ** 0.5) + 1

    # 4~71까지 돌면서 2의 배수를 set으로 만듦
    # 6~71까지 돌면서 3의 배수를 set으로 만듦
    # 이걸 lim(8)까지 반복
    for i in range(2, lim):
        prime_set -= set(range(i*2, max(prime_set) + 1, i))
    
    return len(prime_set)

print(solution("17"))