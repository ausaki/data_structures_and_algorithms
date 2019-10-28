def n_sum_rec(n, m, result):
    if m < 0:
        return
    if m == 0:
        print(result)
        return
    if n < 1:
        return
    if n <= m:
        result.append(n)
        n_sum_rec(n - 1, m - n, result)
        result.pop()
        n_sum_rec(n - 1, m, result)
    else:
        n_sum_rec(m, m, result)

def n_sum(n, m):
    result = []
    n_sum_rec(n, m , result)

if __name__ == '__main__':
    n = 10
    m =  20
    n_sum(n, m)