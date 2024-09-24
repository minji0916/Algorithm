import string
aList = list(string.ascii_lowercase)
cntList = [-1]*len(aList)
s_arr = list(input())
for i, a in enumerate(aList):
    if a in s_arr:
        a_i = s_arr.index(a)
        if cntList[i] == -1:
            cntList[i] = a_i

for c in cntList:
    print(c, end=" ")