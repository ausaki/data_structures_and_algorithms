// title: integer-to-roman
// detail: https://leetcode.com/submissions/detail/116017656/
// datetime: Tue Aug 29 09:51:31 2017
// runtime: 75 ms
// memory: N/A

char* intToRoman(int num) {
    int roman[] = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900,1000,2000, 3000
    };
    char** chars[] = {
        "I",
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX",
        "X", //10
        "XX",
        "XXX",
        "XL",
        "L", //50
        "LX",
        "LXX",
        "LXXX",
        "XC",
        "C", // 100
        "CC",
        "CCC",
        "CD",
        "D", // 500
        "DC",
        "DCC",
        "DCCC",
        "CM",
        "M",
        "MM",
        "MMM",
    };
    int N = 30;
    char* result = (char*)malloc(20);   // 
    int l = 0, r = 0, m;    // 查找
    int t = 1000;   // 倍数
    int n = 0;  // 
    int k = 0;  // 索引
    char chars_len = 0;
    
    while(t > 0){
        n = num / t * t;
        if(n <= 0){
            t /= 10;
            continue ;
        }
        l = 0;
        r = N - 1;
        while(l < r){
            m = l + (r - l) / 2;
            if(n > roman[m]){
                l = m + 1;
            } else if(n == roman[m]){
                l = r = m;
                break;
            } else {
                r = m - 1;
            }
        }
        if(roman[l] == n){
            chars_len = strlen(chars[l]);
            memcpy(result + k, chars[l], chars_len);
            k += chars_len;
        }
        num = num % t;
        t /= 10;
    }
    result[k] = 0;
    return result;
}