num_number = int(input("숫자의 개수: "))
numbers = input("공백 없이 주어진 N개의 숫자: ")
hap = 0

for n in numbers:
    hap += int(n)

print(hap)