// title: merge-two-sorted-lists
// detail: https://leetcode.com/submissions/detail/117200271/
// datetime: Tue Sep  5 22:35:47 2017
// runtime: 6 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* p1;
    struct ListNode* p2;
    struct ListNode* last = NULL;
    
    if(l1 == NULL){
        return l2;
    }
    if(l2 == NULL){
        return l1;
    }
    
    p1 = l1;
    p2 = l2;
    
    while(p1 != NULL && p2 != NULL){
        if(p1->val >= p2->val){
            if(last != NULL) last->next = p2;
            last = p2;
            p2 = p2->next;
        } else {
            if(last != NULL) last->next = p1;
            last = p1;
            p1 = p1->next;
        }
    }
    if(p1 != NULL){
        last->next = p1;
    }
    if(p2 != NULL){
        last->next = p2;
    }
    return l1->val >= l2->val ? l2 : l1;
}