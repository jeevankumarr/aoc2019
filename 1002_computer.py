import traceback
def compute(inputfile, a=12, b=2):
    data_raw = open(inputfile).read()
    data = data_raw.split(',')
    data = [int(x) for x in data]

    data[1] = a
    data[2] = b

    i = 0
    while i < len(data):
        if data[i] == 99:
            break
        l = data[i + 1]
        r = data[i + 2]
        dest = data[i + 3]
        # print(f'Pr {i}/{mem[i]}: {l} {r} -> {dest} [ {mem[dest]} <- {mem[l]} {"+" if mem[i] == 1 else "*"} {mem[r]}]')
        if data[i] == 1:
            data[dest] = data[l] + data[r]
        elif data[i] == 2:
            data[dest] = data[l] * data[r]

        # print(f'Po {i}/{mem[i]}: {l} {r} -> {dest} [ {mem[dest]} <- {mem[l]} {"+" if mem[i] == 1 else "*"} {mem[r]}]')
        i += 4

    return data[0]

def run(result=19690720):

    for i in range(0, 99):
        for j in range(0, 99):
            if result == compute('./data/1002_computer.data', i, j):
                print(i, j)
                break

if __name__ == '__main__':
    # print(compute('./data/1002_computer.data'))
    run(19690720)