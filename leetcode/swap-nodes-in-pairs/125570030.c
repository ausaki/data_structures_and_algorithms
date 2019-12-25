// title: swap-nodes-in-pairs
// detail: https://leetcode.com/submissions/detail/125570030/
// datetime: Fri Oct 27 18:15:58 2017
// runtime: 3 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* p0;
    struct ListNode* p1;
    struct ListNode* p2;
    int tmp_val = 0;
    
    p0 = head;
    if(p0 == NULL){
        return head;
    }
    
    p1 = p0->next;
    while(p1 != NULL && p0 != NULL){
        tmp_val = p0->val;
        p0->val = p1->val;
        p1->val = tmp_val;
        
        p0 = p1->next;
        if(p0 == NULL){
            break;
        }
        p1 = p0->next;
    }
    return head;
}