N,S = map(int,input().split())
lst = list(map(int, input().split()))
end = 0      # two pointer
part_sum = lst[0]   # 부분합 초기화
part_sum_len = 111111 # 부분합 길이로 존재할 수 없는 길이(N 최대 길이보다 큼)

for start in range(N):
    while part_sum<S and end<N-1:
        end += 1
        part_sum += lst[end]
        
    if part_sum>=S and part_sum_len>(end-start+1):
        part_sum_len = (end-start+1)
    part_sum -= lst[start]
    
if part_sum_len == 111111:
    part_sum_len = 0

print(part_sum_len)