// title: linked-list-cycle
// detail: https://leetcode.com/submissions/detail/193094955/
// datetime: Mon Dec  3 15:02:17 2018
// runtime: 4 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL){
        return false;
    }
    struct ListNode *slow, *fast;
    slow = fast = head;
    while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            return true;
        }
    }
    return false;
}