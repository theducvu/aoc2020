with open('p8.txt', 'r') as f:
    input_s = f.read()

instructions = []
for ins in input_s.split('\n'):
    instr, count = ins.split()
    if count[0] == '-':
        count = -int(count[1:])
    else:
        count = int(count[1:])
    instructions.append((instr, count))

current = 0

acc = 0
alreadyrun = []
looping = False

while True:
    if current in alreadyrun:
        looping = True
        break
    if current >= len(instructions):
        break
    alreadyrun.append(current)
    ins, cnt = instructions[current]
    if ins == 'nop':
        current += 1
    elif ins == 'acc':
        acc += cnt
        current += 1
    elif ins == 'jmp':
        current += cnt

print(acc)