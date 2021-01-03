def three_sum(sequence, sum):
    sequence = sorted(sequence)
    n = len(sequence)
    for i in range(n - 2):
        l, r = i + 1, n - 1
        sub_sum = sum - sequence[i]
        if sub_sum < sequence[l] + sequence[l + 1] or sub_sum > sequence[r] + sequence[r - 1]:
            continue
        while l < r:
            s = sequence[l] + sequence[r] 
            if s == sub_sum:
                yield sequence[i], sequence[l], sequence[r]
                l += 1
                r -= 1
            elif s < sub_sum:
                l += 1
            else:
                r -= 1


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 5]
    for n, m, k in three_sum(sequence, 8):
        print(n, m, k)