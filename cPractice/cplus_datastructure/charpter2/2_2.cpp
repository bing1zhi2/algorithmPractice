#include<iostream>

#define Maxsize 50
#define ElemType int

typedef struct
{
    /* 动态分配的一维数组 */
    ElemType *data;
    int length;
} SeqList;

using namespace std;

void reverseList(SeqList &seqList){
    int mid = seqList.length / 2;
    ElemType temp;
    for (int i = 0; i < mid; i++)
    {
        // reverse i length-1-i
        temp = seqList.data[i];
        seqList.data[i] = seqList.data[seqList.length - 1 - i];
        seqList.data[seqList.length - 1 - i] = temp;
    }
}
int main(int argc, char const *argv[])
{
    
    SeqList seqlist;
    seqlist.data = new ElemType[3];
    seqlist.data[0] = 1;
    seqlist.data[1] = 2;
    seqlist.data[2] = 3;
    seqlist.length = 3;

    for (int i = 0; i < seqlist.length; i++)
    {
        /* code */
        cout << seqlist.data[i] << endl;
    }

    reverseList(seqlist);

    for (int i = 0; i < seqlist.length; i++)
    {
        /* code */
        cout <<i <<": "<< seqlist.data[i] << endl;
    }
    

    return 0;
}
