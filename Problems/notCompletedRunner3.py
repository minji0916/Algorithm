from collections import Counter

def solution(participant, completion):
    # 1. participant의 counter 구하기
    part_counter = Counter(participant)
    print(type(part_counter))
    print(part_counter)

    # 2. completion의 counter 구하기
    comp_completion = Counter(completion)

    # 3. 둘의 차를 구하고, key 읽기
    answer = part_counter - comp_completion
    print("answer: ", answer)
    print("answer.keys(): ", answer.keys())
    print("list(answer.keys()): ", list(answer.keys()))
    print("list(answer.keys())[0]: ", list(answer.keys())[0])

    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


def simple_solution(participant, completion):

    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(simple_solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))