// title: integer-to-roman
// detail: https://leetcode.com/submissions/detail/116013859/
// datetime: Tue Aug 29 09:26:18 2017
// runtime: 82 ms
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
    char* result = (char*)malloc(20);
    int i = 0, j = 0;
    int n = 1000;
    int m = 0;
    int k = 0;
    // printf("%d\n", (chars));
    // printf("%d\n", (chars + 1));
    // printf("%d\n", (chars + 2));
    // printf("%d\n", (chars + 3));
    // for(i = 0; i < N; i ++){
    //     printf("%d\n", ((char*)chars[i])[j]);
    // }
    while(num > 0 && n > 0){
        m = num / n * n;
        if(m < 0){
            n /= 10;
            continue ;
        }
        for(i = 0; i < N; i ++){
            if(m == roman[i]){
                // j = 0;
                memcpy(result + k, chars[i], strlen(chars[i]));
                // while(((char*)chars[i])[j] != 0){
                //     result[k++] = ((char*)chars[i])[j];
                //     j ++;
                // }
                k += strlen(chars[i]);
                break;
            }
        }
        num = num % n;
        n /= 10;
    }
    result[k] = 0;
    return result;
}