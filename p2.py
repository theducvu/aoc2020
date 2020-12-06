with open('p2.txt', 'r') as f:
    s = f.read()

lines = s.split('\n')
valids = 0
for line in lines:
    policy, pw = line.split(': ')
    nums, char = policy.split(' ')
    bot, top = map(int, nums.split('-'))
    if bot <= pw.count(char) <= top:
        valids += 1

print(valids)