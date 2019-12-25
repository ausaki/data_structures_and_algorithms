// title: generate-parentheses
// detail: https://leetcode.com/submissions/detail/124609476/
// datetime: Sat Oct 21 18:19:54 2017
// runtime: 3 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** generateParenthesis(int n, int* returnSize) {
    int i = 0, j = 0, s = 0, k = 0;
    int size = 5;           // 字符串数组的长度
    int length = n * 2;     // 括号字符串的长度
    char** result = (char**)malloc(sizeof(char*) * size);   // 结果
    char** result1 = NULL;  // 结果1
    char** result2 = NULL;  // 结果2
    int returnSize1 = 0;   // 结果1长度
    int returnSize2 = 0;   // 结果2长度
    char* parentheses = NULL;   // 括号字符串
    char* parentheses_ = NULL;   // 括号字符串
    
    if(n == 0){
        *returnSize = 0;
        return result;
    }
    if(n == 1){
        *returnSize = 1;
        parentheses = (char*)malloc(sizeof(char) * length + 1);
        parentheses = "()";
        result[0] = parentheses;
        return result;
    }
    
    parentheses = (char*)malloc(sizeof(char) * length + 1);
    parentheses[0] = '(';
    
    for(i = n - 1; i >= 0 ; i --){
        if(i == 0){
            parentheses[1] = ')';
            result2 = generateParenthesis(n - 1 - i, &returnSize2);
            for(k = 0; k < returnSize2; k ++){
                strcpy(parentheses + i * 2 + 2, result2[k]);
                parentheses[length] = 0;
                parentheses_ = (char*)malloc(sizeof(char) * length + 1);
                strcpy(parentheses_, parentheses);
                result[s++] = parentheses_;
                if(s >= size){
                    size += 5;
                    result = (char**)realloc(result, sizeof(char*) * size);
                }
            }
        } else {
            result1 = generateParenthesis(i, &returnSize1);
            for(j = 0; j < returnSize1; j ++){
                strcpy(parentheses + 1, result1[j]);
                parentheses[i * 2 + 1] = ')';
                if(i == n - 1){
                    parentheses[length] = 0;
                    parentheses_ = (char*)malloc(sizeof(char) * length + 1);
                    strcpy(parentheses_, parentheses);
                    result[s++] = parentheses_;
                    if(s >= size){
                        size += 5;
                        result = (char**)realloc(result, sizeof(char*) * size);
                    }
                } else {
                    result2 = generateParenthesis(n - 1 - i, &returnSize2);
                    for(k = 0; k < returnSize2; k ++){
                        strcpy(parentheses + i * 2 + 2, result2[k]);
                        parentheses[length] = 0;
                        parentheses_ = (char*)malloc(sizeof(char) * length + 1);
                        strcpy(parentheses_, parentheses);
                        result[s++] = parentheses_;
                        if(s >= size){
                            size += 5;
                            result = (char**)realloc(result, sizeof(char*) * size);
                        }
                    }
                }
            }
        }
    }
    *returnSize = s;
    return result;
}