def solution(n):
    # 약수 3개 이상인 수 리스트
    three_yaksu_num = []
    
    # 4~n이하의 수를 한 번씩 돌기 (4부터 약수 3개)
    for i in range(4,n+1):
        #약수 set 초기화
        yaksu_set = {1,i}
        
        # 2 x (i-1)==i / 3 x (i-2) == i ...
        for gop_num1 in range(2,i+1):
            for gop_num2 in range(i-1,0,-1):
                #print(f"check : {gop_num1}*{gop_num2}=={i}")
                if gop_num1*gop_num2 == i:
                    #set에 없으면 넣기
                    if gop_num1 not in yaksu_set:
                        yaksu_set.update([gop_num1, gop_num2])
                        #print("yaksu_set:",yaksu_set)
                    else:
                        break
        if len(yaksu_set) >= 3:
            three_yaksu_num.append(i)
            #print(three_yaksu_num)
    
                        
    return len(three_yaksu_num)
        
    
    

