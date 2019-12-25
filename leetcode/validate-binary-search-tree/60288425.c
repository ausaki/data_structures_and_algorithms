// title: validate-binary-search-tree
// detail: https://leetcode.com/submissions/detail/60288425/
// datetime: Fri Apr 29 10:36:57 2016
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
// int FLAG = 0, PREVAL;
// bool ISVALIDBST = true;

bool visit(struct TreeNode* node, int* FLAG, int* PREVAL, bool* ISVALIDBST) {
    if (*FLAG > 0){
        if (node->val <= *PREVAL) {
            return false;
        }
    }
    *PREVAL = node->val;
    (*FLAG) ++;
    return true;
}
 
bool inOrderTravel(struct TreeNode* root, int* FLAG, int* PREVAL, bool* ISVALIDBST) {
    if (root == NULL) {
        return true;
    }
    if (!inOrderTravel(root->left, FLAG, PREVAL, ISVALIDBST)) {
        return false;
    }
    if (!visit(root, FLAG, PREVAL, ISVALIDBST)) {
        *ISVALIDBST = false;
        return false;
    }
    if (!inOrderTravel(root->right, FLAG, PREVAL, ISVALIDBST)) {
        return false;
    }
    return true;
}
// void inOrderTravel(struct TreeNode* root, int* FLAG, int* PREVAL, bool* ISVALIDBST) {
//     if (root == NULL) {
//         return;
//     }
//     inOrderTravel(root->left, FLAG, PREVAL, ISVALIDBST);
//     if (!visit(root, FLAG, PREVAL, ISVALIDBST)) {
//         *ISVALIDBST = false;
//         return false;
//     }
//     inOrderTravel(root->right, FLAG, PREVAL, ISVALIDBST);
// }
bool isValidBST(struct TreeNode* root) {
    int FLAG = 0, PREVAL;
    bool ISVALIDBST = true;
    inOrderTravel(root, &FLAG, &PREVAL, &ISVALIDBST);
    // result = ISVALIDBST;
    // FLAG = 0;
    // ISVALIDBST= true;
    // return result;
    printf("FLAG: %d", FLAG);
    return ISVALIDBST;
}