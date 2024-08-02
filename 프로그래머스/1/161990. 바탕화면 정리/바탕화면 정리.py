def solution(wallpaper):
    # 변수 초기화
    x = []
    y = []
    
    # wallpaper에서 '#'인 부분 x,y 좌표값 얻기 
    for i, row in enumerate(wallpaper):
        for j, _ in enumerate(row):
            if _ == "#":
                x.append(i)
                y.append(j)
    # (x의 min, y의 min) ~  (x의 max+1, y의 max+1) 까지 드래그
    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)
    
    return [min_x, min_y, max_x+1, max_y+1]