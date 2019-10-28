def compress_string(string):
    """
    压缩字符串

    给定一个字符串，要求将连续重复的字符压缩为'[COUNT][CHAR]'的形式，例如字符串'aaabcceee'压缩后为'3a1b2c3e'。
    """
    current = string[0]
    count = 1
    result = ''
    
    i = 1
    N = len(string) 
    while i < N:
        c = string[i]
        if c != current:
            result += str(count) + current
            current = c
            count = 0
        count += 1
        i += 1
    result += str(count) + current
    return result


if __name__ == '__main__':
    string = 'aaabcceee'
    print(compress_string(string))
