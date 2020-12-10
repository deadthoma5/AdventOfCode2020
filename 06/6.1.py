from shared import read_records

testing = False

if testing:
    data = read_records("input_test")
else:
    data = read_records("input")

if testing:
    print(data)

sum_total = 0

for group in data:
    sum_group = 0
    unique_list_group = []
    for person in group:
        for response in person:
            if response not in unique_list_group:
                unique_list_group.append(response)
    sum_group += len(unique_list_group)
    sum_total += sum_group

print(sum_total)