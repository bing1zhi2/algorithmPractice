#include <iostream>

#define MaxSize 50
#define ElemType int
typedef struct
{
    /* 静态分配的一维数组 */
    ElemType data[MaxSize];
    int length;
} SqlList;

typedef struct
{
    /* 动态分配*/
    ElemType *data;
    int length;
} SeqList;

using namespace std;

bool deleteMin(SqlList &L, ElemType &minVal)
{
    if (L.length <= 0)
    {
        cout << "the val is null" << endl;
        return false;
    }
    int minIdx = 0; //记录最小值的索引
    minVal = L.data[0];
    for (int i = 1; i < L.length; i++)
    {
        if (L.data[i] < minVal)
        {
            minVal = L.data[i];
            minIdx = i;
        }
    }
    L.data[minIdx] = L.data[L.length - 1];
    L.length--;
    return true;
}

bool ListInsert(SqlList &L, int i, ElemType e){

}


int main(int argc, char const *argv[])
{
    SqlList L;
    L.data[0] = 2;
    L.data[1] = 5;
    L.data[2] = 4;
    L.length = 3;
    ElemType value;
    bool result = deleteMin(L,value);
    cout << value << endl;

    return 0;
}
