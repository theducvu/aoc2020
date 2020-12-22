with open('p11.txt', 'r') as f:
    input_s = f.read()
    input_s = input_s.replace('L', '#')
    seats = [list(s) for s in input_s.split('\n')]


def update_seats(seats):
    changed = []
    rowcount = len(seats)
    colcount = len(seats[0])
    for i in range(rowcount):
        for j in range(colcount):
            if seats[i][j] == '.':
                continue
            occupied = 0
            allowedcols = allowedrows = [-1, 0, 1]
            if i == 0:
                allowedrows = [0, 1]
            elif i == rowcount - 1:
                allowedrows = [-1, 0]
            if j == 0:
                allowedcols = [0, 1]
            elif j == colcount - 1:
                allowedcols = [-1, 0]
            for x in allowedrows:
                shouldbreak = 0
                for y in allowedcols:
                    if not(x == y == 0):
                        occupied += int(seats[i+x][j+y] == '#')
                    if occupied > 3:
                        if seats[i][j] == '#':
                            # seats[i][j] = 'L'
                            changed += [(i,j)] 
                        shouldbreak = 1
                        break
                if shouldbreak: break
            if occupied == 0 and seats[i][j] == 'L':
                # seats[i][j] = '#'
                changed += [(i,j)] 
    for seat in changed:
        i, j = seat
        seats[i][j] = 'L' if seats[i][j] == '#' else '#'
    changed = len(changed) > 0
    return seats, changed

iterations = 0
while True:
    iterations += 1
    seats, changed = update_seats(seats)
    # final_s = '\n'.join([''.join(s) for s in seats])
    # print(final_s)
    # print("\n")
    if not changed:
        break
print(iterations)
final_s = '\n'.join([''.join(s) for s in seats])
print(final_s.count('#'))