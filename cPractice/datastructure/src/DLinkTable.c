#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "DLinkTable.h"

/* 双向表*/
int initDlinkList(DLinkList *L)
{
    * L =(DLinkList)malloc(sizeof(DNode));
    if(*L ==NULL)
        return 0;
    (*L)->pre=(*L)->next=*L;
    return 1;
}

int insertDLinkList(DLinkList L, int i ,STD x)
{
    DLinkList p=L,s;
    int j;
    p=L;j=0;
    while(p->next!=L && j<i-1)
    {
        p = p->next;
        j++;
    }
    if(p->next==L&&j<i-1||j>i-1)
    {
        printf("插入位置不合理！\n");
    }
    s =(DLinkList)malloc(sizeof(DNode));
    s->data = x;

    s->pre = p;
    s->next = p->next;
    p->next->pre = s;
    p->next= s;

    return 1;
}


int deleteDLinkList(DLinkList L,int i,STD *x)
{
    DLinkList p,q;
    int j;
    p=L;j=0;
    while(p->next!=L && j<i-1)
    {
        p = p->next;
        j++;
    }
    if(p->next==L|| j>i-1)
    {
        printf("插入位置不合理\n");
        return 0;
    }
    q = p->next;
    *x = q->data;
    p->next = q->next;
    q->next->pre = p;
    free(q);
    return 1;
}

