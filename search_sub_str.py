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


def make_table(s):
    n = len(s)
    table = [0] * n
    for i in range(1, n):
        j = table[i - 1]
        while j >= 0 and s[i] != s[j]:
            j = table[j - 1] if j else -1
        table[i] = j + 1
    return table


def search_sub_kmp(s, sub):
    n = len(s)
    m = len(sub)
    if n == 0:
        return 0 if m == 0 else -1
    if m == 0:
        return 0

    table = make_table(sub)
    i = 0
    j = 0
    while i < n:
        if s[i] == sub[j]:
            i += 1
            j += 1
            if j == m:
                # find
                return i - j
        else:
            if j:
                j = table[j - 1]
            else:
                i += 1
    return -1

if __name__ == '__main__':
    s = 'ABC ABCDAB ABCDABCDABDE'
    sub = 'ABCDABD'
    print(s, sub, sep=', ')
    print(make_table(sub))
    i = search_sub_kmp(s, sub)
    print(i, s[i: i + len(sub)])
