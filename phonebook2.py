def solution(phone_book):
    # 1. 전화번호 sorting 한다.
    phone_book.sort()

    # 2. sorting 한 전화번호를 2개씩 확인해서 접두어인지 본다.
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

    # 2-1. (zip 활용) sorting 한 전화번호를 2개씩 확인해서 접두어인지 본다.
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         return False
    # return True
            
print(solution(["6", "12", "6789"]))