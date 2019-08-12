def permutation(sequence, left, right):
    """
    print all permutaions of  `sequence`
    """
    if left >= right:
        print(sequence)
        return
    for i in range(left, right + 1):
        sequence[left], sequence[i] = sequence[i], sequence[left]
        permutation(sequence, left + 1, right)
        sequence[left], sequence[i] = sequence[i], sequence[left]


def next_permutaion(sequence):
    """
    return next 'dictionary order' permutation  
    """
    N = len(sequence)
    if N < 2:
        return
    while True:
        i = N - 2
        while i >= 0 and sequence[i] >= sequence[i + 1]:
            i -= 1
        if i < 0:
            break
        j = N - 1
        while j > i and sequence[j] <= sequence[i]:
            j -= 1
        sequence[i], sequence[j] = sequence[j], sequence[i]
        sequence[i + 1: N] = sequence[N - 1: i: -1]
        yield sequence


if __name__ == '__main__':
    import random
    # sequence = [random.randint(1, 10) for i in range(4)]
    # permutation(sequence, 0, len(sequence) - 1)

    sequence = [random.randint(1, 10) for i in range(2)]
    print(sequence)
    for seq in next_permutaion(sequence):
        print(seq)
