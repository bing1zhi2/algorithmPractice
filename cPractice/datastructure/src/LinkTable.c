#include "LinkTable.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
// 单向链表



int initLinkList(LinkList *L)
{
    // L 指向头指针的指针变量 ，（*L）是头指针
    //下面是将头结点地址给头指针
    *L = (LinkList)malloc(sizeof(LNode));
    if(*L ==NULL)
        return 0;
    (*L)->next = NULL; //()是必须的
    return 1;
}

// 此处i从1开始
int insertLinkList(LinkList L,int i, STD x)
{
    LinkList p=L,s;

    int pos=0;
    while(p!=NULL && pos<i-1){
         p = p->next;
         pos = pos +1;
    }
    if(p==NULL ||pos>i-1)
    {
        printf("insert position wrong~ \n");
        return 0;
    }

    s = (LinkList)malloc(sizeof(LNode));
    s->data = x;

    s->next = p->next;
    p->next =s;

    return 1;
}

void deleteNode(LinkList L ,int i , STD *x)
{
    int j=0;
    LinkList p=L;
    LinkList q;

    while(j<i-1 && p->next !=NULL)
    {
        p = p->next;
        j = j+1;
    }
    q= p->next;
    p->next = q->next;
    *x = q->data;
    free(q);

}
void printfLinkList(LinkList L)
{
    LinkList p=L;
    while(p->next !=NULL)
    {
        p=p->next;
        printf(" %11s ",p->data.name);
        printf(" %7.2f ",p->data.score);
        printf("\n");
    }
}

int link_table()
{
    LinkList L;
    int re = initLinkList(&L);
    if(re)
        printf("success \n");

    STD x;
    strcpy(x.name,"cash");
    x.score=100;
    printf(" %7.2f \n",x.score);

    STD x2;
    strcpy(x2.name,"22cash2");
    x2.score=23;

    //insertLinkList(L,0,x);


    insertLinkList(L,1,x);
    insertLinkList(L,2,x2);
//    insertLinkList(L,2,x);
    insertLinkList(L,3,x2);
    printfLinkList(L);

    STD *x3;
    deleteNode(L,2,x3);
    printfLinkList(L);
    printf(x3->name);

    return 1;
}



