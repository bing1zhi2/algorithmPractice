#include<stdio.h>
#include<stdlib.h>
#include<common_define.h>


int initSqlList(SqList *L, int max){
    L->data =(STD*) malloc(sizeof(STD)*max );
    if(L->data == NULL){
        printf("init failed...\n");
        return 0;
    }
    L->listsize = max;
    L->length = 0;
    return 1;
}
