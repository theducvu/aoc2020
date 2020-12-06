with open('p3.txt', 'r') as f:
    input_s = f.read()

lines = input_s.split('\n')

# Because the tree pattern repeats horizontally,
#  a slope of (3,-1) will encounter the same cells
#  as if it was looping around the border

current_column = 0 
ntrees = 0
line_length = len(lines[0])

for line in lines:
    if line[current_column % line_length] == '#':
        ntrees += 1
    current_column += 3

print(ntrees)
