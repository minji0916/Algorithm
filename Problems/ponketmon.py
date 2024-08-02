def solution(nums):
    max_ponketmon = len(nums)/2
    set_nums = list(set(nums))

    if max_ponketmon <= len(set_nums):
        answer = max_ponketmon
    else:
        answer = len(set_nums)

    return answer