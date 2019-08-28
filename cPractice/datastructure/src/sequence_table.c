#include<stdio.h>
#include<stdlib.h>
#include<common_define.h>
#include<string.h>
// ˳���


int initSqlList(SqList *L, int max){
    L->data =(STD *) malloc(max* sizeof(STD) );
    if(L->data == NULL){
        printf("init failed...\n");
        return 0;
    }
    L->listsize = max;
    L->length = 0;
    return 1;
}

//������λ�� �����룬ע�������1��ʼ��ʵ�ʴ洢��0��
int insertSqlList(SqList *L,int i,STD std){

    if(i<1|| i> L->length+1){
        printf("pos error...");
    };
    if(L->length > L->listsize){
        printf("��������");
    };
    int j;
    for(j=L->length ; j>=i; j--){
        L->data[j] = L->data[j-1];
    }
    L->data[i-1]= std;
    L->length=L->length + 1;
    return 1;
}

//ɾ���� ǰ��
int deleteSqlList(SqList *L, int i, STD *std){

    *std = L->data[i-1];
    int k;
    for(k=i-1; k< L->length;k++){
        L->data[k-1] = L->data[k];
    }
    L->length = L->length -1;
    return 1;
}

int updateSqlList(SqList *L, int i, STD std){
    L->data[i-1] = std;
    return 1;
}

void printfSqlList(SqList L){
    int i;
    for(i=0;i<L.length;i++){
        printf(" %10s ",L.data[i].name);
        printf(" %7.2f ",L.data[i].score);
    }
    printf("--------------------- \n");
}


int my_sequence_main()
{
    // ��ʼ��˳���
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
    strcpy(std.name,"����");
    std2.score= 99;
    insertSqlList(&L,L.length+1,std2);

    std2.score= 98;


    printfSqlList(L);

    updateSqlList(&L,2,std2);
    printfSqlList(L);
    return 0;
}

