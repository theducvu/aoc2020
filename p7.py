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
        # Ignore num for first half
        return (pattern, colour)
    else:
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
    container = parse_bag(container)
    containees = [parse_bag(containee) for containee in containees]

    contains_dict[container] = containees

valid_containers = []

def lookup(contained_bag): 
    global valid_containers, contains_dict
    for container, containees in contains_dict.items():
        if any([containee == contained_bag for containee in containees]):
            if container not in valid_containers:
                valid_containers.append(container)
                # Check the container bag to see if other bags contain this container
                lookup(container)
                
lookup(('shiny', 'gold'))
print(len(valid_containers))