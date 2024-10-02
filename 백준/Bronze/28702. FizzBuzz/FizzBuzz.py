"""
15의 배수 : FizzBuzz
3의배수(5X) : Fizz
5의 배수(3X) : Buzz
다 아니면 : i
"""
a = []
for i in range(3):
    a.append(input())

for idx,a_str in enumerate(a):
    if a_str.isdigit():
        i = int(a_str)+3-idx

if i%15==0:
    print("FizzBuzz")
elif i%3==0:
    print("Fizz")
elif i%5==0:
    print("Buzz")
else:
    print(i)