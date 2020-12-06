with open('p4.txt', 'r') as f:
    input_s = f.read()
passports = input_s.split('\n\n')

def check_hex(num):
    try:
        int(num, 16)
        return True
    except ValueError:
        return False

required_fields = {
    "byr": lambda x: len(x) == 4 and x.isnumeric() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and x.isnumeric() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and x.isnumeric() and 2020 <= int(x) <= 2030,
    "hgt": lambda x: True if x[-2:] == 'cm' and x[:-2].isnumeric() and 150 <= int(x[:-2]) <= 193 else True if x[-2:] == 'in' and x[:-2].isnumeric() and 59 <= int(x[:-2]) <= 76 else False,
    "hcl": lambda x: x[0] == '#' and len(x) == 7 and check_hex(x[1:]),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}

valids = 0

for passport in passports:
    fields = passport.split()
    pp_dict = {k: v for field in fields for k, v in [field.split(':')]}

    valid = True
    for field, check_func in required_fields.items():
        if field not in pp_dict:
            valid = False
            break
        if not check_func(pp_dict[field]):
            valid = False
            break
    if valid: valids += 1

print(valids)