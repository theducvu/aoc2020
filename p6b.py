import string

with open('p6.txt', 'r') as f:
    input_s = f.read()

groups = input_s.split('\n\n')

questions = string.ascii_lowercase  # a-z
l = 0
for group in groups:
    remaining_questions = questions    
    people = group.split('\n')
    for p in people:
        remaining_questions = ''.join([c for c in remaining_questions if c in p])
    l += len(remaining_questions)

print(l)