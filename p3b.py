with open('p3.txt', 'r') as f:
    input_s = f.read()

lines = input_s.split('\n')

# Because the tree pattern repeats horizontally,
#  a slope of (3,-1) will encounter the same cells
#  as if it was looping around the border

# Part B:
# Same thing, but we keep a dictionary
# for each slope

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

current_column = {
    slope: 0 for slope in slopes
}
ntrees = {
    slope: 0 for slope in slopes
}

line_length = len(lines[0])

mul = 1
for slope in slopes:
    stepx, stepy = slope
    for row in range(0, len(lines), stepy):
        if lines[row][current_column[slope] % line_length] == '#':
            ntrees[slope] += 1
        current_column[slope] += stepx
    mul *= ntrees[slope]

print(mul)
