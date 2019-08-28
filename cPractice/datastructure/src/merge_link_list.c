#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "common_define.h"
#include "LinkTable.h"



LinkList  mergeTwoLinkList(LinkList La,LinkList Lb)
{
    LinkList pa, pb, pc,s ;
    LinkList *Lc;
    pa = La->next;
    pb = Lb->next;

    initLinkList(Lc);
    pc = (* Lc);
    while( pa && pb)
    {
        if(pa->data.score <= pb->data.score)
        {
            s = (LinkList) malloc(sizeof(LNode));
            s->data = pa->data;
            s->next=NULL;
            pc->next = s;
            pc = s;

            pa = pa->next;
        }
        else
        {
            s = (LinkList)malloc(sizeof(LNode));
            s->data = pb->data;
            pc->next = s;
            pc =s;

            pb = pb->next;
        }
    }
    while(pa)
    {
        s = (LinkList) malloc(sizeof(LNode));
        s->data = pa->data;
        s->next=NULL;
        pc->next = s;
        pc = s;

        pa = pa->next;

    }
    while(pb)
    {

        s = (LinkList)malloc(sizeof(LNode));
        s->data = pb->data;
        pc->next = s;
        pc =s;

        pb = pb->next;

    }
    return (*Lc);
}



void testMerge()
{
    LinkList L;
    int re = initLinkList(&L);
    if(re)
        printf("success \n");

    STD x;
    strcpy(x.name,"cash");
    x.score=23;
    printf(" %7.2f \n",x.score);

    STD x2;
    strcpy(x2.name,"22cash2");
    x2.score=100;

    //insertLinkList(L,0,x);


    insertLinkList(L,1,x);
    insertLinkList(L,2,x2);
    printfLinkList(L);



    LinkList L2;
    int re2 = initLinkList(&L2);
    if(re2)
        printf("success \n");

    STD x3;
    strcpy(x3.name,"cash3");
    x3.score=11;
    printf(" %7.2f \n",x.score);

    STD x4;
    strcpy(x4.name,"cash4");
    x4.score=99;

    //insertLinkList(L,0,x);


    insertLinkList(L2,1,x3);
    insertLinkList(L2,2,x4);
    printfLinkList(L2);

    printf("test merge:\n");
    LinkList lc = mergeTwoLinkList(L,L2);
    printfLinkList(lc);
}
