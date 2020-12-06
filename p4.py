with open('p4.txt', 'r') as f:
    input_s = f.read()
passports = input_s.split('\n\n')

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

valids = 0

for passport in passports:
    fields = passport.split()
    pp_dict = {k: v for field in fields for k, v in [field.split(':')]}
    keys = pp_dict.keys()
    if not any([f not in keys for f in required_fields]):
        valids += 1

print(valids)