// title: linked-list-cycle-ii
// detail: https://leetcode.com/submissions/detail/193108513/
// datetime: Mon Dec  3 16:25:32 2018
// runtime: 4 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    if(head == NULL || head->next == NULL){
        return NULL;
    }
    struct ListNode *slow, *fast;
    int has_cycle = false;
    slow = fast = head;
    while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast){
            has_cycle = true;
            break;
        }
    }
    if(!has_cycle){
        return NULL;
    }
    slow = head;
    while(slow != fast){
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}