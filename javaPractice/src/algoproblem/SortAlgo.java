package algoproblem;

import java.util.Arrays;

/**
 * Created by Administrator on 2018/9/18.
 * sort
 */
public class SortAlgo {
    public static void main(String[] args) {
        Integer[] a = new Integer[]{11,42,33,45,5};
        int[] b = {11, 42, 33, 45 , 5};

//        insertionSort(a);
//        for (Integer integer : a) {
//            System.out.println(integer);
//        }

        sierSort(b);
        for (int i : b) {
            System.out.println(i);
        }





    }
    /**
     * insertion sort
     * 插入排序
     * 思想：
     * 依次把数据插入到合适大小的位置
     * @param a list of T
     * @param <T> anyType extends Comparable
     */
    public static <T extends Comparable<? super T>> void insertionSort(T[] a){
        int j;
        for (int p=1; p<a.length;p++){
            T temp= a[p];
            for(j=p;j>0 && temp.compareTo(a[j-1])<0;j--) {
                a[j] = a[j - 1];
            }
            a[j]=temp;
        }
    }

    /**
     * 插入排序
     * @param a
     */
    public static void insertionSort(int a[]){
        int j;
        for(int p=1; p< a.length; p++){
            int temp = a[p];
            for(j= p; j>0; j--){
                if( temp > a[j-1]){
                    a[j] = a[j-1];

                }else {
                    break;
                }
            }
            a[j] = temp;
        }
    }

    /**
     * 选择排序 普通数组版本
     * 每次找到最小的，把最小的放左边
     * @param arr
     */
    public static void selectionSort(int arr[]){
        for(int i=0;i<arr.length;i++){
            int minIdx = i;

            for(int j =i+1;j<arr.length;j++){
                if(arr[j]<arr[i]){
                    minIdx = j;
                }
            }

            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
        }
    }

    /**
     * 希尔排序
     * @param arr
     */
    public static void sierSort(int arr[]){

        int length = arr.length;
        //区间
        int gap = 1;
        while (gap < length) {
            gap = gap * 3 + 1;
        }
        while (gap > 0) {
            for (int i = gap; i < length; i++) {
                int tmp = arr[i];
                int j = i - gap;
                //跨区间排序
                while (j >= 0 && arr[j] > tmp) {
                    arr[j + gap] = arr[j];
                    j -= gap;
                }
                arr[j + gap] = tmp;
            }
            gap = gap / 3;
        }


    }
}


