def quick_select(data, k):
    if k <= 0 or k > len(data):
        return -1
    l, r = 0, len(data) - 1
    while True:
        mid = (l + r) // 2
        if data[l] > data[mid]:
            data[l], data[mid] = data[mid], data[l]
        if data[mid] > data[r]:
            data[mid], data[r] = data[r], data[mid]
        if data[l] > data[mid]:
            data[l], data[mid] = data[mid], data[l]
        if r - l + 1 <= 3:
            return data[k - 1]
        data[l + 1], data[mid] = data[mid], data[l + 1]
        pivot = data[l + 1]
        i, j = l + 2, r - 1
        while True:
            while data[i] < pivot:
                i += 1
            while data[j] > pivot:
                j -= 1
            if i > j:
                break
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        data[l + 1], data[j] = data[j], data[l + 1]
        if k - 1 == j:
            return data[j]
        if k - 1 < j:
            r = j - 1
        else:
            l = j + 1

if __name__ == '__main__':
    import random
    data = list(range(1, 20))
    random.shuffle(data)
    d = quick_select(data, 10)
    print(data)
    print(d)
