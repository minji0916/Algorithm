"""
양 끝에서 투 포인터로 시작
두 포인터가 교차되지 않는 start<end 까지만 동작
두 포인터 값 같으면 start+=1 / end-=1
두 포인터 값 다르면 슬라이싱하고, 문자열 역순인 것과 비교
비교해서 다르면 return 2
"""
import sys
input = sys.stdin.readline

def is_palindrome(txt):
    start,end = 0, len(txt)-1

    while start<end:
        # print("="*20)
        # print(f"txt[start]:{txt[start]}, txt[end]:{txt[end]}")
        if txt[start] == txt[end]:
            start+=1
            end-=1
        else:
            # 왼쪽 한칸 없애고 역순이랑 비교
            if txt[start+1:end+1] == txt[start+1:end+1][::-1]:
                return 1
            # 오른쪽 한칸 없애고 역순이랑 비교
            if txt[start:end] == txt[start:end][::-1]:
                return 1
            return 2
    return 0

T = int(input())
for i in range(T):
    print(is_palindrome(input().strip()))


