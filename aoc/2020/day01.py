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


def solution1(data):
    target = 2020
    s = set()
    for a in data:
        if (target - a) in s:
            return a * (target - a)
        s.add(a)

def solution2(data):
    a, b, c = next(three_sum(data, 2020))
    return a * b * c

def main():
    arr = []
    while True:
        line = input()
        if not line:
            break
        arr.append(int(line))
    print(solution1(arr))
    print(solution2(arr))

main()