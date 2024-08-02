def solution(n):
    answer = ''
    pattern_string = '수박'
    answer = pattern_string * (n//2)
    if n%2:
        answer += pattern_string[0]

    return answer