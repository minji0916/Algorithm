n = int(input())
world_nums = []

for i in range(6669999):
    if '666' in str(i):
        world_nums.append(i)

print(world_nums[n-1])
