// title: add-two-numbers
// detail: https://leetcode.com/submissions/detail/75776976/
// datetime: Sun Sep 25 19:40:30 2016
// runtime: 15 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int addResult = 0, 
        carry = 0;
    
    struct ListNode *pa, *pb, *result, *pre_a, *tmp;
    pa = l1;
    pb = l2;
    result = l1;

    while(pa != NULL && pb != NULL){
        addResult = pa->val + pb->val + carry;
        if(addResult > 9){
            carry = addResult / 10;
            addResult = addResult % 10;
        } else {
            carry = 0;
        }
        pa->val = addResult;
        pre_a = pa;
        pa = pa->next;
        pb = pb->next;
    }
    if(pb != NULL){
        // pa must be NULL
        pa = pb;
        pre_a->next = pa;
    }
    if(pa != NULL){
        while(pa != NULL){
            // pb must be null
            addResult = pa->val + carry;
            if(addResult > 9){
                carry = addResult / 10;
                addResult = addResult % 10;
            } else {
                carry = 0;
            }
            pa->val = addResult;
            pre_a = pa;
            pa = pa->next;
        }
    }
    if(carry != 0){
        tmp = (struct ListNode *)malloc(sizeof(struct ListNode) * 1);
        tmp->val = carry;
        tmp->next = NULL;
        pre_a->next = tmp;
        carry = 0;
    }
    return result;
}