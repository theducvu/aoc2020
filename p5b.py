

def parse(code):
    rowcode = code[:7].replace('F', '0').replace('B', '1')
    row = int(rowcode, 2)
    colcode = code[7:].replace('L', '0').replace('R', '1')
    col = int(colcode, 2)

    return row * 8 + col

with open('p5.txt', 'r') as f:
    input_s = f.read()

seats = []
for code in input_s.split('\n'):
    seats += parse(code),

seats = sorted(seats)

# after sort, every seat is going to have a consistent offset
# from the first seat in the list, until the first (and only) skipped seat
for idx, seat in enumerate(seats):
    if seat - seats[0] != idx:
        print(seat - 1)
        break