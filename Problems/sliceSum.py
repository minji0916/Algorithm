N, M = map(int, input("").split())
numbers = list(map(int, input("").split()))

sumList = []
sumList.append(numbers[0]) 

sumSlices = []
for idx in range(1, len(numbers)):
    sumList.append(sumList[idx-1] + numbers[idx])

for z in range(M):
    i, j = map(int, input("").split())
    if i == 1:
        sumSlices.append(sumList[j-1])
    else:
        sumSlices.append(sumList[j-1]-sumList[i-2])

for s in sumSlices:
    print(s)

