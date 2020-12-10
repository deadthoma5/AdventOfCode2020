import re

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = []
data_required = []
data_validated = []

def validate_byr(byr):
    byr = int(byr)
    return byr >= 1920 and byr <= 2002

def validate_iyr(iyr):
    iyr = int(iyr)
    return iyr >= 2010 and iyr <= 2020


def validate_eyr(eyr):
    eyr = int(eyr)
    return eyr >= 2020 and eyr <= 2030

def validate_hgt(hgt):
    try:
        hgtfilter = re.compile("([0-9]+)([a-zA-Z]+)") 
        height, unit = hgtfilter.match(hgt).groups()
        height = int(height)
    except AttributeError:
        return False
    if unit == 'cm':
        return height >=150 and height <= 193
    elif unit == 'in':
        return height >=59 and height <= 76
    else:
        return False

def validate_hcl(hcl):
    try:
        hclfilter = re.compile("(#)([0-9a-fA-F]{6})") 
        symbol, value = hclfilter.match(hcl).groups()
    except AttributeError:
        return False
    return True

def validate_ecl(hcl):
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return hcl in valid_ecl

def validate_pid(pid):
    try:
        pidfilter = re.compile("([0-9]{9})") 
        if pidfilter.fullmatch(pid):
            return True
        else:
            return False
    except AttributeError:
        return False
    
with open("input") as f:
    record = {}
    for line in f:
        if len(line.strip()) > 0:
            for item in line.rstrip('\n').split(" "):
                record[item.split(":")[0]] = item.split(":")[1]
        else:
            data.append((record))
            record = {}
            continue

# check required fields
for record in data:
    if all(key in record for key in required_keys):
        data_required.append(record)

# validate fields
for record in data_required:
    status = True
    status *= validate_byr(record['byr'])
    status *= validate_iyr(record['iyr'])
    status *= validate_eyr(record['eyr'])
    status *= validate_hgt(record['hgt'])
    status *= validate_hcl(record['hcl'])
    status *= validate_ecl(record['ecl'])
    status *= validate_pid(record['pid'])

    if status:      
        data_validated.append(record)
        #print(record['byr'], record['iyr'], record['eyr'], record['hgt'], record['hcl'], record['ecl'], record['pid'])

print(len(data_validated))