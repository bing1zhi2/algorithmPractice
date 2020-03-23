#ifndef COMMON_DEFINE_H_INCLUDED
#define COMMON_DEFINE_H_INCLUDED
#define MAXSIZE 1000

typedef int ElemType;

typedef struct{
 char name[20];
 float score;
}STD;

typedef struct{
 STD *data;
 int listsize;
 int length;
}SqList;


/* 静态链表相关 */
typedef struct{
    ElemType data;
    int next;
}SNode;

typedef struct{
    SNode sd[MAXSIZE];
    int SL,AV;  /* 两个头指针*/
    int SLinksize;

}StaticLink;

#endif // COMMON_DEFINE_H_INCLUDED
