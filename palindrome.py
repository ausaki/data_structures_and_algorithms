def find_longest_palindrome(sequence):
    N = len(sequence)
    longest = 1
    c = 0
    l = 0
    for i in range(N):
        j = 0
        # odd
        while (i - j >= 0) and (i + j < N) and sequence[i - j] == sequence[i + j]:
            j += 1
        l = 2 * j - 1
        if l > longest:
            longest = l
            c = i
        # even
        j = 0
        while (i - j >= 0) and (i + 1 + j < N) and sequence[i - j] == sequence[i + 1 + j]:
            j += 1
        l = 2 * j - 2
        if l > longest:
            longest = l
            c = i
    return sequence[c - (longest - 1) // 2: c + longest // 2 + 1]
            

def manacher(sequence):
    # add boundaries
    N = 2 * len(sequence) + 1
    old_sequence = sequence
    sequence = '|' + '|'.join(old_sequence) + '|'
    P = [0] * N
    C = 0
    R = 0
    for i in range(1, N):
        if i < R:
            P[i] = min([P[2 * C - i], R - i + 1])
        else:
            P[i] = 1
        while i - P[i] >= 0 and i + P[i] < N and sequence[i - P[i]] == sequence[i + P[i]]:
            P[i] += 1
        if i + P[i] - 1 > R:
            R = i + P[i] - 1
            C = i
    print(P)
    m = 0
    k = 0
    for i, l in enumerate(P):
        if l > m:
            m = l
            k = i
    return sequence[k - m + 2: k+m: 2]

if __name__ == '__main__':
    sequence = 'abcdefgfedc'
    print(sequence)
    # print(find_longest_palindrome(sequence))
    print(manacher(sequence))