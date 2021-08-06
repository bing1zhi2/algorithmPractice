#include<stdio.h>
#include<stdlib.h>

/*
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

//Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct Snode{
    struct TreeNode Data[101];
    int top;
} Stack;

void push(Stack *sptr, struct TreeNode item)
{
    if(sptr->top == 100-1)
    {
        printf("堆栈满");
        return;
    }else{
        sptr->Data[++(sptr->top)] = item;
        printf("push top: %d, val:%d ;",sptr->top, item.val);
    }
}
struct TreeNode pop(Stack *sptr)
{
    if(sptr->top == -1)
    {
        printf("堆栈空\n");
        struct TreeNode dummy;
        return dummy;
    }
    else{

        struct TreeNode node = sptr->Data[(sptr->top)--];
        printf("pop %d \n", node.val);
        return node;
    }
}
int isEmpty(Stack *sptr)
{
    if(sptr->top ==-1 )
    {
        printf("堆栈空\n");
        return 1;
    }else
    {
        printf("堆栈非空\n");
        return 0;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize){
    Stack *sptr = (Stack*) malloc(sizeof(Stack));
    sptr->top = -1;
    struct TreeNode* tptr = root;
    struct TreeNode* emptyPrt;

    int* return_arr = (int*) malloc(sizeof(int)*100);
    int idx = 0;


    while( tptr || !isEmpty(sptr))
    {
        while(tptr)
        {
            push(sptr, *tptr);  
            if (tptr->left)
            {
                tptr = tptr->left;
            }
            else
            {
                break;
            }
                
        }
        if(!isEmpty(sptr))
        {
            struct TreeNode node1 = pop(sptr);
            return_arr[idx++]= node1.val;
            tptr = &node1;
            if(tptr->right)
                tptr = tptr->right;
            else
                tptr = emptyPrt;
        }
    }
    *returnSize = idx;
    free(sptr);
    return return_arr;
}

int main()
{
    printf("Hello world!\n");
    // Node *p = (Node*)malloc(sizeof(Node));
    // p->left = NULL;
    // p->val = -1;
    // p->right = NULL;
    
    // if( !p->left)
    // {
    //     printf("p left is null");
    // }else{
    //     printf("p has left...%d", p->val);
    //     printf("p has left..%p", p->left);
    // }
    // struct TreeNode *root;
    struct TreeNode *p = (struct TreeNode*) malloc(sizeof(struct TreeNode));
    p->left = NULL;
    p->right = NULL;
    if(!p->left)
    {
      printf("p left is null");
    }

    Stack *a = (Stack*) malloc(sizeof(Stack));
    a->top = -1;
    isEmpty(a);
    push(a, *p);
    isEmpty(a);


    // printf();

    return 0;
}