// title: divide-two-integers
// detail: https://leetcode.com/submissions/detail/125994796/
// datetime: Mon Oct 30 18:20:45 2017
// runtime: 19 ms
// memory: N/A

int divide(int dividend, int divisor) {
    int MAX_INT = 1;
    int MIN_INT = 1;
    int int_size = 0;
    int i;
    int neg = 0;
    int shift = 0;
    int shift_val = 0;
    int rest = 0;
    int result = 0;
    
    for(i = 0; i < sizeof(int); i ++){
        int_size += 8;
    }
    MIN_INT = 1 << (int_size - 1);
    MAX_INT = MIN_INT - 1;
    
    printf("MIN_INT = %d\n", MIN_INT);
    printf("MAX_INT = %d\n", MAX_INT);
    printf("%d\n", 2147483647 - (2 << 30));
    if(divisor == 0){
        // 除数为零
        return MAX_INT;
    }
    if(dividend == 0){
        // 零除以任何数都等于0
        return 0;
    }
    
    if(dividend == MIN_INT && divisor == -1){
        return MAX_INT;
    }
    if(divisor == MIN_INT){
        if(dividend == MIN_INT){
            return 1;
        } else {
            return 0;
        }
    }
    if(dividend > 0 && divisor < 0){
        neg = 1;
    }
    if(dividend < 0 && divisor > 0){
        neg = 1;
    }
    if(dividend < 0){
        if(dividend == MIN_INT){
            dividend = MAX_INT;
            rest = 1;
        } else {
            dividend = -dividend;
        }
    }
    if(divisor < 0){
        divisor = -divisor;
    }
    while(dividend >= divisor){
        shift = 0;
        shift_val = divisor << shift;
        while(dividend >= shift_val && shift_val > 0){
            shift ++;
            shift_val = divisor << shift;
        }
        printf("shift = %d\n", shift);
        printf("dividend = %d\n", dividend);
        dividend -= (divisor << (shift - 1));
        printf("dividend = %d\n", dividend);
        result += 1 << (shift - 1);
    }
    printf("rest = %d\n", rest);
    printf("dividend = %d\n", dividend);
        
    if(rest){
        dividend += rest;
        if(dividend >= divisor){
            shift = 0;
            while(dividend >= (divisor << shift)){
                shift ++;
            }
            dividend -= (divisor << (shift - 1));
            result += 1 << (shift - 1);
        }
    }
    return neg ? -result : result;
}