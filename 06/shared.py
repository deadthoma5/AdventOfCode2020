# read a list of records from a file (blocks of multiple lines, each record seperated by blank line)
def read_records(filename):
    data = []
    group = []
    with open(filename) as f:
        for line in f:
            if len(line.strip()) > 0:
                person = []
                for index in range(len(line.rstrip('\n'))):
                    person.append(line[index])
                group.append(person)
            else:
                data.append((group))
                group = []
                continue
    return data