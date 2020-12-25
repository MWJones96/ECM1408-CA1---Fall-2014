def is_train_possible(capacity, stations):
    in_train = 0
    waiting = 0
    for station in stations:
        in_train -= station[0]
        if in_train < 0:
            return 'impossible'

        in_train += station[1]
        if in_train > capacity:
            return 'impossible'

        waiting = station[2]

        if waiting > 0 and in_train < capacity:
            return 'impossible'

    return 'possible' if in_train == 0 and waiting == 0 else 'impossible'

files = ['train1.txt', 'train2.txt', 'train3.txt', 'train4.txt']
for file in files:
    with open(file) as f:
        lines = [[int(s) for s in x.split(' ')] for x in f.readlines()]
        cap = lines[0][0]
        stations = lines[1:]

        print(is_train_possible(cap, stations))