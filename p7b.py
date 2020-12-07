import re

with open('p7.txt', 'r') as f:
    input_s = f.read()

rules = input_s.split('\n')

bag_string_regex = re.compile('([1-9]*)? ?([a-z]+) ([a-z]+) bags?')

def parse_bag(bag_string):
    if bag_string == 'no other bags':
        return None
    match = bag_string_regex.match(bag_string)
    if match:
        num, pattern, colour = match.groups()
        num = int(num) if num.isnumeric() else 1
        # Add count for the bags
        return ((pattern, colour), num)
    else:
        # Shouldn't happen
        raise ValueError("Bag string invalid:", bag_string)

contains_dict = {}
contained_dict = {}

for rule in rules:
    # Remove the period and split at contain
    container, containees = rule[:-1].split(' contain ')
    if ',' in containees:
        # Multiple bags
        containees = containees.split(', ')
    else:
        containees = [containees]
    container = parse_bag(container)[0] # Num should be ignored for container (1)
    containees = [parse_bag(containee) for containee in containees]
    if containees != [None]:
        contains_dict[container] = containees

total_count = 0

# Assume no infinite recursion
def traverse(container_bag, bag_count):
    global contains_dict, total_count
    total_count += bag_count
    if container_bag in contains_dict:
        for containee in contains_dict[container_bag]:
            bag_colour, containee_count = containee
            # Traverse inside the current containee bag
            # to count further
            traverse(bag_colour, bag_count * containee_count)
        

traverse(('shiny', 'gold'), 1)
# Ignore the shiny gold bag itself (-1)
print(total_count - 1)