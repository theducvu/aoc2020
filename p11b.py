with open('p11.txt', 'r') as f:
    input_s = f.read()
    input_s = input_s.replace('L', '#')
    seats = [list(s) for s in input_s.split('\n')]

directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def update_seats(seats):
    changed = []
    rowcount = len(seats)
    colcount = len(seats[0])
    for i in range(rowcount):
        for j in range(colcount):
            if seats[i][j] == '.':
                continue
            occupied = 0
            for a, b in directions:
                x, y = i, j
                while True:
                    x += a
                    y += b
                    if x < 0 or x > rowcount - 1 or y < 0 or y > colcount - 1:
                        break
                    
                    if seats[x][y] == '#':
                        occupied += 1
                        break
                    elif seats[x][y] == 'L':
                        break
            if occupied > 4 and seats[i][j] == '#':
                # seats[i][j] will be changed to 'L'
                changed += [(i,j)]
                
            elif occupied == 0 and seats[i][j] == 'L':
                # seats[i][j] will be changed to '#'
                changed += [(i,j)] 
    for seat in changed:
        i, j = seat
        seats[i][j] = 'L' if seats[i][j] == '#' else '#'
    changed = len(changed) > 0
    return seats, changed

iterations = 0
while True:
    iterations += 1
    print('.', end='')
    seats, changed = update_seats(seats)
    # final_s = '\n'.join([''.join(s) for s in seats])
    # print(final_s)
    # print("\n")
    if not changed:
        break
print(iterations)
final_s = '\n'.join([''.join(s) for s in seats])
print(final_s.count('#'))