#ifndef LINKTABLE_H_INCLUDED
#define LINKTABLE_H_INCLUDED
#include "common_define.h"
typedef struct LNode{
 STD data;
 struct LNode *next;
}LNode,*LinkList;

int initLinkList(LinkList *L);
int insertLinkList(LinkList L,int i, STD x);
void deleteNode(LinkList L ,int i , STD *x);
void printfLinkList(LinkList L);

#endif // LINKTABLE_H_INCLUDED
