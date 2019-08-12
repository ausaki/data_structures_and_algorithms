
def quick_select_r(data, k, left, right):
    """
    """
    center = (left + right) // 2
    if data[left] > data[center]:
        data[left], data[center] = data[center], data[left]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[center] > data[right]:
        data[center], data[right] = data[right], data[center]
    if right - left < 3:
        return center
    pivot = data[center]
    data[center], data[right - 1] = data[right - 1], data[center]
    
    i = left + 1
    j = right - 2
    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        else:
            break
    data[i], data[right - 1] = data[right - 1], data[i]
    if k < i + 1:
        quick_select_r(data, k, left, i - 1)
    elif k > i + 1:
        quick_select_r(data, k, i + 1, right)


def quick_select(data, k):
    quick_select_r(data, k, 0, len(data)  - 1)
    return data[k - 1]


if __name__ == '__main__':
    import random
    data = list(range(1, 20))
    random.shuffle(data)
    d = quick_select(data, 10)
    print(data)
    print(d)
