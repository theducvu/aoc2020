with open('p12.txt', 'r') as f:
    input_s = f.read().split('\n')

facing = 0  
angle_to_dir = {
    0: (1, 0),    # E / right
    90: (0, 1),   # N / up
    180: (-1, 0), # W / left
    270: (0, -1)  # S / down
}
named_to_dir = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1)
}
position = [0, 0]

for cmd in input_s:
    dir_ = cmd[0]
    val = int(cmd[1:])
    if dir_ == 'R':
        facing = (facing - val) % 360
    elif dir_ == 'L':
        facing = (facing + val) % 360
    else:
        if dir_ == 'F':
            mydir = angle_to_dir[facing]
        else:
            mydir = named_to_dir[dir_]
        position[0] += mydir[0] * val
        position[1] += mydir[1] * val

print(abs(position[0]) + abs(position[1]))

