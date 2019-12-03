import traceback
def compute(inputfile, a=12, b=2):
    data_raw = open(inputfile).read()
    data = data_raw.split(',')
    data = [int(x) for x in data]
    # print(data)
    mem = dict()


    for i, d in enumerate(data):
        mem[i] = d
    # print(f'14 {mem[14]}')
    mem[1] = a
    mem[2] = b
    i = 0
    while i < len(data):
        if mem[i] == 99:
            i += 1
            break
        if mem[i] == 1 or mem[i] == 2:
            l = mem[i + 1]
            r = mem[i + 2]
            dest = mem[i + 3]
            try:
                # print(f'Pr {i}/{mem[i]}: {l} {r} -> {dest} [ {mem[dest]} <- {mem[l]} {"+" if mem[i] == 1 else "*"} {mem[r]}]')
                if mem[i] == 1:

                    mem[dest] = mem[l] + mem[r]

                elif mem[i] == 2:
                    mem[dest] = mem[l] * mem[r]
                # print(f'Po {i}/{mem[i]}: {l} {r} -> {dest} [ {mem[dest]} <- {mem[l]} {"+" if mem[i] == 1 else "*"} {mem[r]}]')
                # print(f'Success {mem[dest]}[{dest}] <- {mem[l]}[{l}] {"+" if mem[i] == 1 else "*"} {mem[r]}[{r}]')
                # print(f'Success {i}: Op: {data[i]}, l = {data[i + 1]} meml = {mem[l]}, r = {data[i + 2]} memr = {mem[r]}=> {data[i + 3]}, mem={mem}')
                i += 4

            except Exception as e:
                print(f'Err {i}: {mem[i]}, {mem[i+1]}, {mem[i+2]} => {mem[i+3]}, mem = {mem}')
                traceback.print_exc()
                raise
        else:
            print(f'Err {i}')
    return mem[0]
def run():
    result = 19690720
    for i in range(0, 99):
        for j in range(0, 99):
            if result == compute('./data/1002_computer.data', i, j):
                print(i, j)
                break
if __name__ == '__main__':
    # compute('./data/1002_computer.data')
    run()