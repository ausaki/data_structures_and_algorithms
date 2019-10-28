def search_sub_str_brute_force(s, sub):
    N = len(s)
    n = len(sub)
    i = 0
    j = 0

    while i <= N - n and j < n:
        while j < n and s[i + j] == sub[j]:
            j += 1
        if j == n:
            return i
        else:
            i += 1
            j = 0
    return -1


def partial_table(sub):
    m = len(sub)
    table = [0] * (m + 1)
    table[0] = -1
    i = 0
    while i < m:
        j = table[i]
        while j >= 0 and sub[i] != sub[j]:
            j = table[j]
        i += 1
        table[i] = j + 1
    return table


def search_sub_kmp(s, sub):
    n = len(s)
    m = len(sub)
    if n == 0:
        if m == 0:
            return 0
        else:
            return -1
    elif m == 0:
        return 0

    table = partial_table(sub)
    i = 0
    j = 0
    while i < n:
        if s[i] == sub[j]:
            i += 1
            j += 1
            if j == m:
                # find
                break
        else:
            j = table[j]
            if j < 0:
                j = 0
                i += 1
    if j == m:
        return i - j
    return -1

if __name__ == '__main__':
    s = 'ABC ABCDAB ABCDABCDABDE'
    sub = 'ABCDABD'
    print(s, sub, sep=', ')
    print(partial_table(sub))
    print(search_sub_kmp(s, sub))
