def two_sum(sequence, sum):
    sequence = sorted(sequence)
    i = 0
    j = len(sequence) - 1
    while i < j:
        tmp = sequence[i] + sequence[j] 
        if tmp == sum:
            yield sequence[i], sequence[j]
            i += 1
            j += 1
        elif tmp < sum:
            i += 1
        else:
            j -= 1


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 5]
    for n, m in two_sum(sequence, 5):
        print(n, m)
