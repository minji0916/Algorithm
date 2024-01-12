def solution(participant, completion):
    
    # 1. 리스트 정렬
    participant.sort()
    completion.sort()
    print("participant: ", participant)
    print("completion: ", completion)
    
    # 2. completion 기준으로 비교
    for idx in range(len(completion)):
        if participant[idx] != completion[idx]:
            return participant[idx]
    
    # 3. 만약 모두 비교했는데, 없으면 participant의 마지막 요소가 정답
    return participant[-1]

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])