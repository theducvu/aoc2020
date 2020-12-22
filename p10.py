with open('p10.txt', 'r') as f:
    input_s = f.read()

adapters = sorted(map(int, input_s.split('\n')))

current = 0
diff = {}
for n in adapters:
    diff[n - current] = diff.get(n-current, 0) + 1
    current = n

print(diff[1] * (diff[3] + 1))