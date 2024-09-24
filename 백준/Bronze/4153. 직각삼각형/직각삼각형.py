while True:
    _list = sorted(list(map(int, input().split())))
    a = _list[0]
    b = _list[1]
    c = _list[2]
    if a==0 and b==0 and c==0:
        break
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")