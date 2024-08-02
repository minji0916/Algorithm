def solution(phone_book):
    # 1. 비교할 A 선택 
    for i in range(len(phone_book)):
        # 2. 비교할 B 선택
        for j in range(i+1, len(phone_book)):
            # 3. 서로가 서로의 접두어인지 확인
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True
            
print(solution(["6", "12", "6789"]))