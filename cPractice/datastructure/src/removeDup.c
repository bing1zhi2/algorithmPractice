#include "removeDup.h"

/**
����һ���������飬����Ҫ��ԭ��ɾ���ظ����ֵ�Ԫ�أ�ʹ��ÿ��Ԫ��ֻ����һ�Σ������Ƴ���������³��ȡ�

��Ҫʹ�ö��������ռ䣬�������ԭ���޸��������鲢��ʹ�� O(1) ����ռ����������ɡ�

ʾ�� 1:

�������� nums = [1,1,2],

����Ӧ�÷����µĳ��� 2, ����ԭ���� nums ��ǰ����Ԫ�ر��޸�Ϊ 1, 2��

�㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�

ʾ�� 2:

���� nums = [0,0,1,1,1,2,2,3,3,4],

����Ӧ�÷����µĳ��� 5, ����ԭ���� nums ��ǰ���Ԫ�ر��޸�Ϊ 0, 1, 2, 3, 4��

�㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�

*/

int removeDuplicates(int* nums, int numsSize) {
	if (numsSize == 0) {
		return 0;
	}
	int temp = 0;
	for(int i = 1; i< 10; i++)
    {
		if (nums[temp] != nums[i]) {
			temp += 1;
			nums[temp] = nums[i];
		}
	}
	return temp + 1;
}

void testRemoveDup(){
    int nums[10] = { 0,0,1,1,1,2,2,3,3,4 };
    int numsSize = 10;
	int *p = nums;
//    for ( int i = 0; i < 10; i++ )
//    {
//       printf("*(p + %d) : %d\n",  i, *(p + i) );
//       printf("*(p + %d) : %d\n",  i, *(p + i) );
//    }

    removeDuplicates(p, 10);
    // ��ӡ����
    for (int i = 0; i < 10; i++) {
		printf("%d", nums[i]);
	}

	// ===============================================
}
