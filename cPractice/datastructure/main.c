#include <stdio.h>
#include <stdlib.h>

#include "removeDup.h"
#include "common_define.h"





int main()
{

//	 ===== 删除排序数组中多出来的元素======================
//    testRemoveDup();


    // 初始化顺序表
    SqList L;
    if(initSqlList(&L,10))
        printf("success \n");
    printf(" %d ", L.length+1);
    STD std;
    strcpy(std.name,"test");
    std.score= 90;


    int re = insertSqlList(&L,L.length+1,std);
    if(re){
       printf("insert success \n");
    }

    STD std2;
    strcpy(std.name,"张三");
    std2.score= 99;
    insertSqlList(&L,L.length+1,std2);

    std2.score= 98;


    printfSqlList(L);

    updateSqlList(&L,2,std2);
    printfSqlList(L);


    return 0;
}
