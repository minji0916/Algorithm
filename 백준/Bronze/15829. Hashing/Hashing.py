n = int(input())
az = 'abcdefghijklmnopqrstuvwxyz'
s_list = input()
M = 1234567891
H=0
for i, s in enumerate(s_list):
    ai = az.find(s)+1
    r = 31**i
    H+=(ai*r)
print(H%M)
