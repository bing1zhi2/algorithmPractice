#ifndef DLINKTABLE_H_INCLUDED
#define DLINKTABLE_H_INCLUDED
#include "common_define.h"

typedef struct DNode
{
    STD data;
    struct DNode *pre;
    struct DNode *next;
} DNode, *DLinkList;


int initDlinkList(DLinkList *L);
int insertDLinkList(DLinkList L, int i ,STD x);
int deleteDLinkList(DLinkList L,int i,STD *x);

#endif // DLINKTABLE_H_INCLUDED
