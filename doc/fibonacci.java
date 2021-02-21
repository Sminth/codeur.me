package codeur.com;

public class fibonacci {
	/*Auteur: Emmanuel Malan
	date : 13-09-19 ; java
	objet :Fibonacci */

	//fonction recursive
	static int fibonacci_1(int n){
	    int res=1;
		if (n<0) 
	    	System.out.println( "nombre incorrect") ;
	    else if (n==1)
	        res= 0 ;
	    else if (n==2 )
	        res= 1 ;
	    else
	        res= fibonacci_1(n-1)+fibonacci_1(n-2) ;
	    return res;
	}

	//fonction non recursive
	static int fibonacci_2(int n){
	    int a = 0 ; int b = 1 ;
	    int i ; int c;
	    if (n < 0)
	    	System.out.println("nombre incorrect") ;
	    else if (n == 0)
	        return a ;
	    else if (n == 1 )
	        return b ;
	    else{
	        for (i=2;i<n;i++){
	            c = a + b ;
	            a = b ;
	            b = c ;
	        }
	        return b ;
	    }
	    return b;
	}
	public static void main(String[] args) {
		System.out.println("fibonacci (9)= "+fibonacci_1(9));
		System.out.println("fibonacci (0)= "+fibonacci_2(0)+"\n");
	}
}