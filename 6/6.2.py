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
    responses_group = []
    unique_responses_group = []
    sum_group = 0
    for person in group:
        for response in person:
            responses_group.append(response)
            if response not in unique_responses_group:
                unique_responses_group.append(response)
    for response in unique_responses_group:
        if testing:
            print(response, responses_group.count(response), len(group))
        if responses_group.count(response) == len(group):
            sum_group += 1
    if testing:
        print()
    sum_total += sum_group

print(sum_total)