public class Sequentielle {

    public static boolean contains(int[] a, int b){
        for (int i : a) {
            if (i==b){
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[] a = {3,2,4,5,3,2,7,6,4};
        boolean ans = contains(a,7);
        if (ans) {
            System.out.println ("Nombre trouve");
        }
        else {
            System.out.println ("Nombre non trouve");
        }

    }
}