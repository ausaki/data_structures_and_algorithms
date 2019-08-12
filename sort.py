import random

def insertion_sort(data):
    N = len(data)
    for i in range(1, N):
        tmp = data[i]
        j = i
        while j > 0 and data[j - 1] > tmp:
            data[j] = data[j - 1]
            j -= 1
        data[j] = tmp

def shell_sort(data):
    pass


def build_heap(data):
    N = len(data)
    i = 1
    while i < N:
        tmp = data[i]
        k = i
        parent = (k - 1)  // 2
        while parent >= 0 and tmp > data[parent]:
            data[k] = data[parent]
            k =  parent
            parent = (k - 1) // 2
        data[k] = tmp
        i += 1


def build_heap2(data):
    N = len(data)
    i = N // 2
    while i >= 0:
        percolate_down(data, i, N - 1)
        i -= 1

def percolate_down(data, i, N):
    tmp = data[i]
    child = 2 * i + 1
    while child <= N:
        if child < N and data[child + 1] > data[child]:
            child += 1
        if data[child] > tmp:
            data[i] = data[child]
        else:
            break
        i = child
        child = 2 * i + 1
    data[i] = tmp


def heap_sort(data):
    build_heap2(data)
    N = len(data)
    i = 0
    while i < N:
        data[0], data[N - 1 - i] = data[N - 1 - i], data[0]
        percolate_down(data, 0, N - 2 - i)
        i += 1


def merge_sort_r(data, left, right, buffer):
    if left >= right:
        return
    center = (left + right) // 2
    merge_sort_r(data, left, center, buffer)
    merge_sort_r(data, center + 1, right, buffer)
    i = left
    j = center + 1
    k = left

    while i <= center and j <= right:
        if data[i] < data[j]:
            buffer[k] = data[i]
            k += 1
            i += 1
        else:
            buffer[k] = data[j]
            k += 1
            j += 1
    while i <= center:
        buffer[k] = data[i]
        k += 1
        i += 1
    while j <= right:
        buffer[k] = data[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        data[i] = buffer[i]
    
def merge_sort(data):
    N = len(data)
    buffer = [None] * N
    merge_sort_r(data, 0, N - 1, buffer)

def partitioning1(data, left, right):
    """
    分区思路：根据三数中值法计算基准值。
    经过下面的比较和交换，必定data[left] <= data[center] <= data[right]，如果长度小于等于3，那么无需再进行分区了。
    接着将pivot和data[right]进行交换，并设置i=left，j=right - 1。
    如果i遇到小于pivot的元素就继续往右移动，如果j遇到大于pivot的元素，就继续往左移动。
    由于pivot放在索引right处，可以保证i向右移动过程中最远只能等于right。
    由于data[left]小于pivot，可以保证j向左移动过程中最远只能等于left。
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
    data[center], data[right] = data[right], data[center]
    i = left
    j = right - 1
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
    data[i], data[right] = data[right], data[i]
    return i

def partitioning2(data, left, right):
    """
    partitioning2是对partitioning1的优化
    因为data[left] <= pivot和data[right] >= pivot, 可以将pivot和data[right - 1]进行交换，并设置i=left + 1，j=right - 2。
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
    return i


def  partitioning3(data, left, right):
    """
    分区思路：i用于标识小于pivot的边界，即i左边的元素都小于pivot，右边的元素都大于等于pivot。

    这个方法没有partitioning1好，容易导致分区不平衡。
    """
    pivot = data[left]
    i = left
    j = left + 1
    while j <= right:
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        j += 1
    data[left], data[i] = data[i], data[left]
    return i

def quick_sort_r(data, left, right):
    if left >= right:
        return
    i = partitioning3(data, left, right)
    quick_sort_r(data, left, i - 1)
    quick_sort_r(data, i + 1, right)
    
def quick_sort(data):
    quick_sort_r(data, 0, len(data) - 1)


def test(name):
    g = globals()
    s = g.get(name)
    if s is not None:
        print('test ' + name)
        data = [random.randint(1, 100) for i in range(20)]
        print('Before:', data)
        s(data)
        print('After:', data)
        

if __name__ == '__main__':
    # test('insertion_sort')
    # test('heap_sort')
    # test('merge_sort')
    # test('quick_sort')
    d1 = [87, 98, 42, 81, 10, 71, 59, 37, 31, 29, 100, 14, 34, 53, 66, 21, 88, 83, 79, 62]
    d2 = [1, 1, 1, 1, 1]
    quick_sort(d1)
    print(d1)
    quick_sort(d2)
    print(d2)