#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*  һԪ����ʽ�ļ���*/
typedef struct{
    float coef; //ϵ��
    int exp; //ָ��
}Term;

typedef struct
{
    Term data;
    struct node *next;
}PNode,*PLink;
