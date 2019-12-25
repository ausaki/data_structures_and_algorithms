// title: roman-to-integer
// detail: https://leetcode.com/submissions/detail/116042671/
// datetime: Tue Aug 29 12:25:22 2017
// runtime: 92 ms
// memory: N/A

int romanToInt(char* s) {
    int result = 0;
    int length = strlen(s);
    int i = 0;
    while(s[i] != 0){
        switch(s[i]){
            case 'I':
                if(i + 1 < length){
                    if(s[i + 1] == 'V'){
                        result += 4;
                        i ++;
                    } else if(s[i + 1] == 'X'){
                        result += 9;
                        i ++;
                    } else {
                        result += 1;
                    }
                } else{
                    result += 1;
                }
                break;
            case 'V':
                result += 5;
                break;
            case 'X':
                if(i + 1 < length){
                    if(s[i + 1] == 'L'){
                        result += 40;
                        i ++;
                    } else if(s[i + 1] == 'C'){
                        result += 90;
                        i ++;
                    } else {
                        result += 10;
                    }
                } else{
                    result += 10;
                }
                break;
            case 'L':
                 result += 50;
                break;
            case 'C':
                if(i + 1 < length){
                    if(s[i + 1] == 'D'){
                        result += 400;
                        i ++;
                    } else if(s[i + 1] == 'M'){
                        result += 900;
                        i ++;
                    } else {
                        result += 100;
                    }
                } else{
                    result += 100;
                }
                break;
            case 'D':
                 result += 500;
                break;
            case 'M':
                 result += 1000;
                break;
        }
        i ++;
    }
    return result;
}