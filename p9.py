with open('p9.txt', 'r') as f:
    input_s = f.read()

numbers = list(map(int, input_s.split('\n')))

preamble_len = 25
preamble = numbers[:preamble_len]

for n in numbers[preamble_len:]:
    if not any([(n - x) in preamble and x != n - x for x in preamble]):
        print(n)
        break
    preamble = preamble[1:] + [n]

    