// title: validate-binary-search-tree
// detail: https://leetcode.com/submissions/detail/60285783/
// datetime: Fri Apr 29 10:02:32 2016
// runtime: 8 ms
// memory: N/A

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int FLAG = 0, PREVAL;
bool ISVALIDBST = true;

bool visit(struct TreeNode* node) {
    if (FLAG > 0){
        if (node->val <= PREVAL) {
            return false;
        }
    }
    PREVAL = node->val;
    FLAG ++;
    return true;
}
 
void inOrderTravel(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }
    inOrderTravel(root->left);
    if (!visit(root)) {
        ISVALIDBST = false;
        return;
    }
    inOrderTravel(root->right);
}

bool isValidBST(struct TreeNode* root) {
    bool result;
    inOrderTravel(root);
    result = ISVALIDBST;
    FLAG = 0;
    ISVALIDBST= true;
    return result;
}