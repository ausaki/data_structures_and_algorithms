// title: rotate-list
// detail: https://leetcode.com/submissions/detail/145520516/
// datetime: Sat Mar 17 13:48:02 2018
// runtime: 8 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    struct ListNode* p = head;
    struct ListNode* prev = head;
    int n = 0;
    
    if(head == NULL){
        return head;
    }
    
    while(p->next != NULL){
        prev = p;
        p = p->next;
        n ++;
    }
    
    n ++;
    
    k = k % n;
    
    while(k > 0){
        p = head;
        prev = head;
        while(p->next != NULL){
            prev = p;
            p = p->next;
        }
        p->next = head;
        head = p;
        prev->next = NULL;
        
        k --;
    }
    return head;
    
}