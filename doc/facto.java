package exo3;

import java.util.Scanner;

public class facto {
	public static double fact(double n) {
		// ok
		double facto;
		if(n==0 || n==1)
			return facto=1;
		else {
			return fact(n-1)*n;
		}
		 
	}
	public static void main(String[] args) {
		Scanner lire=new Scanner(System.in);
		System.out.println("donner n");
		double n=lire.nextInt();
		System.out.println(fact(n));
	}
}
