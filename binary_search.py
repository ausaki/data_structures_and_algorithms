def binary_search(data, num):
    left = 0
    right = len(data) - 1
    middle = 0

    while left <= right:
        middle = (left + right) // 2
        if data[middle] == num:
            break
        elif data[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    if left > right:
        return -1
    return middle


if __name__ == '__main__':
    data = [1, 5, 6, 6, 7, 10, 13, 20]
    print(binary_search(data, 1))
