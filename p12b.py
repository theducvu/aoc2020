with open('p12.txt', 'r') as f:
    input_s = f.read().split('\n')


named_to_dir = {
    'E': (1, 0),
    'N': (0, 1),
    'W': (-1, 0),
    'S': (0, -1)
}
position = [0, 0]
waypoint = [10, 1]

"""    0,1
        |
        |
-1,0----O----1,0
        |
        |
       0,-1
"""

for cmd in input_s:
    dir_ = cmd[0]
    val = int(cmd[1:])
    x, y = waypoint
    if dir_ == 'R' or dir_ == 'L':
        relative_angle = val if dir_ == 'L' else -val % 360
        if relative_angle == 90:
            waypoint = (-y, x)
        elif relative_angle == 180:
            waypoint = (-x, -y)
        elif relative_angle == 270:
            waypoint = (y, -x)

    else:
        if dir_ == 'F':
            position = [position[0] + waypoint[0] * val, position[1] + waypoint[1] * val]
        else:
            mydir = named_to_dir[dir_]
            waypoint = (x + mydir[0] * val, y + mydir[1] * val)
    print(position, waypoint)

print(abs(position[0]) + abs(position[1]))

