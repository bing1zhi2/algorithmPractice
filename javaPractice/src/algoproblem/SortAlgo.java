package algoproblem;

/**
 * Created by Administrator on 2018/9/18.
 * sort
 */
public class SortAlgo {
    public static void main(String[] args) {
        Integer[] a = new Integer[]{11,42,33,45,5};
        insertionSort(a);
        for (Integer integer : a) {
            System.out.println(integer);
        }
    }
    /**
     * insertion sort
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
}


