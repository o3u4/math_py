# Exam.py
# Directly Calculating exhaustive algorithm for verifying the structure of solutions

import itertools


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def mat(i):
    mi = []
    for x in range(3):
        for y in range(3):
            if dist((x, y), (i // 3, i % 3)) <= 1:
                mi.append(1)
            else:
                mi.append(0)
    return mi


def add(m1, m2):
    new_m = []
    for i in range(9):
        new_m.append((m1[i] + m2[i]) % 2)
    return new_m


bas = []
for item in range(9):
    bas.append(mat(item))

sequences = []
for le in range(9):
    for seq in itertools.combinations(range(9), le + 1):
        sequences.append(seq)


def answer(org, tgt):
    result = []
    st = []     # All possibilities
    for seqs in sequences:
        init = org
        for shun in seqs:
            init = add(bas[shun], init)
        if init not in st:
            st.append(init)
    print(len(st))
    print(st)
    for i in range(len(st)):
        if st[i] == tgt:
            result = [itm + 1 for itm in sequences[i]]
            # print(result)
            break
        else:
            continue
    return result


if __name__ == '__main__':
    origin = [0, 0, 1, 0, 0, 0, 0, 1, 1]
    target = [1, 1, 0, 0, 0, 1, 0, 0, 0]
    print(answer(origin, target))
    

