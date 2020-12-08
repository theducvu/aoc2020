with open('p8.txt', 'r') as f:
    input_s = f.read()

import time
start = time.time()
instructions = []
for ins in input_s.split('\n'):
    instr, count = ins.split()
    if count[0] == '-':
        count = -int(count[1:])
    else:
        count = int(count[1:])
    instructions.append((instr, count))


final_acc = 0
final_swapped = 0

# Recursive function to traverse the instruction list
# and backtrack when 1. hitting a loop
#                 or 2. reaching the end of the list
# In the second case it saves the acc value and immediately escapes.
def recursive_traverse(current, acc, swapped, traveled_list):
    global instructions, final_acc, final_swapped
    
    if current in traveled_list:
        return False
    if current >= len(instructions):
        final_acc = acc
        final_swapped = swapped
        return True
    
    ins, cnt = instructions[current]
    # print(current, len(traveled_list), swapped)

    if ins == 'nop':
        # Try as nop
        res = recursive_traverse(current + 1, acc, swapped, traveled_list + [current])
        if not res and swapped is None:
            # Try switching nop to jmp
            res = recursive_traverse(current + cnt, acc, current, traveled_list + [current])

    elif ins == 'jmp':
        if swapped is None:
            # Try switching jmp to nop first
            res = recursive_traverse(current + 1, acc, current, traveled_list + [current])
            if not res:
                # Back to jmp
                res = recursive_traverse(current + cnt, acc, swapped, traveled_list + [current])

        else:
            res = recursive_traverse(current + cnt, acc, swapped, traveled_list + [current])

    elif ins == 'acc':
        res = recursive_traverse(current + 1, acc + cnt, swapped, traveled_list + [current])
    else:
        raise ValueError("Not supposed to happen! Unknown instruction:", ins)
    
    return res

res = recursive_traverse(0, 0, None, [])
print(res, final_acc, final_swapped)
