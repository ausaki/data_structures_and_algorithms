def jump_rec(n, result):
    if n < 0:
        return
    if n == 0:
        print(result)
        return
    result.append(1)
    jump_rec(n - 1, result)
    result.pop()
    result.append(2)
    jump_rec(n - 2, result)
    result.pop()
    
def jump_stairs(n):
    result = []
    jump_rec(n, result)


if __name__ == '__main__':
    jump_stairs(10)