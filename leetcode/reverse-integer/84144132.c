// title: reverse-integer
// detail: https://leetcode.com/submissions/detail/84144132/
// datetime: Tue Nov 29 11:18:13 2016
// runtime: 6 ms
// memory: N/A

int reverse(int x) {
    int base = 10;
    int remainder = 0;
    int tmpx = 0;
    int result = 0;
    int sign = 1;
    if(x < 0){
        sign = -1;
        x = -x;
    }
    while((tmpx = x / base) != 0){
        remainder = x % base;
        printf("remainder = %d\n", remainder);
        result += remainder;
        if(result > 2147483647 / 10){
            return 0;
        }
        result *= base;
        printf("result = %d\n", result);
        x = tmpx;
    }
    if(result > 2147483647 - x){
        return 0;
    }
    result += x;
    return result * sign;
}