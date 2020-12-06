with open('p2.txt', 'r') as f:
    s = f.read()

lines = s.split('\n')
valids = 0
for line in lines:
    policy, pw = line.split(': ')
    nums, char = policy.split(' ')
    bot, top = map(int, nums.split('-'))
    cb = pw[bot-1]
    ct = pw[top-1]
    if [cb, ct].count(char) == 1:
        valids += 1

print(valids)