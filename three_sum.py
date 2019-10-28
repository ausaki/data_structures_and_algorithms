def three_sum(sequence, sum):
    sequence = sorted(sequence)
    N = len(sequence)
    i = 0
    j = len(sequence) - 1
    k = 0
    while i <= N - 3:
        k = i + 1
        j = N - 1
        sub_sum = sum - sequence[i]
        while k < j:
            tmp = sequence[k] + sequence[j] 
            if tmp == sub_sum:
                yield sequence[i], sequence[k], sequence[j]
                k += 1
                j -= 1
            elif tmp < sub_sum:
                k += 1
            else:
                j -= 1
        i += 1


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 5]
    for n, m, k in three_sum(sequence, 8):
        print(n, m, k)