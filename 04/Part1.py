required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = []
data_required = []

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

print(len(data_required))