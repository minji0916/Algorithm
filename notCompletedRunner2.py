def solution(participant, completion):
    hashDict = {}
    sumhash = 0

    # 1. Hash를 Key로 갖고, participant의 이름을 Value로 갖는 Dictionary 만들고 Sum을 구함
    for part in participant:
        hashDict[hash(part)] = part
        sumhash += hash(part)
    print("hashDict: ", hashDict)
    print("sumhash: ", sumhash)

    # 2. 합에서 completion의 hash들의 합을 뺌
    for com in completion:
        sumhash -= hash(com)
    
    # 3. 마지막에 남은 hash가 완주하지 못한 선수의 hash
    return hashDict[sumhash]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))