

def parse(code):
    rowcode = code[:7].replace('F', '0').replace('B', '1')
    row = int(rowcode, 2)
    colcode = code[7:].replace('L', '0').replace('R', '1')
    col = int(colcode, 2)

    return row * 8 + col

with open('p5.txt', 'r') as f:
    input_s = f.read()

max_seatid = 0
for code in input_s.split('\n'):
    seatid = parse(code)
    if seatid > max_seatid:
        max_seatid = seatid

print(max_seatid)