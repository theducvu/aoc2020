with open('p6.txt', 'r') as f:
    input_s = f.read()

groups = input_s.split('\n\n')



print(sum([len(set(list(group.replace('\n', '')))) for group in groups]))