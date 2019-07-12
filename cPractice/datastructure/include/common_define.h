#ifndef COMMON_DEFINE_H_INCLUDED
#define COMMON_DEFINE_H_INCLUDED

typedef struct{
 char name[20];
 float score;
}STD;

typedef struct{
 STD *data;
 int listsize;
 int length;
}SqList;

#endif // COMMON_DEFINE_H_INCLUDED
