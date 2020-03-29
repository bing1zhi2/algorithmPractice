/*
删除元素为x的 O(n) 空间O(1)
*/

#include <iostream>

#define EleType int

typedef struct
{
    EleType *data;
    int length;
} SeqList;

void deleteAllx(SeqList &seqlist, EleType x)
{
    int k = 0; // 不等于x的数量
    for (int i = 0; i < seqlist.length;i++)
    {
        if(seqlist.data[i] != x){
            seqlist.data[k] = seqlist.data[i];
            k++;
        }
    }
}
