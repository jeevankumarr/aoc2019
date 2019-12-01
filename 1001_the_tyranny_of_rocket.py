import requests

def run(input_data):
    rep = open(input_data)
    # print(rep)
    s = 0
    with open(f'{input_data[:-5]}{"_out"}{".data"}', 'w') as out_file:
        for i, val in enumerate(rep):
            out_val = calculate_fuel(int(val))
            print(f'{i+1:3}: {int(val):,}: {out_val:,}')
            out_file.write(f'{out_val}\n')
            s += out_val

    assert s == 5055835
    print(f'{s:,}', f'is correct {s == 5055835}')

def calculate_fuel(weight):
    fuel_wt = ((weight//3)-2)
    temp = fuel_wt

    while temp > 0:
        temp = (temp // 3 ) - 2
        fuel_wt += temp
    return fuel_wt - temp

if __name__ == '__main__':
    run('./data/1001_the_tyranny_of_rocket.data')