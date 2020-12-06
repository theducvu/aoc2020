with open('p1.txt', 'r') as f:
    input_s = f.read()

nums = list(map(int, input_s.split('\n')))

l = len(nums)

for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            if nums[i]+nums[j]+nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
    
