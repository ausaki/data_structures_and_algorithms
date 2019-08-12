def combination_rec(sequence, offset, count, index):
    if count == 0:
        print([sequence[i] for i in index])
        return 
    for i in range(offset, len(sequence) - count + 1):
        index[-count] = i
        combination_rec(sequence, i + 1, count - 1, index)

def combination(sequence, count):
    index = [0] * count
    combination_rec(sequence, 0, count, index)

def combination2(sequence, count):
    N = len(sequence)
    index = list(range(count))
    i = count - 1
    while True:
        while index[i] < N:
            yield [sequence[i] for i in index]
            index[i] += 1 
        while i >= 0 and ((count - i) >= (N - index[i])):
            i -= 1
        if i < 0:
            break
        index[i] += 1
        for i in range(i + 1, count):
            index[i] = index[i - 1] + 1
        
if __name__ == '__main__':
    # sequence = [1, 2, 3, 4, 5]
    # print(sequence)
    # combination(sequence, 3)

    sequence = [1, 2, 3, 4, 5]
    for s in combination2(sequence, 3):
        print(s)