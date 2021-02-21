public class Min_Max{
    
    public static void min_max(int[] array){
        int maxVal = Integer.MAX_VALUE;
        int minVal = Integer.MIN_VALUE;
        
        for (int i = 0; i < array.length; i++){
         if (array[i] < maxVal)
           maxVal = array[i];
         if (array[i] > minVal)
           minVal = array[i];
       }
  
       System.out.print ("\nValeur minimale = "+maxVal);
       System.out.print ("\nValeur maximale = "+minVal);
    }
    
    public static void main(String[] args) {
       
       
       int array[] = {51, 24, 19, 5, 37, 76, 61, 99, 101, 36};
  
       for (int nombre:array)
         System.out.print (nombre+" ");
        min_max(array);
      
    }
}