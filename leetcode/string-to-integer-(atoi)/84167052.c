// title: string-to-integer-(atoi)
// detail: https://leetcode.com/submissions/detail/84167052/
// datetime: Tue Nov 29 14:45:12 2016
// runtime: 6 ms
// memory: N/A

int myAtoi(char* str) {
    int MAX_INT = 2147483647;
    int MIN_INT = -2147483648;
    int result = 0;
    int sign = 1;
    char ch;
    int i = 0;
    int j = 0;
    int strlength = strlen(str);
    if(strlength == 0){
        return 0;
    }
    for(; i < strlength && str[i] == ' '; i ++){
    }
    if(i == strlength){
        return 0;
    }
    // 判断开始的字符是否合法：0-9, - , +
    ch = str[i];
    if(ch == '-'){
        sign = -1;
        i ++;
    } else if(ch == '+'){
        sign = 1;
        i ++;
    } else if(ch < '0' || ch > '9'){
        return 0;
    }
    for(j = i; j < strlength && str[j] >= '0' && str[j] <= '9'; j ++){
        
    }
    for(; i < j - 1; i ++){
        ch = str[i] - '0';
        if(ch < 0 || ch > 9){
            // invalid
            printf("invalid break");
            break;
        }
        if(result > MAX_INT - ch){
            return MAX_INT;
        }
        if(result < MIN_INT + ch){
            return MIN_INT;
        }
        result += ch * sign;
        if(result > MAX_INT / 10){
            return MAX_INT;
        }
        if(result < MIN_INT / 10){
            return MIN_INT;
        }
        result *= 10;
    }
    printf("result = %d, sign = %d", result, sign);
    if(i < strlength){
        ch = str[i] - '0';
        if(ch >= 0 && ch <= 9){
            // if(sign > 0 && result > MAX_INT - ch){
            //     return MAX_INT;
            // } else if(sign < 0 && result > MAX_INT + 1 - ch){
            //     return MIN_INT;
            // }
            if(result > MAX_INT - ch){
                return MAX_INT;
            } else if(result < MIN_INT + ch){
                return MIN_INT;
            }
            result += ch * sign;
        } else {
            result /= 10;
        }
    }
    return result;
}