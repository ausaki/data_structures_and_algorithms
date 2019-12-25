// title: remove-nth-node-from-end-of-list
// detail: https://leetcode.com/submissions/detail/116559891/
// datetime: Fri Sep  1 16:35:53 2017
// runtime: 6 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int k = 0,length = 0;
    struct ListNode* p_current;
    
    p_current = head;
    while(p_current != NULL){
        length ++;
        p_current = p_current->next;
    }
    
    p_current = head;
    if(length - n == 0){
        // 移除头部
        head = head->next;
    } else {
        while(k < length - n - 1){
            p_current = p_current->next;
            k ++;
        }
        p_current->next = p_current->next->next;
    }
    return head;
}