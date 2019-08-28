#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*  一元多项式的计算*/
typedef struct{
    float coef; //系数
    int exp; //指数
}Term;

typedef struct
{
    Term data;
    struct node *next;
}PNode,*PLink;
