# 1. prime_set을 정의
prime_set = set()

def isPrime(number):
    # 6. 0,1 제외
    if number in (0,1):
        return False
    
    # 7. 에라토스테네스 체 
    lim = int(number ** 0.5 + 1)
    for i in range(2, lim):
        if number % i == 0:
            return False
    return True

# combination : 여태까지 조합된 숫자
# others : 아직 쓰지 않은 숫자
def recursive(combination, others):
    # 5. 탈출 조건 / 비교 조건 : 지금까지 만들어진 조합이 소수인지 판단
    if combination != "":
        if isPrime(int(combination)):
            prime_set.add(int(combination))

    # 4. 현재까지 만들어진 숫자에 남아있는 숫자를 더해준다.
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i+1:])
    

def solution(numbers):
    
    
    
    # 2. 모든 조합을 만드는 recursive를 수행
    ## recursive에서 아직 만들어진 조합은 없는데, 내가 써야하는 숫자는 numbers야.
    recursive("", numbers)


    # prime_set의 length를 반환
    return len(prime_set)

print(solution("17"))